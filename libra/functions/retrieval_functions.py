from typing import List, Union, Dict
import json


with open("./data/old_jobs_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


titles = [
    "Chuyên viên Khách hàng Cá nhân",
    "Chương trình The Banker"
    "Chuyên viên Khách hàng Doanh nghiệp",
    "Chuyên viên Tư vấn khách hàng cá nhân",
    "Quản lý chi nhánh"
]


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
    industries = [e.strip() for e in industry.split(',')]
    
    def check_contains(entry: Dict) -> bool: # type: ignore
        contain_industry = False
        for ind in industries:
            if (ind.lower() in entry['title'].lower()):
                contain_industry = True
                
        return contain_industry and entry['workplace'] == workplace
    
    def check_contains_workplace(entry: Dict) -> bool: # type: ignore
        return entry['workplace'] == workplace
        
    results = []
    for entry in data:
        if check_contains(entry):
            results.append(entry)
    
    if len(results) < top_k:
        results = []
        for entry in data:
            if check_contains_workplace(entry):
                results.append(entry)
    
    import random

    if len(results) > top_k:
        results = random.choices(results, k=top_k)
    else:
        results = random.choices(data, k=top_k)
    
    return results
    

if __name__ == "__main__"  :
    result = job_retrieval(industry="Chuyên viên khách hàng cá nhân", workplace="Hà Nội")        
    for entry in result:
        print(entry)
        print()
    