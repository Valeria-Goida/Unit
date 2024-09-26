import math
import unittest


def to_radians(degrees):
    return degrees * (math.pi / 180)

def sin_custom(angle, is_degrees=True, precision=1e-10):
    if is_degrees:
        angle = to_radians(angle)
    sine_value = 0
    term = angle
    n = 1

    while abs(term) > precision:
        sine_value += term
        term *= -angle * angle / ((2 * n) * (2 * n + 1))
        n += 1

    return sine_value

def cos_custom(angle, is_degrees=True, precision=1e-10):
    if is_degrees:
        angle = to_radians(angle)
    cosine_value = 1
    term = 1
    n = 1

    while abs(term) > precision:
        term *= -angle * angle / ((2 * n - 1) * (2 * n))
        cosine_value += term
        n += 1

    return cosine_value


class TestTrigonometricFunctions(unittest.TestCase):

    def test_sin_custom_radians(self):
        self.assertAlmostEqual(sin_custom(0, is_degrees=False), 0, places=10)
        self.assertAlmostEqual(sin_custom(math.pi / 2, is_degrees=False), 1, places=10)
        self.assertAlmostEqual(sin_custom(math.pi, is_degrees=False), 0, places=10)
        self.assertAlmostEqual(sin_custom(3 * math.pi / 2, is_degrees=False), -1, places=10)

    def test_sin_custom_degrees(self):
        self.assertAlmostEqual(sin_custom(0), 0, places=10)
        self.assertAlmostEqual(sin_custom(90), 1, places=10)
        self.assertAlmostEqual(sin_custom(180), 0, places=10)
        self.assertAlmostEqual(sin_custom(270), -1, places=10)

    def test_cos_custom_radians(self):
        self.assertAlmostEqual(cos_custom(0, is_degrees=False), 1, places=10)
        self.assertAlmostEqual(cos_custom(math.pi / 2, is_degrees=False), 0, places=10)
        self.assertAlmostEqual(cos_custom(math.pi, is_degrees=False), -1, places=10)
        self.assertAlmostEqual(cos_custom(3 * math.pi / 2, is_degrees=False), 0, places=10)

    def test_cos_custom_degrees(self):
        self.assertAlmostEqual(cos_custom(0), 1, places=10)
        self.assertAlmostEqual(cos_custom(90), 0, places=10)
        self.assertAlmostEqual(cos_custom(180), -1, places=10)
        self.assertAlmostEqual(cos_custom(270), 0, places=10)

    def test_precision(self):
        self.assertAlmostEqual(sin_custom(30, precision=1e-5), 0.5, places=5)
        self.assertAlmostEqual(cos_custom(60, precision=1e-5), 0.5, places=5)


if __name__ == '__main__':
    unittest.main()