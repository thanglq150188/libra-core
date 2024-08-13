from libra.loaders import read_file
from io import BytesIO
import json

with open("data/company_profile.csv", "rb") as f:
    file = BytesIO(f.read())
    file.name = "company_profile.csv"
    json_file = read_file(file)
    for doc in json_file.docs:
        print(json.loads(doc['page_content']))
    print(len(json_file.docs))