import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -5, 0]) == 0

def test_all_positive_numbers():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks_longest_last():
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_multiple_streaks_longest_first():
    assert longest_positive_streak([1, 2, 3, 0, 4, 5]) == 3

def test_zeros_and_negatives():
    assert longest_positive_streak([1, 0, 2, -3, 4, 5]) == 2

def test_single_element_list():
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0
    assert longest_positive_streak([0]) == 0
