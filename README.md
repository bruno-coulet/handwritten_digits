# Handwritten Digits Recognition (MNIST)

End-to-end machine learning and deep learning project for handwritten digit classification on the MNIST dataset, progressing from a classical linear baseline to Multi-Layer Perceptrons (MLPs) and Convolutional Neural Networks (CNNs), tracked with MLflow/DagsHub, versioned with DVC, and served via a Flask web application.

🔗 **DagsHub Repository & MLflow Experiments**: [https://dagshub.com/bruno-coulet/handwritten_digits](https://dagshub.com/bruno-coulet/handwritten_digits)

---

## Project Objectives & Milestones

1. **Milestone 1 — Data Exploration & Classical Baseline**: Exploratory analysis of the 60,000 training images, stratified 54,000 / 6,000 train/validation split, and Logistic Regression baseline using `scikit-learn`.
2. **Milestone 2 — Multi-Layer Perceptron (MLP)**: Deep fully connected architectures built with Keras/TensorFlow, systematic hyperparameter tuning (learning rate, batch size, Batch Normalization, Dropout, EarlyStopping) targeting **< 2% test error**.
3. **Milestone 3 — Convolutional Neural Network (CNN)**: Spatial feature extraction using Conv2D and MaxPooling layers, ablation studies, and error analysis on the 20 worst test predictions targeting **< 1% test error**.
4. **Milestone 4 — Web Application & Testing**: Production Flask application serving the best `.keras` model with strict input validation, full 10-class probability distribution output, interactive drawing canvas, and an automated `pytest` suite.

---

## Repository Structure

```text
handwritten_digits/
├── app/                         # Flask web application (routes, preprocessing, templates)
├── data/
│   ├── raw/                     # Raw MNIST training set (60,000 images) — tracked via data/raw.dvc
│   └── processed/               # Stratified 54k/6k splits — tracked via data/processed.dvc
├── holdout/                     # Isolated 10,000-image test set — tracked via holdout.dvc
├── models/                      # Trained models tracked via DVC (e.g., best_model.keras)
├── notebooks/                   # End-to-end executable notebooks per milestone
│   ├── 1_baseline.ipynb         # Milestone 1: EDA & scikit-learn baseline
│   ├── 02_mlp_experiments.ipynb # Milestone 2: MLP experiments & tuning
│   └── 03_cnn_experiments.ipynb # Milestone 3: CNN architecture & error analysis
├── reports/
│   └── figures/                 # Confusion matrices, learning curves, and evaluation reports
├── src/
│   └── handwritten_digits/
│       └── config.py            # Centralized project paths, constants, and DagsHub/MLflow config
├── tests/                       # Unit and integration tests (pytest)
├── .dvc/                        # DVC remote storage configuration (DagsHub S3)
├── .pre-commit-config.yaml      # Pre-commit hooks (Ruff, YAML/TOML/JSON checks)
├── pyproject.toml               # Project metadata and uv dependency definitions
├── uv.lock                      # Locked dependency tree for reproducible environments
└── README.md                    # Project documentation and experimental report

```

---

## Centralized Configuration (`src/handwritten_digits/config.py`)

All notebooks and modules import shared constants from `handwritten_digits.config` to ensure consistency across local (WSL/Linux/macOS) and **Google Colab** environments:

| Category | Constant | Value / Description |
| --- | --- | --- |
| **Paths** | `ROOT_DIR` | Repository root directory (auto-detected) |
|  | `RAW_DATA_DIR` | `data/raw` — Raw MNIST training dataset |
|  | `PROCESSED_DATA_DIR` | `data/processed` — Preprocessed `54k / 6k` splits (`mnist_split_54k_6k.npz`) |
|  | `HOLDOUT_DIR` | `holdout` — Strictly isolated 10,000-image test set |
|  | `REPORTS_DIR` / `FIGURES_DIR` | `reports` and `reports/figures` |
| **Data & Seed** | `RANDOM_SEED` | `42` (reproducibility for splits and model initialization) |
|  | `IMAGE_SIZE` | `(28, 28)` |
|  | `NUM_CLASSES` | `10` (digits `0` through `9`) |
| **MLflow / DagsHub** | `DAGSHUB_REPO_OWNER` | `"bruno-coulet"` |
|  | `DAGSHUB_REPO_NAME` | `"handwritten_digits"` |
|  | `EXPERIMENT_BASELINE` | `"1_Baseline"` |
|  | `EXPERIMENT_MLP` | `"2_MLP"` |
|  | `EXPERIMENT_CNN` | `"3_CNN"` |

---

## Installation & Environment Setup

This project uses **[uv](https://docs.astral.sh/uv/)** for Python dependency management (`Python >= 3.12`) defined in `pyproject.toml`.

### 1. Local Setup (VS Code / Terminal)

```bash
# Clone the repository
git clone [https://github.com/bruno-coulet/handwritten_digits.git](https://github.com/bruno-coulet/handwritten_digits.git)
cd handwritten_digits

# Create the virtual environment and install all dependencies from pyproject.toml
uv sync --all-groups

# Install Git pre-commit hooks
uv run pre-commit install

```

To install only production dependencies (for serving the Flask application):

```bash
uv sync --no-dev

```

### 2. DagsHub & DVC Authentication Setup (Collaborators)

1. **MLflow Tracking Credentials**: Create a `.env` file at the repository root (ignored by Git) with your personal DagsHub token (*DagsHub → Settings → Tokens*):
```env
DAGSHUB_USER_TOKEN=<YOUR_DAGSHUB_TOKEN>

```


2. **DVC Remote Storage Credentials**: Configure local S3 credentials for DagsHub (stored locally in `.dvc/config.local`, ignored by Git) and pull the versioned datasets:
```bash
uv run dvc remote modify --local origin access_key_id <YOUR_DAGSHUB_USERNAME>
uv run dvc remote modify --local origin secret_access_key <YOUR_DAGSHUB_TOKEN>

# Download tracked datasets (data/raw, data/processed, holdout)
uv run dvc pull

```



### 3. Running on Google Colab

Each notebook includes a universal initialization cell at the top that automatically detects Google Colab, clones the repository, installs dependencies via `uv`, authenticates with DagsHub using Colab **Secrets** (`DAGSHUB_USER_TOKEN`), and pulls versioned datasets/models via DVC.

---

## MLOps: Experiment Tracking (MLflow / DagsHub) & Data Versioning (DVC)

### Experiment Tracking with MLflow & DagsHub

All training runs, hyperparameters, learning curves, classification reports, and confusion matrices are logged remotely on DagsHub:

* **DagsHub Repository**: [https://dagshub.com/bruno-coulet/handwritten_digits](https://dagshub.com/bruno-coulet/handwritten_digits)

To launch a local MLflow dashboard if inspecting local runs:

```bash
uv run mlflow ui --port 5001

```

(Port 5001 avoids conflicts with the Flask server running on port 5000.)

### Data & Model Version Control (DVC)

Large binary artifacts (`.npz` datasets and trained `.keras` models) are tracked with **DVC** and synced with DagsHub remote storage rather than committed directly to Git:

```bash
# Pull tracked datasets and models from DagsHub remote storage
uv run dvc pull

# Check local data status against .dvc pointers
uv run dvc status

# Track and push updated datasets or trained models
uv run dvc add data/raw data/processed holdout
uv run dvc push
git add data/raw.dvc data/processed.dvc holdout.dvc
git commit -m "data: update tracked datasets via DVC"

```

---

## Usage

### Running the Notebooks

Select the `.venv` Python kernel in VS Code (or open the notebook in Google Colab) and execute the notebooks sequentially:

* `notebooks/1_baseline.ipynb`
* `notebooks/02_mlp_experiments.ipynb`
* `notebooks/03_cnn_experiments.ipynb`

### Launching the Flask Web Application

Ensure the trained model is present under `models/best_model.keras` (via `uv run dvc pull` or downloaded from DagsHub artifacts), then start the local server:

```bash
uv run python app/app.py

```

Open your browser at `http://localhost:5000`.

---

## Quality Assurance & Testing

Run the automated test suite with coverage:

```bash
uv run pytest --cov=app --cov=src --cov-report=term-missing

```

Run code linting and formatting checks manually:

```bash
uv run ruff check .
uv run ruff format --check .

```

Or execute all configured pre-commit hooks across the repository:

```bash
uv run pre-commit run --all-files

```

---

## Experimental Results Summary

Strict evaluation protocol: all architecture and hyperparameter decisions are made exclusively on the 6,000-image validation set (`data/processed/mnist_split_54k_6k.npz`). The 10,000-image test set (`holdout/mnist_test_holdout.npz`) is evaluated only once per milestone.

| Milestone | Model Architecture | Validation Error (%) | Test Error (%) | Parameters | Notes |
| --- | --- | --- | --- | --- | --- |
| **Milestone 1** | Logistic Regression (Baseline) | *TBD* | *N/A* | 7,850 | Linear pixel-wise baseline |
| **Milestone 2** | Best MLP (`784 -> ... -> 10`) | *TBD* | *TBD* | *TBD* | Target: < 2.0% test error |
| **Milestone 3** | Best CNN (`Conv2D + MaxPool`) | *TBD* | *TBD* | *TBD* | Target: < 1.0% test error |

---

## Error Analysis & Key Findings

*(To be completed after Milestone 3 evaluation)*

* **Most Confused Digit Pairs**: ...
* **Analysis of the 20 Worst Test Predictions**: ...
* **Why CNN Outperforms MLP on MNIST**: ...

---

## Documentation & References

* **MLOps Tools**: MLflow Tracking API, DagsHub Integration, DVC (Data Version Control) Documentation.
* **Frameworks & Libraries**: Keras Documentation & Callbacks, scikit-learn Classification Metrics, Flask Quickstart.
* **Technical Literature**: MNIST Database Overview (Yann LeCun et al.), Stanford CS231n: Convolutional Neural Networks.
