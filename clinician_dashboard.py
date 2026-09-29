import streamlit as st
from db import list_cases
from pathlib import Path

st.set_page_config(page_title="Clinician Dashboard", layout="wide")
st.title("CLINICIAN DASHBOARD — REVIEW CASES")

rows = list_cases(200)
if not rows:
    st.info("No cases yet.")
else:
    for r in rows:
        id_, name, age, notes, filename, prediction, score, timestamp = r
        result_text = f"Case {id_} — {name} — {prediction} (score: {score:.3f}) — {timestamp}"
        if prediction == "NORMAL":
            st.success(result_text)
        else:
            st.error(result_text)
        cols = st.columns([1,2,3])
        if Path(filename).exists():
            cols[0].image(str(filename), width=150)
        cols[1].markdown(f"**Notes:**\n{notes}")
        cols[2].markdown(f"**Age:** {age}\n\n**File:** {filename}")
        st.markdown("---")


