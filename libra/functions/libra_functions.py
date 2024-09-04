from typing import List, Union, Dict

from libra.functions import OpenAIFunction

from data.prepare_data import (
    JOB_TITLE_RETRIEVER, 
    JOB_DF,
    MB_INFO_RETRIEVER
)

from dotenv import load_dotenv

load_dotenv(override=True)


def mb_information_retrieval(
    query: str,
) -> Dict[str, str]:
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
    results = MB_INFO_RETRIEVER.query(
        query=query,
        top_k=6
    )
    
    retrieved_info_text = "\n".join(
        info['text'] for info in results if 'text' in info
    )
    
    display_text = "\n  - ".join(
        info['metadata']['embed'] for info in results
    )
    
    result = f"""
Lưu ý: Nếu tài liệu không có thông tin cần thiết, cứ trả lời là bạn không có đủ thông tin nên không thể giải đáp.
tài liệu được tìm thấy: {retrieved_info_text}
"""
    return {
        "display": display_text,
        "document": result,
    }

def mb_network_retrieval():
    """Retrieve information about MB Bank branches and transaction offices.
    This function should be used when:
        - The user asks for information about MB Bank's branches or transaction offices.
        - The user wants to know the number of branches or transaction offices in a specific area.
        - The user requests details about a particular branch or transaction office.
    """
    from data.mb_network import mb_network_address
    return {
        "display": "danh sách địa chỉ mạng lưới MB",
        "document": mb_network_address,
    }


def contains_any(industry_list, search_terms):
    return any(any(term.lower() in industry.lower() for term in search_terms) for industry in industry_list)


def pandas_job_retrieval(
    workplace: str = "",
    job_industry: str = "",
    job_title: str = "",
    salary: int = -1,
) -> Dict[str, str]:
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
    output_df = JOB_DF.copy()
    if workplace != "":
        output_df = output_df[output_df['workplace']==workplace]
    else:
        remain_params.append('workplace')
    
    if job_title != "":        
        acquired_job_titles = [title['text'] for title in JOB_TITLE_RETRIEVER.query(job_title, top_k=3)]        
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
    
    result = "không có gì"
    
    if len(remain_params) == 4:
        result = f"There is no parameter provided. Asking user for them, including {remain_params}"
    else:
        if len(output_df) == 0:
            result = "không tìm thấy jobs phù hợp"
        else:        
            acquire_jobs = "\n"
            chosen_size = 3 if len(output_df) > 3 else len(output_df)        
            for entry in output_df.head(chosen_size).iterrows():
                for key in entry[1].keys():
                    acquire_jobs += f"{key}: {entry[1][key]}\n"
                acquire_jobs += "-"*100 +"\n"
            
            if len(output_df) < 3:
                result = f"""
Jobs tìm được: {acquire_jobs}
"""
            else:
                result = f"""
Lưu ý: số lượng jobs tìm được khá lớn, sau khi liệt kê các jobs tìm thấy xong nên yêu cầu khách hàng cung cấp thêm {remain_params} để khoanh vùng lại.             
Jobs tìm được: {acquire_jobs}
"""
    return {
        "display": result,
        "document": result,
    }

LIBRA_FUNCS: List[OpenAIFunction] = [
    OpenAIFunction(func)
    for func in [
        mb_information_retrieval,
        mb_network_retrieval,
        pandas_job_retrieval
    ]
]


if __name__=="__main__":
    print(pandas_job_retrieval(workplace="Hà Nội"))
    
    