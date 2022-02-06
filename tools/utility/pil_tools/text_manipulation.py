def middle_text_drawer(draw, text, x1, y1, x2, y2):
    text_width, text_height = draw.textsize(text)

    dx = x2 - x1
    dy = y2 - y1

    draw.text((x1 + dx // 2 - text_width // 2, y1 + dy // 2 - text_height // 2), text)
    return draw
