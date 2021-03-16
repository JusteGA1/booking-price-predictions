import numpy as np
import json


class Input:
    """Validates and transforms input values into the list."""
    def __init__(self, data: dict) -> None:
        if "longitude" not in data:
            raise ValueError('Mandatory field "longitude" is missing')
        self.long = data["longitude"]
        if "latitude" not in data:
            raise ValueError('Mandatory field "latitude" is missing')
        self.lat = data["latitude"]
        if "distance" not in data:
            raise ValueError('Mandatory field "distance" is missing')
        self.distance = data["distance"]
        if "review_score" not in data:
            raise ValueError('Mandatory field "review_score" is missing')
        self.review_score = data["review_score"]
        if "review_amount" not in data:
            raise ValueError('Mandatory field "review_amount" is missing')
        self.review_amount = data["review_amount"]
        for i in range(3, 6):
            field_name = "stars" + str(i)
            field_value = 0.0
            if field_name in data:
                field_value = data[field_name]
            setattr(self, field_name, field_value)

    def to_list(self) -> list:
        """Returns all input values to the list."""
        return [self.long, self.lat, self.distance, self.review_score,
                self.review_amount, self.stars3, self.stars4, self.stars5]


def process_input(request_data: str) -> np.array:
    """
    Creates a processing function to transform inputs to the expected
    format.
    """
    inputs_data = json.loads(request_data)["inputs"]
    requests = []
    for input_data in inputs_data:
        requests.append(Input(input_data).to_list())

    return np.asarray(requests)
