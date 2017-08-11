def generate_count(gen, count=1):
    if count == 1:
        return gen()
    res = [gen() for c in count]
    return res
