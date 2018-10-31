from PIL import Image, ImageDraw


scale = 10


def adjust(x0, y0, x1, y1):
    return x0 * scale, y0 * scale, x1 * scale, y1 * scale


def draw_web(universe):
    image = Image.new('RGB', universe.get_size(scale))

    draw = ImageDraw.Draw(image)
    draw.ellipse(universe.get_rect(scale), (32, 32, 32))

    for s in universe.structure:
        draw.ellipse(adjust(*s.point()), s.color)

    return image


def draw_universe(universe):
    image = Image.new('RGB', universe.get_size(scale))

    draw = ImageDraw.Draw(image)
    draw.ellipse(universe.get_rect(scale), (32, 32, 32))

    # for void in universe.voids:
    #     draw.ellipse(void.get_rect(scale), (0, 0, 255))

    for filament in universe.filaments:
        draw.line(filament.line, (filament.density, filament.density, filament.density), filament.width)

    return image


def info(universe):
    print(universe.name)
    print("{} megaparsecs".format(universe.radius))
    image = draw_web(universe)
    image.show()


def universe_info(universe):
    universe.generate_voids()
    universe.generate_map()

    image = draw_universe(universe)
    image.show()
