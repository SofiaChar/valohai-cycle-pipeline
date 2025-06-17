import random
import json
import os
import sys

def generate_random_params(num_configs=10):
    # Epochs between 10 and 100
    epochs = [random.randint(10, 100) for _ in range(num_configs)]

    # Learning rates between 0.0001 and 0.1
    lrs = [round(random.uniform(0.0001, 0.1), 5) for _ in range(num_configs)]

    return epochs, lrs


def get_prediction_datum_id():
    INPUTS_PATH = '/valohai/config/inputs.json'
    try:
        with open(INPUTS_PATH, 'r') as f:
            inputs = json.load(f)

        # Ensure the 'predictions' input exists
        if 'predictions' not in inputs:
            print("No 'predictions' input found.")
            return None

        prediction_files = inputs['predictions'].get('files', [])
        if not prediction_files:
            print("No files under 'predictions' input.")
            return None

        # Collect all datum_ids (if they exist)
        datum_ids = [f.get('datum_id') for f in prediction_files if 'datum_id' in f]

        if not datum_ids:
            print("No datum_id found in 'predictions' input files.")
            return None

        return datum_ids

    except FileNotFoundError:
        print(f"File {INPUTS_PATH} not found.")
    except json.JSONDecodeError:
        print("Failed to parse JSON.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None