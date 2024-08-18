from typing import List, Union, Dict

from libra.functions import OpenAIFunction
from libra.retrievers import VectorRetriever
from libra.vectordb import MilvusStorage
from libra.embeddings import SentenceTransformerEncoder, OpenAIEmbedding
import os


from dotenv import load_dotenv

load_dotenv(override=True)

print('loading embedding model...', end='')
embedding_instance = SentenceTransformerEncoder()
print('finish!')

mb_info_storage_instance = MilvusStorage(
    vector_dim=embedding_instance.get_output_dim(),
    url_and_api_key=(os.environ['MILVUS_URI'], "123123"),
    collection_name="MBInfo"
)

mb_info_retriever = VectorRetriever(
    embedding_model=embedding_instance, 
    storage=mb_info_storage_instance
)


def mb_information_retrieval(
    query: str,
) -> str:
    r"""Retrieves MB Bank information based on a Vietnamese query.

    This function searches a local vector storage for information about MB Bank,
    including its history, products, services, achievements, and related issues.

    Args:
        query (str): A Vietnamese language query about MB Bank.

    Returns:
        str: Retrieved information formatted as a string, including the original
             query and relevant document excerpts.

    Example:
        response = mb_information_retrieval("thông điệp của tổng giám đốc MB là gì")
    """
    results = mb_info_retriever.query(
        query=query,
        top_k=3
    )
    
    retrieved_info_text = "\n".join(
        info['text'] for info in results if 'text' in info
    )
    
    text_info = (
        f"câu hỏi:\n{query}\n"
        f"Tài liệu cung cấp:\n{retrieved_info_text}"
    )
    return text_info


job_storage_instance = MilvusStorage(
    vector_dim=embedding_instance.get_output_dim(),
    url_and_api_key=(os.environ['MILVUS_URI'], "123123"),
    collection_name="jobs"
)

job_retriever = VectorRetriever(
    embedding_model=embedding_instance,
    storage=job_storage_instance
)

def job_retrieval(
    workplace: str,
    industry: str,
    welfare: str,
    min_salary: int,
    max_salary: int,
) -> str:
    r"""Retrieve job opportunities at MB Bank based on user preferences.

    This function should be used when:
    - The user asks for information about job opportunities at MB Bank.
    - The user describes their skills and wants to know if there are any suitable jobs at MB Bank.

    Parameters:
        workplace (str): The desired workplace (city or province) at MB Bank (e.g., Nghệ An, Hà Nội, Hồ Chí Minh).
        industry (str): The desired industry at MB Bank. Available options:
            - "Dịch vụ khách hàng"
            - "Ngân hàng"
            - "Tài chính / Đầu tư"
            - "CNTT - Phần mềm"
            These can be combined with 'và' (and) for more specific results.
        welfare (str): Desired welfare benefits (e.g., salary, bonus, insurance).
        min_salary (int): Minimum desired salary at MB Bank.
        max_salary (int): Maximum desired salary at MB Bank.

    Returns:
    str: A formatted string containing the original query and relevant job information, including URLs of job postings.

    Note: Always include the URL of the job posting in the response.
    """
    
    profile = {
        "workplace": workplace,
        "industry": industry,
        "welfare": welfare,
        "min_salary": min_salary,
        "max_salary": max_salary
    }
    
    query = str(profile)
    
    results = job_retriever.query(
        query=query,
        top_k=3
    )
    retrieved_info_text = "\n".join(
        info['text'] for info in results if 'text' in info
    )
    
    text_info = (
        f"profile mong muốn:\n{query}\n"
        f"Các jobs tìm được:\n{retrieved_info_text}"
    )
    return text_info


RETRIEVAL_FUNCS: List[OpenAIFunction] = [
    OpenAIFunction(func)
    for func in [
        mb_information_retrieval,
        job_retrieval
    ]
]


if __name__=="__main__":
    for func in RETRIEVAL_FUNCS:
        print(func.get_openai_tool_schema())
    
    