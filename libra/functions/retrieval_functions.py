from typing import List

from dotenv import load_dotenv

from libra.embeddings import SentenceTransformerEncoder
from libra.functions import OpenAIFunction
from libra.retrievers import VectorRetriever
from libra.vectordb import QdrantStorage

load_dotenv(override=True)

print("loading embedding model...", end="")
embedding_instance = SentenceTransformerEncoder()
print("finish!")

from qdrant_client import QdrantClient

client = QdrantClient(path="../libra_qdrant.db")

mb_info_storage_instance = QdrantStorage(
    client=client,
    vector_dim=embedding_instance.get_output_dim(),
    # url=os.environ['MILVUS_URI'],
    collection_name="MBInfo",
)

mb_info_retriever = VectorRetriever(
    embedding_model=embedding_instance, storage=mb_info_storage_instance
)


def mb_information_retrieval(
    query: str,
) -> str:
    r"""Retrieves MB Bank information based on a Vietnamese query.

    Use when user ask anything about MB (MB Bank) such as: MB Bank's history,
    MB Bank's products and services, MB Bank's achievement, MB Bank's officer salary, any problem relating to MB.
    Furthermore, if user want to receive advice about career path, use this function to add more context to your answer.

    Args:
        query (str): A Vietnamese language query about MB Bank. You should generate this query as good as you can based on the conversation with user.

    Returns:
        str: Retrieved information formatted as a string, including the original
             query and relevant document excerpts.

    Example:
        response = mb_information_retrieval("thông điệp của tổng giám đốc MB là gì")
        response = mb_information_retrieval("Bạn có biết mức lương của MB như thế nào không")
        response = mb_information_retrieval("Có bao nhiêu nhóm công việc và nhóm nghề nghiệp tại MB ?")
    """
    results = mb_info_retriever.query(query=query, top_k=6)

    retrieved_info_text = "\n".join(info["text"] for info in results if "text" in info)

    # text_info = (
    #     f"câu hỏi:\n{query}\n"
    #     f"Tài liệu cung cấp:\n{retrieved_info_text}"
    # )
    return retrieved_info_text


job_storage_instance = QdrantStorage(
    client=client,
    vector_dim=embedding_instance.get_output_dim(),
    # url=os.environ['MILVUS_URI'],
    collection_name="jobs",
)

job_retriever = VectorRetriever(
    embedding_model=embedding_instance, storage=job_storage_instance
)


def job_retrieval(
    workplace: str,
    industry: str,
    min_salary: int = 10000000,
    max_salary: int = 35000000,
    welfare: str = "",
) -> str:
    r"""Retrieve job opportunities at MB Bank based on user preferences.

    This function should be used when:
    - The user asks for information about job opportunities at MB Bank.
    - The user describes their skills and wants to know if there are any suitable jobs at MB Bank.
    - If the user ask about job family at MB Bank, don't trigger this tool

    If no parameter is provided, ask the user for one of the follow missing information (randomly):
    - workplace
    - industry
    - salary
    If one of them is available, just trigger the tool call

    Parameters:
        workplace (str): The desired workplace (city or province) at MB Bank (e.g., Nghệ An, Hà Nội, Hồ Chí Minh).
        industry (str): The desired industry at MB Bank. Available options:
            - "Dịch vụ khách hàng"
            - "Ngân hàng"
            - "Tài chính / Đầu tư"
            - "CNTT - Phần mềm" (IT, AI...)
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
        "max_salary": max_salary,
    }

    query = str(profile)

    results = job_retriever.query(query=query, top_k=3)
    retrieved_info_text = "\n".join(info["text"] for info in results if "text" in info)

    text_info = (
        f"profile mong muốn:\n{query}\n" f"Các jobs tìm được:\n{retrieved_info_text}"
    )
    return text_info


def mb_network_retrieval():
    """Retrieve information about MB Bank branches and transaction offices.
    This function should be used when:
        - The user asks for information about MB Bank's branches or transaction offices.
        - The user wants to know the number of branches or transaction offices in a specific area.
        - The user requests details about a particular branch or transaction office.
    """
    from data.mb_network import mb_network_address

    return mb_network_address


def job_family_faq_retrieval() -> str:
    """Retrieve recommended answers about job families (nhóm công việc) and career paths (nhóm nghề nghiệp) at MB Bank.
    This function should be used when:
        - Including questions asking about job families, career paths in MB.
            Example:
                - Ở MB có job family không ?
                - Ở MB có các nhóm nghề nghiệp không ?
                - Job family là gì ?
                - Tại các chi nhánh của MB có job family/nhóm nghề nghiệp gì ?
        - Asking about the career road map in MB
            Example:
                - Mình muốn biết về lộ trình thăng tiến của banker tại MB
                - Muốn thành 1 leader / quản lí tại MB thì phải làm sao
                - Là một sinh viên ngành bank, con đường sự nghiệp ở MB có gì thú vị hay không.

    Returns:
    str: The answer bases on the recommended answers, and must to obey the MAIN SYSTEM PROMPT about tone of voice, properties, ...

    Note: If the recommended answer is in markdown format (table), response in markdown format correctly.
    """
    from data.few_shot_job_family import details_job_family_at_mb

    return details_job_family_at_mb


RETRIEVAL_FUNCS: List[OpenAIFunction] = [
    OpenAIFunction(func)
    for func in [mb_information_retrieval, job_retrieval, mb_network_retrieval]
]


if __name__ == "__main__":
    for func in RETRIEVAL_FUNCS:
        print(func.get_openai_tool_schema())
