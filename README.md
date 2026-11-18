# Handwritten Digits Recognition (MNIST)

End-to-end machine learning and deep learning project for handwritten digit classification on the MNIST dataset, progressing from a classical linear baseline to Multi-Layer Perceptrons (MLPs) and Convolutional Neural Networks (CNNs), tracked with MLflow/DagsHub, versioned with DVC, and served via a Flask web application[cite: 1, 2, 3, 4].

---

## Project Objectives & Milestones

1. **Milestone 1 — Data Exploration & Classical Baseline**: Exploratory analysis of the 60,000 training images, stratified 54,000 / 6,000 train/validation split, and Logistic Regression baseline using `scikit-learn`[cite: 2].
2. **Milestone 2 — Multi-Layer Perceptron (MLP)**: Deep fully connected architectures built with Keras/TensorFlow, systematic hyperparameter tuning (learning rate, batch size, Batch Normalization, Dropout, EarlyStopping) targeting **< 2% test error**[cite: 2].
3. **Milestone 3 — Convolutional Neural Network (CNN)**: Spatial feature extraction using Conv2D and MaxPooling layers, ablation studies, and error analysis on the 20 worst test predictions targeting **< 1% test error**[cite: 2].
4. **Milestone 4 — Web Application & Testing**: Production Flask application serving the best `.keras` model with strict input validation, full 10-class probability distribution output, interactive drawing canvas, and an automated `pytest` suite[cite: 2].

---

## Repository Structure

```text
handwritten_digits/
├── app/                        # Flask web application (routes, preprocessing, templates)
├── data/                       # Versioned datasets tracked via DVC (.dvc pointers)
├── models/                     # Trained models tracked via DVC (e.g., best_model.keras)
├── notebooks/                  # End-to-end executable notebooks per milestone
│   ├── 01_baseline.ipynb       # Milestone 1: EDA & scikit-learn baseline
│   ├── 02_mlp_experiments.ipynb# Milestone 2: MLP experiments & tuning
│   └── 03_cnn_experiments.ipynb# Milestone 3: CNN architecture & error analysis
├── reports/
│   └── figures/                # Confusion matrices and learning curves
├── src/                        # Reusable Python modules and configuration
├── tests/                      # Unit and integration tests (pytest)
├── .dvc/                       # DVC configuration directory
├── .pre-commit-config.yaml     # Pre-commit hooks (Ruff, YAML/TOML/JSON checks)
├── pyproject.toml              # Project metadata and uv dependency definitions
├── uv.lock                     # Locked dependency tree for reproducible environments
└── README.md                   # Project documentation and experimental report

```

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

### 2. Running on Google Colab

Each notebook includes a universal initialization cell at the top that automatically detects Google Colab, clones the repository, installs dependencies directly from `pyproject.toml` via `uv` (`uv pip install -r pyproject.toml --system`), and pulls versioned data/models via DVC.

---

## MLOps: Experiment Tracking (MLflow / DagsHub) & Data Versioning (DVC)

### Experiment Tracking with MLflow & DagsHub

All training runs, hyperparameters, learning curves, and confusion matrices are logged remotely on DagsHub:

* **DagsHub Repository**: `https://dagshub.com/bruno-coulet/handwritten_digits`

To launch a local MLflow dashboard if inspecting local runs:

```bash
uv run mlflow ui --port 5001

```

(Port 5001 avoids conflicts with the Flask server running on port 5000.)

### Data & Model Version Control (DVC)

Large binary artifacts (datasets and trained `.keras` models) are tracked with **DVC** and synced with DagsHub remote storage rather than committed directly to Git:

```bash
# Pull tracked datasets and best_model.keras from remote storage
uv run dvc pull

# Track a new version of a dataset or trained model
uv run dvc add models/best_model.keras
git add models/best_model.keras.dvc
git commit -m "Update tracked best_model.keras via DVC"
uv run dvc push

```

---

## Usage

### Running the Notebooks

Select the `.venv` Python kernel in VS Code (or open the notebook in Google Colab) and execute the notebooks sequentially:

* `notebooks/1_baseline.ipynb`
* `notebooks/2_mlp_experiments.ipynb`
* `notebooks/3_cnn_experiments.ipynb`

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

Strict evaluation protocol: all architecture and hyperparameter decisions are made exclusively on the 6,000-image validation set. The 10,000-image test set is evaluated only once per milestone.

| Milestone | Model Architecture | Validation Error (%) | Test Error (%) | Parameters | Notes |
| --- | --- | --- | --- | --- | --- |
| **Milestone 1** | Logistic Regression (Baseline) | *TBD* | *N/A* | 7,850 | Linear pixel-wise baseline |
| **Milestone 2** | Best MLP (`784 -> ... -> 10`) | *TBD* | *TBD* | *TBD* | Target: < 2.0% test error   |
| **Milestone 3** | Best CNN (`Conv2D + MaxPool`) | *TBD* | *TBD* | *TBD* | Target: < 1.0% test error   |

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
