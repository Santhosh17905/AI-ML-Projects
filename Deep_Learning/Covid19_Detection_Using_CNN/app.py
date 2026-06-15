import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import cv2
from gradcam import get_gradcam_sequential, overlay_heatmap

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="🩺 COVID-19 Detection AI",
    layout="wide",
    page_icon="🦠"
)

# ---------------------------
# Glassmorphism CSS
# ---------------------------
st.markdown("""
<style>
body {
    background: url('assets/bg.jpg');
    background-size: cover;
    background-attachment: fixed;
}
.glass {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    color: white;
}
h1,h2,h3,h4 { color:#fff; text-shadow:1px 1px 5px rgba(0,0,0,0.5); }
.stButton>button {
    background: linear-gradient(90deg, #0f62fe, #0053ba);
    color: white;
    border-radius: 10px;
    padding:0.6em 1.2em;
    font-size:16px;
    font-weight:bold;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #0053ba, #0f62fe);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="glass">', unsafe_allow_html=True)

# ---------------------------
# Title
# ---------------------------
st.title("🩺 COVID-19 Detection System")
st.write("""
Upload a chest X-ray image, and the AI model will predict if it is **Covid Positive** or **Normal**.  
The AI focus area is shown using **Grad-CAM**.
""")

# ---------------------------
# Load Model
# ---------------------------
@st.cache_resource
def load_covid_model():
    return load_model('model/covid_resnet50.h5')

model = load_covid_model()

# ---------------------------
# File Uploader
# ---------------------------
uploaded_file = st.file_uploader("📂 Upload Chest X-ray Image", type=["jpg","png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img_resized = img.resize((224,224))
    img_array = np.expand_dims(np.array(img_resized)/255.0, axis=0)

    # ---------------------------
    # Prediction
    # ---------------------------
    prediction = model.predict(img_array)[0][0]

    # ---------------------------
    # Layout
    # ---------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Prediction")
        # ImageDataGenerator is alphabetical: Covid=0, Normal=1
        # prediction close to 0 is Covid, close to 1 is Normal
        if prediction < 0.5:
            st.error(f"⚠️ Covid Positive ({(1-prediction)*100:.2f}%)")
            st.write("### Model Confidence")
            st.progress(int((1-prediction)*100))
        else:
            st.success(f"✅ Normal ({prediction*100:.2f}%)")
            st.write("### Model Confidence")
            st.progress(int(prediction*100))

    with col2:
        st.subheader("🔥 AI Focus Area (Grad-CAM)")
        heatmap = get_gradcam_sequential(model, img_array)
        img_cv = cv2.cvtColor(np.array(img_resized), cv2.COLOR_RGB2BGR)
        cam = overlay_heatmap(heatmap, img_cv, alpha=0.5)
        cam_rgb = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
        st.image(cam_rgb, use_container_width=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("""
---
<p style="text-align:center; color:blue;">
Developed with ❤️ by Santhosh S | Powered by Streamlit & TensorFlow
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)