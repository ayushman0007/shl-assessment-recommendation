import sys
import os
import pandas as pd

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Allow Python to import modules from project root
sys.path.append(BASE_DIR)

from retrieval.retrieve import search_assessments

# Build correct dataset path
data_path = os.path.join(BASE_DIR, "data", "Gen_AI Dataset.xlsx")

df = pd.read_excel(data_path)

rows = []

for query in df["Query"]:

    results = search_assessments(query)

    for r in results:

        rows.append({
            "Query": query,
            "Assessment_url": r["url"]
        })

output = pd.DataFrame(rows)

# Build correct output path
output_path = os.path.join(BASE_DIR, "evaluation", "predictions.csv")

output.to_csv(output_path, index=False)

print("Predictions file generated!")