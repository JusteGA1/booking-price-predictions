import pytest
from utils.input_processor import Input


def test_input_longitude():
    example = {
        "latitude": 54.685095,
         "distance": 300,
         "review_score": 8.3,
         "review_amount": 3006,
         "stars3": 0.0,
         "stars4": 1.0,
         "stars5": 0.0
    }
    with pytest.raises(ValueError):
        Input(example)


def test_input_latitude():
    example = {
         "longitude": 25.285243,
         "distance": 300,
         "review_score": 8.3,
         "review_amount": 3006,
         "stars3": 0.0,
         "stars4": 1.0,
         "stars5": 0.0
    }
    with pytest.raises(ValueError):
        Input(example)


def test_input_distance():
    example = {
        "longitude": 25.285243,
         "latitude": 54.685095,
         "review_score": 8.3,
         "review_amount": 3006,
         "stars3": 0.0,
         "stars4": 1.0,
         "stars5": 0.0
    }
    with pytest.raises(ValueError):
        Input(example)


def test_input_review_score():
    example = {
        "longitude": 25.285243,
         "latitude": 54.685095,
         "distance": 300,
         "review_amount": 3006,
         "stars3": 0.0,
         "stars4": 1.0,
         "stars5": 0.0
    }
    with pytest.raises(ValueError):
        Input(example)


def test_input_review_amount():
    example = {
        "longitude": 25.285243,
         "latitude": 54.685095,
         "distance": 300,
         "review_score": 8.3,
         "stars3": 0.0,
         "stars4": 1.0,
         "stars5": 0.0
    }
    with pytest.raises(ValueError):
        Input(example)


def test_input_no_stars():
    example = {
        "longitude": 25.285243,
        "latitude": 54.685095,
        "distance": 300,
        "review_score": 8.3,
        "review_amount": 3006
    }
    assert Input(example).to_list() == [25.285243, 54.685095, 300, 8.3, 3006,
                                        0.0, 0.0, 0.0]


def test_input_one_star():
    example = {
        "longitude": 25.285243,
        "latitude": 54.685095,
        "distance": 300,
        "review_score": 8.3,
        "review_amount": 3006,
        "stars4": 1.0
    }
    assert Input(example).to_list() == [25.285243, 54.685095, 300, 8.3, 3006,
                                        0.0, 1.0, 0.0]
