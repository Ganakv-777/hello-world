import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4]) == 4

def test_mixed_values():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_single_negative_values():
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -1, 6]) == 3

def test_zero_breaks_streak():
    assert longest_positive_streak([1, 2, 0, 3]) == 2

