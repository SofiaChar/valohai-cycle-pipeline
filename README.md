# 🔁 Valohai Cycle Pipeline

This project demonstrates how to build a cyclic ML pipeline using the [Valohai MLOps platform](https://valohai.com/). It showcases how to:
- Preprocess data
- Train multiple models
- Evaluate and select the best model
- Decide whether to rerun the pipeline with new parameters
- Automatically trigger a new pipeline via Valohai's API

---

## 📁 Project Structure

- `valohai.yaml` – Defines the pipeline steps:
  - `preprocess-dataset`
  - `train-model`
  - `batch-inference`
  - `compare-predictions`
  - `start-cycle` (triggers new pipeline)
- `create_pipeline.json` – The JSON template of the pipeline used for API-based creation.
- `parameter_dumper.py` – Logs metadata like chosen hyperparameters.
- `start_cycle.py` – Generates new hyperparameters and triggers a new pipeline via API call.

---

## 🧠 How It Works

1. **Step 1: Preprocessing**
   - Takes the input dataset and performs preprocessing.

2. **Step 2: Training**
   - Trains models using parameters (e.g., epochs, learning rate) provided as inputs.

3. **Step 3: Evaluation**
   - Compares the model outputs and decides if a "best model" was found.

4. **Step 4: Triggering Cycle**
   - If conditions are met (e.g., `cycle=1`), the `start-cycle` step generates a new set of random hyperparameters and makes an API call to start a new pipeline.

---

## 🔧 Environment Variables

### ✅ Required Variable

To trigger a new pipeline using the Valohai API, make sure you’ve set the following environment variable:

VALOHAI_API_TOKEN

You can rename this in the code if you prefer, just update the corresponding variable name in `start_cycle.py`.


### 🔐 How to Create Your Valohai Token

1. Go to your **Valohai Profile** → **Authentication** → **Manage Tokens**
2. Click **Generate New Token**
3. Copy and save the generated token securely.


### 📦 How to Set the Environment Variable

You can add the token to your Valohai project in one of two ways:

#### 1. Per Execution
When launching a new execution:
- Click **Create Execution**
- Add `VALOHAI_API_TOKEN` under **Environment Variables**

> ⚠️ This token will only be available in the specific execution where it’s defined.

#### 2. Project-Wide (Recommended)
To make it available for all executions:
- Go to **Project Settings** → **Environment Variables** tab
- Add `VALOHAI_API_TOKEN`
- Check the **Secret** checkbox to keep it hidden and secure
