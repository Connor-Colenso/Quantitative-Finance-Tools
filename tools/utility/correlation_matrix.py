from PIL import Image, ImageDraw
import yfinance as yf
import pandas as pd
import numpy as np
import itertools
from tools.utility.pil_tools import text_manipulation


def correlation_matrix_generator(securities, period='1y', visual=True, img_name='correlation_matrix', interval='1d'):
    """
    :param securities: List of the securities to be correlated.
    :param period: Period of time over which the asset correlation will take place.
    :param visual: Boolean value, whether or not to generate an image of the matrix.
    :param img_name: Saved image name, defaults to correlation_matrix. Directory can be used.
    :param interval: Interval over which the correlation matrix will be generated. E.g. '1d'
    :return: Correlation matrix as a pandas dataframe. If visual enabled an associated image will be generated.
    """

    correlation_matrix = pd.DataFrame(columns=securities, index=securities)
    assets = []

    for ticker in securities:
        correlation_matrix[ticker][ticker] = 1

        ticker_info = yf.Ticker(ticker)
        asset = ticker_info.history(period=period, interval=interval)['Close']
        asset.name = ticker

        assets.append(asset)

    for asset_pair in itertools.combinations(assets, 2):
        name1 = asset_pair[0].name
        name2 = asset_pair[1].name

        asset1_price_hist = asset_pair[0]
        asset2_price_hist = asset_pair[1]

        correlation = asset1_price_hist.corr(asset2_price_hist)

        correlation_matrix[name1][name2] = correlation
        correlation_matrix[name2][name1] = correlation

    if visual:
        image = image_matrix(matrix=correlation_matrix, scale=50, add_corr=True)
        image.save(f'image_dump/{img_name}.png')

    return correlation_matrix


def image_matrix(matrix, scale=50, add_asset_text=True, add_corr=True, circle_mode=False):
    """
    :param matrix: Pandas matrix dataframe.
    :param scale: Size of each square in pixels.
    :param add_asset_text: Boolean, whether or not to write each assets name on the exterior of the matrix.
    :param add_corr: Boolean, whether or not to show the rounded (3dp) correlation value in the middle of each square.
    :param circle_mode: Boolean, whether or not to render the grid with circles rather than squares.
    :return: PIL Image of the correlation matrix.
    """
    matrix = matrix.fillna(0)

    matrix_len = len(matrix)
    asset_names = list(matrix.columns)
    original_matrix = np.array(matrix)

    max_val = matrix.max().max()
    matrix = np.round(matrix / max_val * 255)
    image = Image.new(mode='RGB', size=(scale * (matrix_len + add_asset_text), scale * (matrix_len + add_asset_text)))
    draw = ImageDraw.Draw(image)

    np_matrix = np.array(matrix)

    if add_asset_text:

        for x, text in zip(range(matrix_len), asset_names):
            draw = text_manipulation.middle_text_drawer(draw, text, (x + 1) * scale, 0, (x + 2) * scale, scale)

        for y, text in zip(range(matrix_len), asset_names):
            draw = text_manipulation.middle_text_drawer(draw, text, 0, (y + 1) * scale, scale, (y + 2) * scale)

    for x in range(matrix_len):

        for y in range(matrix_len):

            val = np_matrix[x][y]

            if val == np.nan:

                val == 0

            if val >= 0:

                b = int(val)
                r = 0

            else:

                r = int(np.abs(val))
                b = 0

            x1 = (x + add_asset_text) * scale
            y1 = (y + add_asset_text) * scale

            x2 = (x + 1 + add_asset_text) * scale
            y2 = (y + 1 + add_asset_text) * scale

            if circle_mode:

                s = scale * (1 - abs(original_matrix[x][y])) / 2
                draw.ellipse((x1 + s, y1 + s, x2 - s, y2 - s), fill=(r, 0, b), width=0)

            else:

                draw.rectangle((x1, y1, x2, y2), fill=(r, 0, b), width=0)

            correlation_val = str(round(original_matrix[x][y], 3))

            if add_corr:
                draw = text_manipulation.middle_text_drawer(draw, correlation_val, x1, y1, x2, y2)

    return image
