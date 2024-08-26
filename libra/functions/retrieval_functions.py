from typing import List, Union, Dict

from libra.functions import OpenAIFunction
from libra.retrievers import VectorRetriever
from libra.vectordb import MilvusStorage, QdrantStorage
from libra.embeddings import SentenceTransformerEncoder, OpenAIEmbedding
import os


from dotenv import load_dotenv

load_dotenv(override=True)

print('loading embedding model...', end='')
embedding_instance = SentenceTransformerEncoder()
print('finish!')

from qdrant_client import QdrantClient

client = QdrantClient(
    path='./libra_qdrant.db'
)

mb_info_storage_instance = QdrantStorage(
    client=client,
    vector_dim=embedding_instance.get_output_dim(),
    # url=os.environ['MILVUS_URI'],
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
    results = mb_info_retriever.query(
        query=query,
        top_k=6
    )
    
    retrieved_info_text = "\n".join(
        info['text'] for info in results if 'text' in info
    )
    
    return f"""
tài liệu được tìm thấy: {retrieved_info_text}
Lưu ý: Nếu tài liệu không có thông tin cần thiết, cứ trả lời là bạn không có đủ thông tin nên không thể giải đáp.
"""


job_storage_instance = QdrantStorage(
    client=client,
    vector_dim=embedding_instance.get_output_dim(),
    # url=os.environ['MILVUS_URI'],
    collection_name="jobs"
)

job_retriever = VectorRetriever(
    embedding_model=embedding_instance,
    storage=job_storage_instance
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


def mb_network_retrieval():
    """Retrieve information about MB Bank branches and transaction offices.
    This function should be used when:
        - The user asks for information about MB Bank's branches or transaction offices.
        - The user wants to know the number of branches or transaction offices in a specific area.
        - The user requests details about a particular branch or transaction office.
    """
    from data.mb_network import mb_network_address
    return mb_network_address


import json

with open("./data/mb_jobs_7.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    
import re

def parse_salaries(salary_data):
    if isinstance(salary_data, str):
        salaries = ("", "")
        lines = salary_data.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for "a - b VND" format
            match = re.match(r'(\d{1,3}(?:,\d{3})*) - (\d{1,3}(?:,\d{3})*)\s*VNĐ', line)
            if match:
                min_salary = match.group(1).replace(',', '')
                max_salary = match.group(2).replace(',', '')
            else:
                # For other formats, set min and max to the same value
                # Remove "VNĐ" and any leading/trailing whitespace
                value = line.replace('VNĐ', '').strip()
                
                # Try to extract a number if present
                number_match = re.search(r'\d{1,3}(?:,\d{3})*', value)
                if number_match:
                    salary_value = int(number_match.group().replace(',', ''))
                    min_salary = max_salary = salary_value
                else:
                    min_salary = 0
                    max_salary = -1

            salaries = (min_salary, max_salary)
        
        return salaries
    else:
        return (salary_data["junior"]["min"], salary_data["professional"]["max"])
    

refined_data = []

for entry in data:    
    salary_range = parse_salaries(entry["salary_range"])
    min_salary = salary_range[0]
    max_salary = salary_range[1]
    refined_data.append({
        "url": entry["url"],
        "job_title": entry["job_title"],
        "department": entry["department"],
        "job_code": entry["job_code"],
        "workplace": entry["workplace"],
        "job_rank": entry["job_rank"],
        "job_type": entry["job_type"],
        "job_industry": [term.strip() for term in entry["job_industry"].split(",")],
        "deadline_application": entry["deadline_application"],
        "min_salary": min_salary,
        "max_salary": max_salary,
        "job_detail": entry["job_detail"],
        "job_requirements": entry["job_requirements"]
    })
    

import pandas as pd

job_df = pd.DataFrame(refined_data)

job_df['min_salary'] = job_df['min_salary'].astype(int)
job_df['max_salary'] = job_df['max_salary'].astype(int)

def contains_any(industry_list, search_terms):
    return any(any(term.lower() in industry.lower() for term in search_terms) for industry in industry_list)


workplace_values = [
    'Khánh Hòa', 'Hà Nam', 'Đà Nẵng', 'Đắk Lắk', 'Phú Yên', 'Nam Định',
    'Đắk Nông', 'Bình Định', 'Hải Phòng', 'Hà Nội', 'Hồ Chí Minh',
    'Bình Thuận', 'Cần Thơ', 'Sóc Trăng', 'Long An', 'Cà Mau',
    'Tiền Giang', 'Tây Ninh', 'Bình Dương', 'Kiên Giang', 'Đồng Nai',
    'Lâm Đồng', 'Đồng Tháp', 'Bình Phước', 'Bến Tre', 'Trà Vinh',
    'Ninh Bình', 'Hà Tĩnh', 'Thanh Hóa', 'Nghệ An', 'Yên Bái',
    'Vĩnh Phúc', 'Phú Thọ', 'Tuyên Quang', 'Bắc Ninh', 'Thái Nguyên',
    'Sơn La', 'Lào Cai', 'Lạng Sơn', 'Hưng Yên', 'Hòa Bình',
    'Hải Dương', 'Điện Biên', 'Bắc Giang', 'An Giang', 'Bạc Liêu',
    'Hậu Giang', 'Vĩnh Long', 'Bà Rịa - Vũng Tàu', 'Thừa Thiên Huế',
    'Quảng Trị', 'Quảng Ninh', 'Thái Bình', 'Gia Lai', 'Quảng Ngãi',
    'Quảng Nam', 'Quảng Bình', 'Ninh Thuận'
]

job_industry_values = [
    'Bán hàng / Kinh doanh',
    'Bảo trì / Sửa chữa',
    'Bộ phận pháp lý',
    'CNTT - Phần cứng / Mạng',
    'CNTT - Phần mềm',
    'Dịch vụ khách hàng',
    'Hành chính / Thư ký',
    'Kế toán / Kiểm toán',
    'Luật / Pháp lý',
    'Mỹ thuật / Nghệ thuật / Thiết kế',
    'Ngân hàng',
    'Nhân sự',
    'Quản lý điều hành',
    'Quảng cáo / Đối ngoại / Truyền Thông',
    'Tài chính / Đầu tư',
    'Tài chính kế hoạch',
    'Tư vấn'
]

job_title_values = [
    'Chuyên viên Khách hàng Cá nhân',
    'Chuyên viên Tập sự Khách hàng Cá nhân',
    'Chuyên viên Tập sự Khách hàng Doanh nghiệp',
    'Chuyên viên Khách hàng Doanh nghiệp',
    'Chuyên gia Phát triển dịch vụ (API)',
    'Chuyên viên Phát triển dịch vụ thẻ Khách hàng doanh nghiệp (BA thẻ)',
    'Cộng tác viên Tuyển dụng', 'Chuyên viên UB',
    'Chuyên viên Vận hành hệ thống', 'Data Platform Engineer',
    'Quality Assurance (QA)', 'UI UX Designer',
    'Chuyên viên Thúc đẩy bán Sản phẩm Tín dụng', 'Giao dịch viên',
    'Kiểm soát viên', 'Kiểm toán viên (mảng Mô hình, Dữ liệu)',
    'Phó phòng Khách hàng Cá nhân', 'Trưởng phòng Khách hàng Cá nhân',
    'Chuyên viên và Chuyên viên cao cấp Quản trị rủi ro mô hình',
    'Chuyên viên và Chuyên viên cao cấp Kiểm định Mô hình rủi ro',
    'Chuyên viên cao cấp Phân tích nghiệp vụ',
    'Chuyên viên và Chuyên viên cao cấp Xây dựng Mô hình rủi ro',
    'Red Team', 'Pentester', 'Chuyên viên kiến trúc an toàn thông tin',
    'Chuyên viên Giải pháp nền tảng',
    'Chuyên viên Phát triển nguồn lực',
    'Trưởng phòng Khách hàng Doanh nghiệp',
    'Nhân viên hành chính (NS)', 'Kiểm ngân', 'Giám đốc Dịch vụ',
    'Chuyên viên Tài trợ thương mại',
    'Chuyên viên Phát triển Kinh doanh Bancassurance',
    'Chuyên viên và Chuyên viên cao cấp Quản trị rủi ro tích hợp',
    'Chuyên viên Hỗ trợ', 'Giám đốc Quan hệ Khách hàng',
    'Chuyên viên Dịch vụ Tài trợ Thương mại',
    'Chuyên viên Kiểm thử tự động (Automation Tester)',
    'Chuyên viên Khách hàng lớn', 'Network Administrator',
    'Chuyên viên và Chuyên viên cao cấp Phát triển thương hiệu',
    'Chuyên viên và Chuyên viên cao cấp Quản trị nợ',
    'Chuyên viên Quản lý ứng dụng', 'AI Engineer', 'Kỹ sư Devsecops',
    'Chuyên viên cao cấp và Chuyên gia Tư vấn pháp chế',
    'Phó Giám đốc Chi nhánh (SME)', 'Chuyên viên Tập sự UB',
    'Chuyên viên Khách hàng Cá nhân (aRM)',
    'Chuyên viên Cao cấp và Chuyên gia Chính sách và chất lượng dữ liệu',
    'Data Architect', 'Data Engineer', 'Business Analyst',
    'Chuyên viên Cao cấp và Chuyên gia Quản lý cấu trúc dữ liệu',
    'Tester',
    'Chuyên viên và Chuyên viên Cao cấp Mô hình kinh doanh (Data scientist)',
    'Chuyên viên và Chuyên viên Cao cấp Công nghệ mô hình (AI/ML Ops)',
    'Chuyên viên và Chuyên viên Cao cấp Kiểm định mô hình (Model Validation)',
    'Chuyên viên/CVCC Phân tích Khách hàng cá nhân',
    'Chuyên viên và Chuyên viên Cao cấp Phân tích Khách hàng doanh nghiệp',
    'Data Scientist',
    'Chuyên viên và Chuyên viên Cao cấp Phân tích quản trị',
    'Data Analyst',
    'Chuyên viên Phát triển kinh doanh SME Factory Micro Lending Squad',
    'Chuyên viên kinh doanh thẻ',
    'DevOps Engineer (Python, Nodejs, Java)', 'Lập trình viên Backend',
    'Lập trình viên Mobile',
    'Chuyên viên và Chuyên viên cao cấp Giám sát rủi ro tín dụng',
    'Chuyên viên và Chuyên viên cao cấp Chính sách rủi ro tín dụng',
    'Chuyên Viên Quản lý tuân thủ', 'Chuyên viên Điều tra',
    'Chuyên viên và Chuyên viên cao cấp Quản lý pháp chế hệ thống',
    'Kỹ Sư Phát Triển BackEnd', 'Kỹ sư Phát triển Fullstack',
    'Kỹ sư Phát triển AI', 'Kỹ sư phát triển Mobile',
    'Chuyên viên Quản lý xây dựng', 'Title: Giám đốc Dịch vụ',
    'Giám đốc Phòng giao dịch', 'Giám đốc UB',
    'Chuyên viên và Chuyên viên cao cấp Đầu tư chiến lược và M&A',
    'Chuyên viên/ Chuyên viên cao cấp Quản trị rủi ro thị trường'
]


job_title_storage_instance = QdrantStorage(
    client=client,
    vector_dim=embedding_instance.get_output_dim(),
    collection_name="job_title"
)

job_title_retriever = VectorRetriever(
    embedding_model=embedding_instance,
    storage=job_title_storage_instance,
    similarity_threshold=0.6
)


def pandas_job_retrieval(
    workplace: str = "",
    job_industry: str = "",
    job_title: str = "",
    salary: int = -1,
) -> str:
    r"""Retrieve job opportunities at MB Bank based on user preferences.
    This function should be used when:
    - The user asks for information about job opportunities at MB Bank.
    - The user describes their skills and wants to know if there are any suitable jobs at MB Bank.
    - If the user ask about job family at MB Bank, don't trigger this tool
    
    If a parameter is not provided, just leave it, don't try to make up an value for it
    
    Parameters:
        workplace (str): địa điểm làm việc mong muốn, phải tìm cách ánh xạ giá trị user cung cấp vào một trong những giá trị sau: 
                    ['Khánh Hòa', 'Hà Nam', 'Đà Nẵng', 'Đắk Lắk', 'Phú Yên', 'Nam Định',
                    'Đắk Nông', 'Bình Định', 'Hải Phòng', 'Hà Nội', 'Hồ Chí Minh',
                    'Bình Thuận', 'Cần Thơ', 'Sóc Trăng', 'Long An', 'Cà Mau',
                    'Tiền Giang', 'Tây Ninh', 'Bình Dương', 'Kiên Giang', 'Đồng Nai',
                    'Lâm Đồng', 'Đồng Tháp', 'Bình Phước', 'Bến Tre', 'Trà Vinh',
                    'Ninh Bình', 'Hà Tĩnh', 'Thanh Hóa', 'Nghệ An', 'Yên Bái',
                    'Vĩnh Phúc', 'Phú Thọ', 'Tuyên Quang', 'Bắc Ninh', 'Thái Nguyên',
                    'Sơn La', 'Lào Cai', 'Lạng Sơn', 'Hưng Yên', 'Hòa Bình',
                    'Hải Dương', 'Điện Biên', 'Bắc Giang', 'An Giang', 'Bạc Liêu',
                    'Hậu Giang', 'Vĩnh Long', 'Bà Rịa - Vũng Tàu', 'Thừa Thiên Huế',
                    'Quảng Trị', 'Quảng Ninh', 'Thái Bình', 'Gia Lai', 'Quảng Ngãi',
                    'Quảng Nam', 'Quảng Bình', 'Ninh Thuận']
        job_industry (str): ngành nghề mong muốn của user, phải tìm cách ánh xạ giá trị user cung cấp vào một trong những giá trị sau:
                    ['Bán hàng / Kinh doanh',
                    'Bảo trì / Sửa chữa',
                    'Bộ phận pháp lý',
                    'CNTT - Phần cứng / Mạng',
                    'CNTT - Phần mềm',
                    'Dịch vụ khách hàng',
                    'Hành chính / Thư ký',
                    'Kế toán / Kiểm toán',
                    'Luật / Pháp lý',
                    'Mỹ thuật / Nghệ thuật / Thiết kế',
                    'Ngân hàng',
                    'Nhân sự',
                    'Quản lý điều hành',
                    'Quảng cáo / Đối ngoại / Truyền Thông',
                    'Tài chính / Đầu tư',
                    'Tài chính kế hoạch',
                    'Tư vấn']
        job_title (str): chức danh nghề nghiệp mong muốn của user
        salary (int): mức lương mong muốn
    """
    
    remain_params = []
    output_df = job_df.copy()
    if workplace != "":
        output_df = output_df[output_df['workplace']==workplace]
    else:
        remain_params.append('workplace')
    
    if job_title != "":        
        acquired_job_titles = [title['text'] for title in job_title_retriever.query(job_title, top_k=3)]        
        output_df = output_df[output_df['job_title'].isin(acquired_job_titles)]
    else:
        remain_params.append('job_title')
        
    if job_industry != "":
        output_df = output_df[output_df['job_industry'].apply(lambda x: contains_any(x, [job_industry]))]
    else:
        remain_params.append('job_industry')
        
    if salary > 0:
        output_df = output_df[(output_df['min_salary'] < salary) & (output_df['max_salary'] > salary)]
    else:
        remain_params.append('salary')
        
    if len(remain_params) == 4:
        return f"There is no parameter provided. Asking user for them, including {remain_params}"
    else:
        if len(output_df) == 0:
            return "không tìm thấy jobs phù hợp"
        else:        
            acquire_jobs = "\n"
            chosen_size = 3 if len(output_df) > 3 else len(output_df)        
            for entry in output_df.head(chosen_size).iterrows():
                for key in entry[1].keys():
                    acquire_jobs += f"{key}: {entry[1][key]}\n"
                acquire_jobs += "-"*100
            
            if len(output_df) < 3:
                return f"""
Jobs tìm được: {acquire_jobs}
"""
            else:
                 return f"""
Jobs tìm được: {acquire_jobs}
Lưu ý: số lượng jobs tìm được khá lớn, nên yêu cầu khách hàng cung cấp thêm {remain_params} để khoanh vùng lại.
"""

USAGE_FUNCS: List[OpenAIFunction] = [
    OpenAIFunction(func)
    for func in [
        mb_information_retrieval,
        mb_network_retrieval,
        pandas_job_retrieval
    ]
]


if __name__=="__main__":
    print(pandas_job_retrieval(workplace="Hà Nội"))
    
    