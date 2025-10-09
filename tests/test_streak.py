from streak import longest_positive_streak


def test_empty_list():
    assert longest_positive_streak([]) == 0


def test_multiple_streaks():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3


def test_with_zeros_and_negatives():
    assert longest_positive_streak([1, 2, 0, 4, 5, -1, 3, 4, 5, 6]) == 4


def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5


def test_all_non_positive():
    assert longest_positive_streak([-1, -2, 0, -4, -5]) == 0


def test_single_element_positive():
    assert longest_positive_streak([5]) == 1


def test_single_element_non_positive():
    assert longest_positive_streak([-5]) == 0


def test_streaks_at_beginning_and_end():
    assert longest_positive_streak([1, 2, 3, 0, -1, 4, 5]) == 3
    assert longest_positive_streak([1, 2, 0, -1, 4, 5, 6]) == 3
