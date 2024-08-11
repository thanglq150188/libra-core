from typing import List

from libra.vectordb import VectorRecord
from libra.vectordb import VectorDBQuery

from libra.vectordb import QdrantStorage


def main():
    # Initialize QdrantStorage with local storage
    storage = QdrantStorage(path='qdrant_demo', vector_dim=512, delete_collection_on_del=True)

    # Add sample vectors to the storage
    sample_vectors = [
        VectorRecord(id="1", vector=[0.1, 0.2, 0.3], payload={"name": "Vector 1"}),
        VectorRecord(id="2", vector=[0.4, 0.5, 0.6], payload={"name": "Vector 2"}),
        VectorRecord(id="3", vector=[0.7, 0.8, 0.9], payload={"name": "Vector 3"}),
    ]
    storage.add(sample_vectors)

    # Query the storage for similar vectors
    query = VectorDBQuery(query_vector=[0.5, 0.5, 0.5], top_k=2)
    results = storage.query(query)

    print("Query Results:")
    for result in results:
        print(result)

    # Delete a vector by its ID
    storage.delete(ids=["2"])

    # Clear the storage
    storage.clear()


if __name__ == "__main__":
    main()