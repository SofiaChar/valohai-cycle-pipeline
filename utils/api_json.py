create_pipeline = {
  "edges": [
    {
      "source_node": "preprocess",
      "source_key": "preprocessed_mnist.npz",
      "source_type": "output",
      "target_node": "train",
      "target_type": "input",
      "target_key": "dataset"
    },
    {
      "source_node": "preprocess",
      "source_key": "epochs",
      "source_type": "metadata",
      "target_node": "train",
      "target_type": "parameter",
      "target_key": "epochs"
    },
    {
      "source_node": "preprocess",
      "source_key": "learning_rate",
      "source_type": "metadata",
      "target_node": "train",
      "target_type": "parameter",
      "target_key": "learning_rate"
    },
    {
      "source_node": "train",
      "source_key": "model*",
      "source_type": "output",
      "target_node": "evaluate",
      "target_type": "input",
      "target_key": "model"
    },
    {
      "source_node": "evaluate",
      "source_key": "*.json",
      "source_type": "output",
      "target_node": "find-best-model",
      "target_type": "input",
      "target_key": "predictions"
    },
    {
      "source_node": "find-best-model",
      "source_key": "cycle",
      "source_type": "metadata",
      "target_node": "start-cycle",
      "target_type": "parameter",
      "target_key": "cycle"
    }
  ],
  "nodes": [
    {
      "name": "preprocess",
      "type": "execution",
      "on_error": "stop-all",
      "edge_merge_mode": "replace",
      "template": {
        "environment": "0167d05d-a1d7-cc02-8256-6455a6ecfa56",
        "commit": "main",
        "step": "preprocess-dataset",
        "image": "python:3.9",
        "command": "pip install numpy valohai-utils\npython ./preprocess_dataset.py",
        "inputs": {
          "dataset": [
            "https://valohaidemo.blob.core.windows.net/mnist/mnist.npz"
          ]
        },
        "parameters": {
          "epochs": {
            "style": "single",
            "rules": {
              "value": [
                5
              ]
            }
          },
          "learning_rate": {
            "style": "single",
            "rules": {
              "value": [
                0.001
              ]
            }
          },
          "seed": {
            "style": "single",
            "rules": {
              "value": [
                221
              ]
            }
          }
        },
        "runtime_config": {},
        "inherit_environment_variables": True,
        "tags": [],
        "time_limit": 0,
        "environment_variables": {},
        "priority": 0
      }
    },
    {
      "name": "train",
      "type": "task",
      "template": {
        "project": "019778e8-e9d6-7521-5d3d-5880cb41306b",
        "environment": "0167d05d-a1d7-cc02-8256-6455a6ecfa56",
        "commit": "main",
        "step": "train-model",
        "image": "tensorflow/tensorflow:2.6.0",
        "command": "pip install valohai-utils\npython ./train_model.py {parameters}",
        "inputs": {
          "dataset": [
            "https://valohaidemo.blob.core.windows.net/mnist/preprocessed_mnist.npz"
          ]
        },
        "runtime_config": {},
        "inherit_environment_variables": True,
        "tags": [],
        "time_limit": 0,
        "environment_variables": {},
        "priority": 0,
        "type": "grid_search",
        "on_child_error": "continue-and-error",
        "maximum_queued_executions": 1000,
        "parameters": {
          "epochs": {
            "style": "single",
            "rules": {
              "value": ""
            }
          },
          "learning_rate": {
            "style": "single",
            "rules": {
              "value": ""
            }
          }
        }
      },
      "on_error": "stop-all",
      "edge_merge_mode": "replace"
    },
    {
      "name": "evaluate",
      "type": "execution",
      "on_error": "stop-all",
      "edge_merge_mode": "replace",
      "template": {
        "environment": "0167d05d-a1d7-cc02-8256-6455a6ecfa56",
        "commit": "main",
        "step": "batch-inference",
        "image": "tensorflow/tensorflow:2.6.0",
        "command": "pip install pillow valohai-utils\npython ./batch_inference.py",
        "inputs": {
          "model": [],
          "images": [
            "https://valohaidemo.blob.core.windows.net/mnist/four-inverted.png",
            "https://valohaidemo.blob.core.windows.net/mnist/five-inverted.png",
            "https://valohaidemo.blob.core.windows.net/mnist/five-normal.jpg"
          ]
        },
        "parameters": {},
        "runtime_config": {},
        "inherit_environment_variables": True,
        "tags": [],
        "time_limit": 0,
        "environment_variables": {},
        "priority": 0
      }
    },
    {
      "name": "find-best-model",
      "type": "execution",
      "on_error": "stop-all",
      "edge_merge_mode": "replace",
      "template": {
        "environment": "0167d05d-a1d7-cc02-8256-6455a6ecfa56",
        "commit": "main",
        "step": "compare-predictions",
        "image": "python:3.9",
        "command": "pip install numpy valohai-utils\npython ./compare_predictions.py",
        "inputs": {
          "predictions": [],
          "models": []
        },
        "parameters": {},
        "runtime_config": {},
        "inherit_environment_variables": True,
        "tags": [],
        "time_limit": 0,
        "environment_variables": {},
        "priority": 0
      }
    },
    {
      "name": "start-cycle",
      "type": "execution",
      "on_error": "stop-all",
      "edge_merge_mode": "replace",
      "template": {
        "environment": "0167d05d-a1d7-cc02-8256-6455a6ecfa56",
        "commit": "main",
        "step": "set-new-parameters",
        "image": "python:3.9",
        "command": "pip install numpy valohai-utils\npython ./set_new_params_and_cycle.py",
        "inputs": {},
        "parameters": {
          "cycle": {
            "style": "single",
            "rules": {
              "value": 0
            }
          }
        },
        "runtime_config": {},
        "inherit_environment_variables": True,
        "tags": [],
        "time_limit": 0,
        "environment_variables": {},
        "priority": 0
      }
    }
  ],
  "project": "019778e8-e9d6-7521-5d3d-5880cb41306b",
  "tags": [],
  "parameters": {},
  "title": "train-dynamic-pipeline"
}