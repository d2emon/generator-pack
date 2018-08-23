from noise import fill1d, fill2d, fill3d


def test_noise():
    data = [int(i * 8) for i in fill1d(16)]
    # fill2d(16, 16),
    # fill3d(16, 16, 16),
    assert data is None
