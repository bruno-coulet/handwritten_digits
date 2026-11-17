# Handwritten Digits: From Perceptron to CNN



Welcome to the **Handwritten Digits** classification repository. This project guides the implementation, evaluation, and web deployment of machine learning and deep learning models to recognize handwritten digits using the MNIST dataset.


## Overview

The goal of this project is to build, evaluate, and deploy deep learning models capable of reading handwritten digits from the **MNIST** (Modified National Institute of Standards and Technology) dataset.

### Key Targets:
- **Scikit-learn Baseline**: Establish initial benchmark with classical machine learning models.
- **Tuned MLP Model**: Achieve **< 2% error** on the test set.
- **Convolutional Neural Network (CNN)**: Achieve **< 1% error** on the test set.
- **Web Interface**: Deploy a Flask application displaying digit predictions with class confidence probabilities and robust input validation.


## MNIST Dataset & Literature Benchmarks

The MNIST dataset consists of 60,000 training images and 10,000 test images of normalized, centered 28x28 pixel grayscale handwritten digits.



## Methodology & Best Practices

1. **Three-Way Data Split (54k / 6k / 10k)**:
   - Split the 60,000 training images into **54,000 training** and **6,000 validation** images.
   - All hyperparameter tuning, architectural choices, and regularization adjustments are made strictly on the validation set.
   - The **10,000 test set images** are evaluated **only once per milestone** at the very end to prevent data leakage.

2. **Reproducibility**:
   - Set fixed random seeds across library calls.
   - Document library versions in `requirements.txt`.

3. **Controlled Experimentation**:
   - Change **only one variable at a time** when comparing candidate models.

4. **Empirical Rigor**:
   - Support explanations using training/validation curves and quantitative metrics rather than theoretical definitions.


## Project Milestones (Paliers)

### Palier 1: Data Exploration & Classical Baseline
- **Data Inspection**: Load MNIST, render sample grids per digit class, and verify class balance.
- **Preprocessing**: Rescale pixel intensities and perform the 54,000 / 6,000 / 10,000 split.
- **Baseline Classifier**: Train a `scikit-learn` baseline model (Logistic Regression or Random Forest).
- **Validation**: Measure validation error and generate a confusion matrix to identify digit pairs most frequently confused.

### Palier 2: Multi-Layer Perceptron (MLP)
- **Architectural Experimentation**: Build an MLP with Keras/TensorFlow. Compare at least **4 configurations** varying network depth/width, learning rate, batch size, or optimizer.
- **Training Analysis**: Plot training and validation loss and error curves across epochs.
- **Empirical Phenomena**:
  - Compare low vs. high learning rates.
  - Observe overfitting and mitigate using `EarlyStopping`, `Dropout`, or L1/L2 regularization.
  - Test the effect of `BatchNormalization` with and without normalization layers.
- **Averaging & Scale**: Calculate iterations per epoch (e.g., 54,000 samples / batch size 128 = 422 iterations/epoch).
- **Optimizer Evaluation**: Compare convergence speed between Adam and SGD.
- **Final Evaluation**: Select the best configuration based on validation metrics and evaluate it **once** on the test set (Target: **< 2% test error**). Output confusion matrix and classification report.

### Palier 3: Convolutional Neural Network (CNN)
- **CNN Architecture**: Construct a CNN with convolutional layers, ReLU activations, pooling layers, and dense output layers.
- **Parameter & Speed Comparison**: Compare total parameter count (`model.summary()`) and training duration between the best MLP and CNN models.
- **Ablation Study**: Analyze model sensitivity by removing pooling layers or adjusting filter counts.
- **Data Augmentation**: Apply spatial transformations (minor rotations and shifts) and evaluate impact on validation error.
- **Feature Map Inspection**: Visualize activations from the first convolutional layer to inspect low-level feature detectors.
- **Error Analysis**: Inspect the **top 20 most severely misclassified test images**. Quantify illegible samples and ground-truth labeling errors to estimate the practical error floor.
- **Target Evaluation**: Evaluate once on the test set (Target: **< 1% test error**).


### Palier 4: Flask Web Application & Unit Testing
- **Model Persistence**: Export the top-performing model to `.keras` format and load it on web application startup.
- **Flask Application**: Build a lightweight web API that accepts an MNIST-formatted image input and returns:
  - The predicted digit class (0-9).
  - Full probability distribution across all 10 target classes.
- **Input Validation**: Cleanly reject invalid file formats, incorrect dimensions, or corrupted payloads with informative HTTP status codes and error messages.
- **Automated Testing (`pytest`)**:
  - Test 1: Verify correct prediction on a known sample test image.
  - Test 2: Verify HTTP rejection of malformed/invalid inputs.
  - Test 3: Confirm predicted class probabilities sum to 1.0.

### Bonus: Interactive Drawing Tool & Real-World Domain Adaptation
- **Drawing Interface**: Implement an interactive HTML/CSS/JS HTML5 Canvas drawing board allowing users to sketch custom digits in real-time.
- **Domain Shift Benchmark**: Test model accuracy across 20 custom user-drawn samples and compare performance against standard MNIST.
- **Preprocessing Alignment**: Identify and correct domain mismatch factors (e.g., canvas color inversion, line thickness normalization, bounding box centering, padding) to restore model precision on real-world hand-drawn inputs.


## Repository Architecture

```
handwritten_digits/
├── notebooks/
│   ├── 01_baseline_exploration.ipynb
│   ├── 02_mlp_experiments.ipynb
│   └── 03_cnn_experiments.ipynb
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── js/canvas.js
│       └── css/style.css
├── models/
│   └── best_model.keras
├── tests/
│   └── test_app.py
├── requirements.txt
└── README.md
```


## Installation & Getting Started

### Prerequisites
- Python 3.10+
- Virtual environment tool (`venv` or `conda`)

### Environment Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd handwritten_digits
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


### Running the Flask Web Application

```bash
python app/app.py
```
Open your browser and navigate to the application URL (e.g. `http://localhost:5000`) to interact with the digit prediction interface.

---

## Running Unit Tests

Execute the automated test suite using `pytest`:

```bash
pytest tests/
```

---

## Documentation & References

- **Official Guides**: Keras Documentation & Callbacks, scikit-learn Classification Metrics, Flask Quickstart.
- **Technical Literature**: MNIST Database Overview (Yann LeCun et al.), Stanford CS231n: Convolutional Neural Networks, A Recipe for Training Neural Networks (Andrej Karpathy), 3Blue1Brown Neural Networks Series.


### Reference Performance in Literature

| Classifier Type | Architecture / Classifier Details | Error Rate (%) |
| :--- | :--- | :--- |
| **Linear Classifier** | Pairwise linear classifier | 7.6% |
| **Random Forest** | Fast Unified Random Forests (RerF) | 2.8% |
| **Dense Network (DNN)** | 2-layer (784-800-10) | 1.6% |
| **Support Vector Machine** | Original SVM baseline | 0.8% |
| **K-Nearest Neighbors** | k-NN with non-linear deformation | 0.52% |
| **Convolutional Network (CNN)** | 6-layer (784-50-100-500-1000-10-10) | 0.27% |
| **State-of-the-Art (SOTA)** | Model ensembles & heavy data augmentation | ~0.20% |
