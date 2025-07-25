# 🧠 SmartMed - Breast Cancer Classification Web App

SmartMed is a deep learning-based web application that classifies grayscale breast images (28x28) as **Benign** or **Malignant**. The goal is to assist in early detection of breast cancer using machine learning, all within a lightweight, deployable environment using Streamlit.

---

## 🚀 Project Overview

Breast cancer is one of the most common types of cancer affecting women worldwide. Early diagnosis significantly improves chances of survival. This project uses a Convolutional Neural Network (CNN) trained on the **BreastMNIST** dataset to predict breast tumor type.

- 📚 Dataset: BreastMNIST from MedMNIST (10,000+ grayscale images)
- 🔍 Problem Type: Binary Classification
- 🛠️ Tech Stack: TensorFlow, Keras, Streamlit
- 🖼️ Image Input: 28x28 grayscale

---

## 📁 Folder Structure

smartmed-classifier/
│
├── app.py # Streamlit web app
├── model/
│ └── breastmnist_model.h5 # Trained CNN model
├── 1_data_loading_visualization.ipynb
├── 2_model_training.ipynb
├── 3_evaluation_prediction.ipynb
├── breast_data.npz # Preprocessed image data
├── requirements.txt # All required packages
└── README.md # Project documentation


---

## ⚙️ Installation & Running Locally

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/rajrishikashyap/smartmed-classifier.git
cd smartmed-classifier

📦 2. Install Dependencies
pip install -r requirements.txt
▶️ 3. Run the Web App
streamlit run app.py
Then open http://localhost:8501 in your browser.

🧪 How to Use
Upload a 28x28 grayscale PNG/JPG breast image.

Model will display:

✅ Predicted Label (Benign or Malignant)

📊 Confidence Score

📉 Bar chart with class probabilities

📊 Model Info
📦 Model: Convolutional Neural Network (CNN)

🧠 Trained on: BreastMNIST

🧪 Accuracy: ~89% on test set

🎯 Optimizer: Adam

🔢 Loss Function: Sparse Categorical Crossentropy

📈 How to Improve This Project
✅ Future Enhancements:

📌 Use transfer learning (e.g. ResNet, EfficientNet) for better generalization.

🔁 Implement data augmentation (rotation, zoom, flip) using ImageDataGenerator.

📊 Add evaluation metrics like ROC-AUC, F1-Score, Confusion Matrix.

🔍 Increase image resolution to 64x64 or 128x128 for more detail.

🧪 Add a real-time camera input (via OpenCV or webcam upload).

🔄 Deploy via Streamlit Cloud, Render, or Hugging Face Spaces.

🌐 Live Deployment (Optional)
You can deploy your app to the web using Streamlit Community Cloud. Just sign in with GitHub, connect your repo, and you're live in minutes.

💾 Sample Image Preview
You can add a preview screenshot here if desired:

bash
Copy
Edit
📸 [Upload a sample image and copy its link to paste here]
