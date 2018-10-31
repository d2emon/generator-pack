import random
import math
from PIL import Image, ImageDraw





def parabola(focus, l):
    def x(y):
        xf, yf = focus
        return ((y - yf) ** 2 + xf ** 2 - l ** 2) / (2 * (xf - l))
    return x


def distance(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return math.sqrt(dx ** 2 + dy ** 2)


def simple_voronoi(points, size):
    shapes = [[] for _ in points]
    for x in range(size[0]):
        for y in range(size[1]):
            p = x, y
            d = [distance(p, point) for point in points]
            if d[0] < d[1] and d[0] < d[2] and d[0] < d[3] and d[0] < d[4]:
                shapes[0].append(p)
            elif d[1] < d[0] and d[1] < d[2] and d[1] < d[3] and d[1] < d[4]:
                shapes[1].append(p)
            elif d[2] < d[0] and d[2] < d[1] and d[2] < d[3] and d[2] < d[4]:
                shapes[2].append(p)
            elif d[3] < d[0] and d[3] < d[1] and d[3] < d[2] and d[3] < d[4]:
                shapes[3].append(p)
            elif d[4] < d[0] and d[4] < d[1] and d[4] < d[2] and d[4] < d[3]:
                shapes[4].append(p)
    return shapes


def voronoi(points, size):
    def point_event(point):
        print("PointEvent", point)

    for sweep in range(size[0]):
        swept = filter(lambda point: point[0] == sweep, points)
        for point in swept:
            point_event(point)


def draw_map(voronoi_map):
    print(voronoi_map)


def draw_voronoi():
    def point_ellipse(point):
        x, y = point
        x1, x2 = x - 1, x + 1
        y1, y2 = y - 1, y + 1
        return x1, y1, x2, y2

    size = 512, 512
    points = [
        (100, 100),
        (356, 301),
        (400, 65),
        (324, 145),
        (200, 399),
    ]

    # v = simple_voronoi(points, (512, 512))
    v1 = voronoi(points, (512, 512))

    from scipy.spatial import Voronoi, voronoi_plot_2d
    vor = Voronoi(points)
    print(vor)

    plot = voronoi_plot_2d(vor)
    print(plot)


    image = Image.new('RGB', size)

    draw = ImageDraw.Draw(image)
    colors = (
        (0, 0, 255),
        (0, 255, 0),
        (0, 255, 255),
        (255, 0, 0),
        (255, 0, 255),
    )
    """
    for i, shape in enumerate(v):
        for p in shape:
            draw.ellipse(point_ellipse(p), colors[i])
    """

    for p in points:
        draw.ellipse(point_ellipse(p), (255, 255, 255))

    image.show()

    # return draw_map(v)
