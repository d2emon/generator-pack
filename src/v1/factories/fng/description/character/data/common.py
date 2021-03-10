def with_gender(gender_id, default_values, wrapper):
    values = {
        'gender_id': gender_id,
        **default_values.get(gender_id, {}),
    }

    def f(**kwargs):
        result = {**values}
        result.update(**kwargs)
        yield from wrapper(**values)

    return f
