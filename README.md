# 🧠 SmartMed - Breast Cancer Classification Web App

SmartMed is a deep learning web app that classifies breast images as **Benign** or **Malignant** using a CNN trained on the BreastMNIST dataset. Built to explore whether a lightweight model could achieve clinically useful accuracy with minimal preprocessing.

**Live stack:** TensorFlow · Keras · Streamlit · Python

---

## Why I Built This

I wanted to understand whether a simple CNN could reliably classify medical images with minimal preprocessing. BreastMNIST was a good test, small images (28x28), binary classification, real clinical stakes.

**What surprised me:** The model hit ~89% accuracy quickly, but accuracy turned out to be misleading. Class imbalance caused the model to predict "benign" too confidently. I had to tune the decision threshold and switch focus to F1-score and confusion matrix analysis, a more honest measure of performance for imbalanced medical data.

---

## Model

| Detail | Value |
|---|---|
| Architecture | Convolutional Neural Network (CNN) |
| Dataset | BreastMNIST (10,000+ grayscale 28x28 images) |
| Task | Binary Classification (Benign / Malignant) |
| Accuracy | ~89% on test set |
| Optimizer | Adam |
| Loss | Sparse Categorical Crossentropy |

---

## Project Structure
smartmed-classifier/

├── app.py                          # Streamlit web app

├── model/

│   └── breastmnist_model.h5        # Trained CNN model

├── 1_data_loading_visualization.ipynb

├── 2_model_training.ipynb

├── 3_evaluation_prediction.ipynb

├── breast_data.npz                 # Preprocessed data

├── requirements.txt

└── README.md
