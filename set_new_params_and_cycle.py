
from utils.api_json import create_pipeline
from utils.generate_parameters import generate_random_params
if valohai.parameters('cycle').value == 1:

    # Generate new set of params:
    epochs_list, lr_list = generate_random_params(num_configs=5)

    api_token = os.environ["VALOHAI_API_TOKEN"]


    # edit json
    json_with_new_parameters = create_pipeline.deepcopy()


    resp = requests.request(
        url="https://app.valohai.com/api/v0/pipelines/",
        method="POST",
        headers={"Authorization": f"Token {api_token}"},
        json={
            "project": project_id,
            "commit": "main",
            "name": "train-val-pipeline",
        },
    )
    if resp.status_code == 400:
        raise RuntimeError(resp.json())
    resp.raise_for_status()
    data = resp.json()