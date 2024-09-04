import asyncio
import time
import numpy as np
from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

# Constants
NUM_CONCURRENT_USERS = 10000
VECTOR_SIZE = 1024
COLLECTION_NAME = "MBInfo"  # Replace with your actual collection name

# Initialize Qdrant client
client = QdrantClient(path="./libra_qdrant_backup.db")

async def perform_query(client, query_id):
    # Generate a random query vector
    query_vector = np.random.rand(VECTOR_SIZE).tolist()
    
    # Perform a search operation
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=5
    )
    return f"Query {query_id} completed"

async def run_concurrent_queries():
    tasks = [perform_query(client, i) for i in range(NUM_CONCURRENT_USERS)]
    return await asyncio.gather(*tasks)

def run_benchmark():
    start_time = time.time()
    asyncio.run(run_concurrent_queries())
    end_time = time.time()
    
    total_time = end_time - start_time
    print(f"Time taken for {NUM_CONCURRENT_USERS} concurrent queries: {total_time:.2f} seconds")
    print(f"Average time per query: {total_time/NUM_CONCURRENT_USERS:.4f} seconds")

if __name__ == "__main__":
    run_benchmark()