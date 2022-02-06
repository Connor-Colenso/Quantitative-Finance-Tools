def rectangle_outline(draw, coords, colour):
    """
    :param draw: Image to draw the square on.
    :param coords: Tuple of the squares coordinates (x1, y1, x2, y2).
    :param colour: RGB tuple of the outlines colour.
    :return:
    """
    x1, y1, x2, y2 = coords
    width = 1

    draw.line((x1 + width, y1 + width, x1, y2), fill=colour, width=0)
    draw.line((x1 + width, y1, x2 + width, y1), fill=colour, width=0)
    draw.line((x2, y1 + width, x2, y2 + width), fill=colour, width=0)
    draw.line((x1, y2 + width, x2, y2 + width), fill=colour, width=0)

    return draw
