import os
import copy
import requests
import valohai
from utils.api_json import create_pipeline
from utils.utils import generate_random_params, get_prediction_datum_id


if valohai.parameters('cycle').value == 1:
    # Generate new set of params
    new_epochs, new_lr = generate_random_params(num_configs=3)

    print("New set of parameters generated for cycle pipeline: ")
    print("Epochs: ", new_epochs)
    print("Learning rate: ", new_lr)

    datum_id = get_prediction_datum_id()[0]
    print('datum ', datum_id)

    api_token = os.environ["VALOHAI_API_TOKEN"]

    # Deepcopy to avoid mutating the original template
    json_with_new_parameters = copy.deepcopy(create_pipeline)

    # Find the "preprocess" node and update parameters
    for node in json_with_new_parameters["nodes"]:
        if node["name"] == "preprocess":
            node["template"]["parameters"]["epochs"]["rules"]["value"] = new_epochs
            node["template"]["parameters"]["learning_rate"]["rules"]["value"] = new_lr

            node["template"]["inputs"]["info"] = [f"datum://{datum_id}"]
            break

    # Optionally update pipeline title to reflect the cycle
    json_with_new_parameters["title"] = f"train-dynamic-pipeline-cycle"

    # POST request to Valohai API
    resp = requests.post(
        url="https://app.valohai.com/api/v0/pipelines/",
        headers={"Authorization": f"Token {api_token}"},
        json=json_with_new_parameters,
    )

    if resp.status_code == 400:
        raise RuntimeError(resp.json())
    resp.raise_for_status()

    data = resp.json()
    print("Pipeline created:", data.get("url", "No URL found"))

else:
    print("No cycle pipeline required, we reached the best set of parameters")