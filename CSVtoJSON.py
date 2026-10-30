import pandas as pd
import json
df = pd.read_csv("data.csv")
json_data = df.to_json(orient="records",indent=4)
with open("data.json", "w") as json_file:
    json_file.write(json_data)

print("CSV data has been successfully converted to JSON and saved as 'data.json'")
print("Output Saved in data.json file")