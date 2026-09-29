import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import os
from db import init_db, insert_case
from report import create_report
import smtplib, ssl
import os
import subprocess
import sys
import socket
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

st.set_page_config(page_title="Telemedicine Pneumonia Detection", layout="wide")

# Start the dashboard once for this Streamlit server.
@st.cache_resource
def start_dashboard():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        if connection.connect_ex(("127.0.0.1", 8502)) == 0:
            return None

    dashboard_path = Path(__file__).with_name("clinician_dashboard.py")
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            str(dashboard_path),
            "--server.port",
            "8502",
            "--server.headless",
            "true",
        ],
        cwd=str(dashboard_path.parent),
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
    )


start_dashboard()

# Initialize DB
init_db()

st.title("🩻 TELEMEDICINE — PNEUMONIA DETECTION FROM CHEST X-RAYS 🩻")
st.link_button("Open Clinician Dashboard", "http://localhost:8502")

# Load model (only once)
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model/pneumonia_model.h5")

model = load_model()

with st.form("patient_form"):
    st.subheader("Patient Details")
    name = st.text_input("Patient Name", value="")
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    notes = st.text_area("Notes for clinician (symptoms, history)")

    uploaded_file = st.file_uploader("Upload Chest X-ray", type=["jpg","jpeg","png"])
    submitted = st.form_submit_button("ANALYZE")

if submitted:
    if not uploaded_file:
        st.warning("Please upload an X-ray image.")
    else:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_column_width=False, width=300)

        # preprocess
        img_resized = img.resize((150,150))
        arr = image.img_to_array(img_resized)/255.0
        arr = np.expand_dims(arr, axis=0)

        pred = model.predict(arr)[0][0]
        label = "PNEUMONIA" if pred > 0.5 else "NORMAL"
        st.markdown(f"### Prediction: **{label}**  (score: {pred:.3f})")
        if label == "PNEUMONIA":
            st.error("⚠️ PNEUMONIA DETECTED ⚠️")
        else:
            st.success("✅ NO PNEUMONIA DETECTED ✅")

        # Save locally image
        uploads_dir = Path("uploads")
        uploads_dir.mkdir(exist_ok=True)
        filename = uploads_dir / f"{name.replace(' ','_')}_{int(st.session_state.get('_ts', 0) or 0)}.png"
        img.save(filename)

        # Insert record into DB
        insert_case(name, int(age), notes, str(filename), label, float(pred))

        # Create PDF report
        report_path = create_report(name, age, notes, label, pred, img)
        with open(report_path, "rb") as f:
            st.download_button("Download Report (PDF)", f, file_name=f"{name}_pneumonia_report.pdf", mime="application/pdf")

        # Email sending (optional)
        if st.button("Send report to clinician"):
            smtp_host = os.getenv("SMTP_HOST")
            smtp_port = int(os.getenv("SMTP_PORT", 587))
            smtp_user = os.getenv("SMTP_USER")
            smtp_pass = os.getenv("SMTP_PASS")
            doctor_email = os.getenv("DOCTOR_EMAIL")
            if not all([smtp_host, smtp_user, smtp_pass, doctor_email]):
                st.error("SMTP credentials or doctor email not configured. Set them in .env.")
            else:
                try:
                    # Simple sending with smtplib (attach as binary)
                    import email, email.mime.application
                    from email.mime.multipart import MIMEMultipart
                    from email.mime.base import MIMEBase
                    from email.mime.text import MIMEText
                    from email import encoders

                    message = MIMEMultipart()
                    message["From"] = smtp_user
                    message["To"] = doctor_email
                    message["Subject"] = f"Pneumonia report — {name}"

                    body = f"Patient: {name}\nAge: {age}\nPrediction: {label} (score {pred:.3f})\nNotes: {notes}"
                    message.attach(MIMEText(body, "plain"))

                    # attach pdf
                    with open(report_path, "rb") as f:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={Path(report_path).name}")
                    message.attach(part)

                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_host, smtp_port) as server:
                        server.starttls(context=context)
                        server.login(smtp_user, smtp_pass)
                        server.sendmail(smtp_user, doctor_email, message.as_string())

                    st.success(f"Report sent to clinician at {doctor_email}")
                except Exception as e:
                    st.error(f"Failed to send email: {e}")




# Push-Location "C:\Users\Arunabha dey\Desktop\PNEUMONIA DETECTION"
# & ".\venv\Scripts\python.exe" -m streamlit run app.py --server.port 8501


# Push-Location "C:\Users\Arunabha dey\Desktop\PNEUMONIA DETECTION"
# PS C:\Users\Arunabha dey\Desktop\PNEUMONIA DETECTION> & ".\venv\Scripts\python.exe" -m streamlit run app.py --server.port 8501