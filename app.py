import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import cv2

# Load model
model = load_model("model/breastmnist_model.h5")

st.title("🧠 Breast Cancer Classification - SmartMed")
st.write("Upload a grayscale breast image (28x28) to detect if it's **Benign** or **Malignant**.")

# Upload image
uploaded_file = st.file_uploader("Upload PNG Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    image = image.resize((28, 28))                  # Resize
    img_array = np.array(image) / 255.0             # Normalize
    img_input = img_array.reshape(1, 28, 28, 1)      # Reshape for model

    st.image(image, caption="Uploaded Image", use_column_width=False)
    
    # Predict
    prediction = model.predict(img_input)[0]
    label = np.argmax(prediction)

    classes = ["Benign", "Malignant"]
    confidence = prediction[label]

    st.markdown(f"### 🧾 Prediction: **{classes[label]}**")
    st.markdown(f"Confidence: **{confidence:.2%}**")

    st.bar_chart(prediction)
