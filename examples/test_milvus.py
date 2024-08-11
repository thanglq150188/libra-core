import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class MilvusClient:
    def __init__(self):
        self.base_url = "https://in03-ad569fe2c349b98.api.gcp-us-west1.zillizcloud.com/v2/vectordb"
        self.username = os.getenv('MILVUS_USERNAME')
        self.password = os.getenv('MILVUS_PASSWORD')
        
        if not self.username or not self.password:
            raise ValueError("Milvus username and password must be set in environment variables")
        
    def _make_request(self, endpoint, json=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {
        "Authorization": "Bearer 7e78ffceb730d78a2dfa8bd1b96b3bdf1091b76d8655dd7f3032db878af9348415dae822e45637af3caa5cf7fa127f95ee2ddbf2",
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        response = requests.post(url, data=json, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
        
    def create_collection(self, collection_name, dimension):
        payload = {
            "collectionName": collection_name,
            "dimension": dimension,
            "index_file_size": 1024,
            "metricType": "L2"
        }
        return self._make_request("collections/create", json=json.dumps(payload))
    
    def insert(self, collection_name, vectors):
        payload = {
            "collection_name": collection_name,
            "vectors": vectors
        }
        return self._make_request("entities/insert", json=json.dumps(payload))
    
    def search(self, collection_name, query_vectors, top_k):
        payload = {
            "collection_name": collection_name,
            "query_vectors": query_vectors,
            "top_k": top_k
        }
        return self._make_request("entities/search", json=json.dumps(payload))

# Usage example
client = MilvusClient()

try:
    # Create a collection
    result = client.create_collection("test_collection", 128)
    print("Create collection result:", result)

    # Insert vectors
    vectors = [[float(i) for i in range(128)], [float(i+1) for i in range(128)]]  # 128-dimensional vectors
    result = client.insert("test_collection", vectors)
    print("Insert vectors result:", result)

    # Search vectors
    query_vectors = [[float(i+0.1) for i in range(128)]]  # 128-dimensional query vector
    result = client.search("test_collection", query_vectors, 10)
    print("Search result:", result)

except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# import requests

# url = "https://in03-ad569fe2c349b98.api.gcp-us-west1.zillizcloud.com/v2/vectordb/collections/create"

# payload = "{\"collectionName\":\"collection1\",\"dimension\":36,\"metricType\":\"COSINE\",\"vectorField\":\"vector\"}"
# headers = {
#   "Authorization": "Bearer 7e78ffceb730d78a2dfa8bd1b96b3bdf1091b76d8655dd7f3032db878af9348415dae822e45637af3caa5cf7fa127f95ee2ddbf2",
#   "Accept": "application/json",
#   "Content-Type": "application/json"
# }

# response = requests.post(url, data=payload, headers=headers)

# print(response.json())