import streamlit as st
import requests

st.title("SHL Assessment Recommendation System")

st.write("Enter a job description or hiring query.")

query = st.text_area("Query")

if st.button("Get Recommendations"):

    response = requests.post(
        "http://127.0.0.1:8000/recommend",
        json={"query": query}
    )

    data = response.json()

    st.subheader("Recommended Assessments")

    for r in data["recommended_assessments"]:
        st.write(f"**{r['assessment_name']}**")
        st.write(r["url"])