import math
import plotly
import random

from plotly import graph_objs as go

x = [i for i in range(0, 64)]

def interpolate(x, xmin, ymin, xmax, ymax):
    x0 = x - xmin
    dx = xmax - xmin
    dy = ymax - ymin
    r = ymin + dy * math.sin((x0 / dx) * (math.pi / 2))
    return r

def red_noise(x1, x2):
    return (x1 + x2) / 2

def pink_noise(x1, x2):
    return (x1 + red_noise(x1, x2)) / 2

def violet_noise(x1, x2):
    return (x1 - x2) / 2

def blue_noise(x1, x2):
    return (x1 + violet_noise(x1, x2)) / 2

def filter_noise(noise, noise_filter):
    output = []
    for i in range(len(noise) - 1):
        output.append(noise_filter(noise[i], noise[i+1]))
        # output.append(min(noise[i], noise[i+1]))
    return output

def f(x):
    return random.uniform(-1, 1)

def fill(seed=1):
    random.seed(seed)
    return [f(i) for i in x]

def lift(data, y0=0):
    return [i + y0 for i in data]

noise = [fill(seed) for seed in range(5)]
data = [go.Scatter(x=x, y=lift(filter_noise(noise[i], blue_noise), i*2)) for i in range(5)]
data += [go.Scatter(x=x, y=lift(noise[i], i*2)) for i in range(5)]
# data += [scatterSeed(f2, seed, seed*10 + 50) for seed in range(5)]
plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="hello world")
})

# plotly.offline.plot(
#     data,
#     filename = 'basic-line'
# )
