from libra.loaders import read_file
from io import BytesIO
import json
from libra.vectordb import MilvusStorage


company_profiles = []

with open("data/company_profile.csv", "rb") as f:
    file = BytesIO(f.read())
    file.name = "company_profile.csv"
    json_file = read_file(file)
    for doc in json_file.docs:
        doc_content = json.loads(doc['page_content'])    
        company_profiles.append({
            "Documents Topic": doc_content['Documents Topic'],
            "Document Content": doc_content['Document Content']
        })
        
print(company_profiles[0])