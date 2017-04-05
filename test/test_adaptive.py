import numpy
import pytest
import quadpy


def test():
    val, _ = quadpy.line_segment.adaptive_integrate(
            numpy.sin, [0.0, numpy.pi], 1.0e-10
            )
    exact = 2.0
    assert abs(exact - val) < 1.0e-10

    val, _ = quadpy.line_segment.adaptive_integrate(
            lambda x: x * numpy.sin(x),
            [0.0, numpy.pi],
            1.0e-10
            )
    exact = numpy.pi
    assert abs(exact - val) < 1.0e-10


def test_predefined_intervals():
    val, _ = quadpy.line_segment.adaptive_integrate(
            lambda x: x * numpy.sin(x),
            [
                [0.0, 0.3*numpy.pi, 0.5*numpy.pi],
                [0.3*numpy.pi, 0.5*numpy.pi, numpy.pi],
            ],
            1.0e-10
            )
    exact = numpy.pi
    assert abs(exact - val) < 1.0e-10


@pytest.mark.parametrize('k', range(4, 12))
def test_sink(k):
    val, _ = quadpy.line_segment.adaptive_integrate(
            lambda x: numpy.sin(k*x),
            [0.0, numpy.pi],
            1.0e-10
            )
    exact = (1.0 - numpy.cos(k*numpy.pi)) / k
    assert abs(exact - val) < 1.0e-10
    return


if __name__ == '__main__':
    test_predefined_intervals()
    # test_sink(5)
