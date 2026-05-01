import math
import pytest

from utils import calculate_mean, calculate_std, calculate_median


def test_calculate_mean_basic():
    assert calculate_mean([1, 2, 3]) == 2.0


def test_calculate_std_basic():
    result = calculate_std([1, 2, 3])
    assert math.isclose(result, 0.8164965809, rel_tol=1e-9)


def test_calculate_median_odd():
    assert calculate_median([3, 1, 2]) == 2


def test_calculate_median_even():
    assert calculate_median([4, 1, 2, 3]) == 2.5


def test_calculate_mean_empty_raises():
    with pytest.raises(ValueError):
        calculate_mean([])


def test_calculate_std_empty_raises():
    with pytest.raises(ValueError):
        calculate_std([])
