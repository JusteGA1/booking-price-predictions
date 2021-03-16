import json
import pickle
from flask import Flask, request

from utils.input_processor import process_input
from database import Database
database = Database()

classifier = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict() -> str:
    """Creates route for model prediction for any number of inputs."""
    user_input = request.data
    output = None
    try:
        inputs_data = process_input(user_input)
        predictions = classifier.predict(inputs_data)
        result = [round(float(prediction), 2) for prediction in predictions]
        output = json.dumps({"predicted_prices": result})
        return output, 200

    except ValueError as e:
        output = json.dumps({"error": f"Invalid request: {e}"})
        return output, 400

    except Exception as e:
        output = json.dumps({"error": f"PREDICTION FAILED: {e}"})
        return output, 400

    finally:
        database.add_record(user_input.decode(), output)


@app.route("/last_requests", methods=["GET"], defaults={"amount": 10})
@app.route("/last_requests/<amount>", methods=["GET"])
def get_last_requests(amount: int):
    """
    Creates route for returning data of last prediction requests.
    The default is 10 last requests.
    """
    last_requests = database.get_last_records(amount)

    return json.dumps({"last_requests": last_requests}), 200
