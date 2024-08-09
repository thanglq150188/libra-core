from pydantic.v1 import BaseModel, Field


class MB_COMPANY_PROFILES_MODEL(BaseModel):
    query: str = Field(
        description="The user's query about MB Bank",
    )


MB_COMPANY_PROFILES = """Use when user ask anything about MB (MB Bank) such as: MB Bank's history,
MB Bank's products and services, MB Bank's achievement, any problem relating to MB.
"""


class MB_JOB_MODEL(BaseModel):
    workplace: str = Field(
        description="The workplace (city or province) where the user wants to work at MB Bank (Nghệ An, Hà Nội, Hồ Chí Minh, etc.)",
    )
    industry: str = Field(
        description="""The industry where the user wants to work at MB Bank.
            In MB Bank, these industries are available:
                - Dịch vụ khách hàng, Ngân hàng, Tài chính / Đầu tư
                - CNTT - Phần mềm, Ngân hàng     
                or combine them with 'và' (and) to get more specific results.
            Ask user until you get the answer.
        """
    )
    welfare: str = Field(
        description="The welfare that the user wants to have at MB Bank (salary, bonus, insurance, etc.)",
    )
    min_salary: int = Field(
        description="The minimum salary that the user wants to have at MB Bank",
    )
    max_salary: int = Field(
        description="The maximum salary that the user wants to have at MB Bank",
    )


MB_JOB = """
Use when the user asks for information about job opportunities at MB Bank.
Or when user tell about their skills and want to know if there is any job at MB Bank that fits their skills.
Note that you always attach the url of the job post to the response.
"""
