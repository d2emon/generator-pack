import math
import random
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


def draw_filament(filament):
    x0, y0, x1, y1 = filament.line
    x, y = x0 - x1, y0 - y1

    if x == 0:
        angle = 90
    else:
        angle = -math.degrees(math.atan(y / x))

    size, dots = filament.get_dots()
    image = Image.new('RGBA', size, (0, 0, 0, 0))
    # print(dots)
    for dot in dots:
        image.putpixel(*dot)
    return image.rotate(angle, expand=1, resample=Image.BICUBIC)


def draw_universe(universe):
    image = Image.new('RGBA', universe.get_size(scale), (0, 0, 0, 255))

    draw = ImageDraw.Draw(image)

    for filament in universe.filaments:
        # print(filament.line)
        # draw.ellipse(filament.line, (0, 0, filament.density, 255))
        # im.paste(rotated, (x0-2*b, y0-b), rotated)
        x = min(filament.line[0], filament.line[2])
        y = min(filament.line[1], filament.line[3])
        # x, y = filament.line[:2]
        filament_image = draw_filament(filament)
        image.paste(filament_image, (x, y), filament_image)
        # print(filament_image, (x, y), filament.line)
        # draw.line(filament.line, (255, filament.density, filament.density, 255), filament.width + 10)
        # draw.line(filament.line, (255, filament.density, filament.density, 255))

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
