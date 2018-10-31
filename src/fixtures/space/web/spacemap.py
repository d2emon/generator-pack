from PIL import Image, ImageDraw


scale = 10


def adjust(x0, y0, x1, y1):
    return x0 * scale, y0 * scale, x1 * scale, y1 * scale


def draw_web(universe):
    size = (
        int(universe.diameter * scale),
        int(universe.diameter * scale),
    )

    image = Image.new('RGB', size)

    draw = ImageDraw.Draw(image)
    draw.ellipse(adjust(0, 0, universe.diameter, universe.diameter), (32, 32, 32))

    for s in universe.structure:
        draw.ellipse(adjust(*s.point()), s.color)

    return image


def info(universe):
    print(universe.name)
    print("{} megaparsecs".format(universe.radius))
    image = draw_web(universe)
    image.show()
