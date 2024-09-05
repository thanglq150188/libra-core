from libra.retrievers import VectorRetriever
from libra.vectordb import QdrantStorage
from libra.types import EmbeddingCompany
from libra.embeddings import OpenAIEmbedding, AzureOpenAIEmbedding
from qdrant_client import QdrantClient
from typing import List, Dict
from libra.config import COMMON_CONFIG
import os
from dotenv import load_dotenv

load_dotenv(override=True)

if COMMON_CONFIG.embedding == EmbeddingCompany.OPENAI:
    embedding_instance = OpenAIEmbedding()
elif COMMON_CONFIG.embedding == EmbeddingCompany.AZURE:
    embedding_instance = AzureOpenAIEmbedding()

client = QdrantClient(
    path=os.environ['LOCAL_QDRANT_PATH']
)


def create_query_engine(
    collection_name: str, 
    data: List[Dict[str, str]],
    similarity_threshold: float = 0.2
):
    storage_instance = QdrantStorage(
        client=client,
        vector_dim=embedding_instance.get_output_dim(),
        collection_name=collection_name
    )

    if COMMON_CONFIG.reload_data:
        storage_instance.clear()
    

    retriever = VectorRetriever(
        embedding_model=embedding_instance, 
        storage=storage_instance,
        similarity_threshold=similarity_threshold
    )
    
    if COMMON_CONFIG.reload_data:
        retriever.process(data=data, batch_size=50)
    
    return retriever


def load_company_profile_data():
    from libra.loaders import read_file
    from io import BytesIO
    import json

    company_profiles = []
    file_path = os.path.join('data', 'mb_company_profile_summarized.csv')
    document_content = """
    topic: {topic}
    summary: {summary}
    content: {content}
    """
    with open(file_path, "rb") as f:
        file = BytesIO(f.read())
        file.name = "mb_company_profile_summarized.csv"
        json_file = read_file(file)
        for doc in json_file.docs:
            doc_content = json.loads(doc['page_content'])    
            company_profiles.append({
                "embed": doc_content['summary'],
                "content": document_content.format(
                    topic=doc_content['topic'],
                    summary=doc_content['summary'],
                    content=doc_content['content']
                )
            })
    return company_profiles


def load_job_titles():
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

    embed_jobs_title = [
        {"embed": job_title, "content": job_title} for job_title in job_title_values
    ]
    
    return embed_jobs_title


def load_job_data():
    import re
    import json

    with open("./data/new_jobs_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        

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

    df = pd.DataFrame(refined_data)

    df['min_salary'] = df['min_salary'].astype(int)
    df['max_salary'] = df['max_salary'].astype(int)
    return df


JOB_DF = load_job_data()
    

MB_INFO_RETRIEVER = create_query_engine(
    collection_name="mb_info",
    data=load_company_profile_data(),
    similarity_threshold=0.2
)

JOB_TITLE_RETRIEVER = create_query_engine(
    collection_name="job_title",
    data=load_job_titles(),
    similarity_threshold=0.6
)


if __name__ == "__main__":
    documents = MB_INFO_RETRIEVER.query(
        query="các sếp lớn ở MB gồm những ai ?",
        top_k=5
    )
    for doc in documents:
        print(doc)
        print()