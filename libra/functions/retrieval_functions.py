from typing import List, Union, Dict

from libra.functions import OpenAIFunction
from libra.retrievers import VectorRetriever
from libra.vectordb.qdrant import QdrantStorage
from libra.vectordb import qdrant_instance
from libra.embeddings import bge_instance


import json

with open("./data/old_jobs_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    
import pandas as pd

jobs_df = pd.DataFrame(data)


def job_retrieval(
    workplace: str = "",
    industry: str = "",
    top_k: int = 3
) -> List[Dict]: # type: ignore
    r"""Retrieve job opportunities at MB Bank based on user preferences.

    This function should be used when:
    - The user asks for information about job opportunities at MB Bank.
    - The user describes their skills and wants to know if there are any suitable jobs at MB Bank.
    - If the user ask about job family at MB Bank, don't trigger this tool
    
    Parameters:
        workplace (str): The desired workplace (city or province) at MB Bank (e.g., Nghệ An, Hà Nội, Hồ Chí Minh).
        industry (str): The desired industry at MB Bank.

    Returns:
    str: A formatted string containing the original query and relevant job information, including URLs of job postings.

    Note: Always include the URL of the job posting in the response.
    """
    output_df = jobs_df.copy()    
    
    output_df = output_df[output_df['workplace'] == workplace]
    workplace_df = output_df.copy()
            
    if industry != "":
        mask = output_df['industry'].str.contains(industry, case=False, na=False)
        output_df = output_df[mask]
    
    json_result = output_df.to_json(orient='records', force_ascii=False)
    json_result = json.loads(json_result)
    
    import random 
    if len(json_result) >= top_k:

        json_result = random.choices(json_result, k=top_k)
    else:
        json_result = jobs_df.to_json(orient='records', force_ascii=False)
        json_result = random.choices(json_result, k=top_k)
    
    return json_result


if __name__ == "__main__"  :
    result = job_retrieval(industry="Ngân hàng")
    print(len(result))
    