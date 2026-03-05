import streamlit as st
import requests
import os

st.title("SHL Assessment Recommendation System")

st.write("Enter a job description or hiring query.")

query = st.text_area("Query")

if st.button("Get Recommendations"):
    # Get API URL from environment or use default
    api_url = os.getenv("API_URL", "https://shl-assessment-recommendation-kk6m.onrender.com")
    
    response = requests.post(
        f"{api_url}/recommend",
        json={"query": query}
    )

    data = response.json()

    st.subheader("Recommended Assessments")

    for r in data["recommended_assessments"]:
        st.write(f"**{r['assessment_name']}**")
        st.write(r["url"])