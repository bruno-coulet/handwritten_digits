"""Module : config.py
Description :
Global configuration, filesystem paths, hyperparameter defaults, and MLflow/DagsHub constants for handwritten-digits
"""

import os
from pathlib import Path
from typing import Final

# Résolution des répertoires avec la structure src-layout :
# __file__        -> .../src/handwritten_digits/config.py
# .parent         -> .../src/handwritten_digits (PACKAGE_DIR)
# .parents     -> .../src (SRC_DIR)
# .parents     -> .../ (BASE_DIR - Racine du projet)
PACKAGE_DIR: Final[Path] = Path(__file__).resolve().parent  # .../src/handwritten_digits
SRC_DIR: Final[Path] = PACKAGE_DIR.parent  # .../src
BASE_DIR: Final[Path] = SRC_DIR.parent  # .../ (Racine du projet)

# Directories paths
DATA_DIR: Final[Path] = BASE_DIR / "data"
RAW_DATA_DIR: Final[Path] = DATA_DIR / "raw"
CLEAN_DATA_DIR: Final[Path] = DATA_DIR / "clean"
PROCESSED_DATA_DIR: Final[Path] = DATA_DIR / "processed"
# Test set holdout directory
HOLDOUT_DIR: Final[Path] = BASE_DIR / "holdout"

# dataset sizes (54k train / 6k validation / 10k test)
TRAIN_SIZE: Final[int] = 54_000
VAL_SIZE: Final[int] = 6_000
TEST_SIZE: Final[int] = 10_000

# MNIST dataset constants
IMAGE_SIZE: Final[tuple[int, int]] = (28, 28)
IMAGE_CHANNELS: Final[int] = 1
NUM_CLASSES: Final[int] = 10
RANDOM_SEED: Final[int] = 42

MODELS_DIR: Final[Path] = BASE_DIR / "models"
BEST_MODEL_PATH: Final[Path] = MODELS_DIR / "best_model.keras"
NOTEBOOKS_DIR: Final[Path] = BASE_DIR / "notebooks"
TESTS_DIR: Final[Path] = BASE_DIR / "tests"
REPORTS_DIR: Final[Path] = BASE_DIR / "reports"
FIGURES_DIR: Final[Path] = REPORTS_DIR / "figures"

# Default hyperparameters (Keras / TensorFlow)
DEFAULT_BATCH_SIZE: Final[int] = 128
DEFAULT_EPOCHS: Final[int] = 30
DEFAULT_LEARNING_RATE: Final[float] = 1e-3

REPO_OWNER = "bruno-coulet"
REPO_NAME = "handwritten_digits"

# Configuration DagsHub & MLflow
DAGSHUB_REPO_OWNER: Final[str] = os.getenv("DAGSHUB_REPO_OWNER", "bruno-coulet")
DAGSHUB_REPO_NAME: Final[str] = os.getenv("DAGSHUB_REPO_NAME", "handwritten_digits")

MLFLOW_DB_PATH: Final[Path] = BASE_DIR / "mlflow.db"
MLFLOW_TRACKING_URI: Final[str] = os.getenv(
    "MLFLOW_TRACKING_URI",
    f"sqlite:///{MLFLOW_DB_PATH.resolve()}",
)

# MlFlow experiments names
EXPERIMENT_BASELINE: Final[str] = "1_Baseline"
EXPERIMENT_MLP: Final[str] = "2_MLP"
EXPERIMENT_CNN: Final[str] = "3_CNN"

# Valeur par défaut (surchargeable via variable d'environnement si besoin)
DEFAULT_EXPERIMENT_NAME: str = os.getenv("MLFLOW_EXPERIMENT_NAME", EXPERIMENT_BASELINE)
