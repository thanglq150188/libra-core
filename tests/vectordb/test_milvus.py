# from dotenv import load_dotenv
# from libra.embeddings import OpenAIEmbedding

# load_dotenv(override=True)

# embedding_instances = OpenAIEmbedding()

# from libra.vectordb import MilvusStorage

# storage_instances = MilvusStorage(
#     vector_dim=embedding_instances.get_output_dim(),
#     url_and_api_key=('milvus_demo.db', '123123'),
#     collection_name='hello_milvus' 
# )

from pymilvus import MilvusClient

client = MilvusClient("milvus_demo.db")