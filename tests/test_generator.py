from generator_runner import run_generator


def test_generator():
    args = []
    assert run_generator(args) is None
