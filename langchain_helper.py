from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.callbacks import get_openai_callback
from langchain_core.output_parsers import StrOutputParser
from decouple import config

OPEN_API_KEY = config("OPEN_API_KEY",cast=str)
llm = ChatOpenAI(api_key=OPEN_API_KEY,model_name="gpt-3.5-turbo", temperature=0.7,seed= 235, top_p= 0.01)


def generate_cover_letters(job_description, company_name, role, info):

    prompt_template = PromptTemplate(
        input_variables=["job_description", "company_name", "role", "information"],
        template="""You are applying for a job in Germany and need to create a 
        cover letter following the guidelines mentioned. You have the company's job description, your information, and your goal is to create a cover letter 
        that adheres to the Guidelines given below

        Information Provided:
        Job Description: {job_description}
        Company Name: {company_name}
        Role: {role}
        Your information: {information}
        
        Guidelines:
        Length Limit: Ensure your cover letter is between 1 to 2 pages, adhering to the specified maximum length.
        Fully Written Text: Craft your cover letter with fully written text, avoiding bullet points and abbreviations. Save bullet points for the CV.
        Personalized Applications: Tailor your application to match the contents and wording used in the job ad, showcasing personalized interest in the position.
        Language: write the cover letter in English.
        Research the Company: Investigate the company's website and social media channels to understand its values, goals, and culture. Reference this information in your cover letter.
        Subject Line: Include a subject line with a clear reference to the position you are applying for.
        Contact Person: If a contact person is mentioned in the job ad, address the cover letter to him/her.
        Opening Paragraph: Express your interest in the job opening and mention any prior interactions with the company or its representatives.
        Motivation to Work for the Company: Clearly state your motivation to work for the specific company, drawing inspiration from its corporate website or social media channels.
        Qualifications and Soft Skills: Outline your qualifications and relevant soft skills. Avoid generic formulations and provide specific examples from your career.
        Link to Job Requirements: Establish a direct link between your past performance, future goals, and the qualifications outlined in the job ad.
        Closing Paragraph: Mention your availability, salary expectations, visa status, or other crucial factors. Conclude with a friendly call-to-action, expressing openness for further communication.
        ATS-Friendly: Ensure that both your cover letter and CV are ATS-friendly to increase the likelihood of passing through automated screening programs.""",
    )

    with get_openai_callback() as cb:
        output_parser = StrOutputParser()
        llm_chain = prompt_template | llm | output_parser
        response = llm_chain.invoke(
            {
                "job_description": job_description,
                "company_name": company_name,
                "role": role,
                "information": info,
            }
        )

    return response


def generate_job_application_answer(
    question, job_description, company_name, role, info
):
    prompt_template = PromptTemplate(
        input_variables=[
            "job_description",
            "company_name",
            "role",
            "information",
            "question",
        ],
        template="""You are applying for a job in Germany and Question are asked in the Application, Make sure you 
        answer the question with the help of the following keep it short and simple. be causal and calm.make sure the answer is 
        based on information provided and max of 5 sentances.

        Information Provided:
        Question: {question}
        Job Description: {job_description}
        Company Name: {company_name}
        Role: {role}
        Your information: {information}

        Note: Make sure the answer is related with your information.
        Give me atleat 5 different Answers that can be submitted for the question
       """,
    )

    with get_openai_callback() as cb:
        output_parser = StrOutputParser()
        llm_chain = prompt_template | llm | output_parser
        response = llm_chain.invoke(
            {
                "job_description": job_description,
                "company_name": company_name,
                "role": role,
                "information": info,
                "question": question,
            }
        )

    return response


def generate_cold_email_prompt(linkedin_data, company_name, company_url):
    prompt_template = PromptTemplate(
        input_variables=["linkedin_data", "company_name", "company_url"],
        template="""Generate a personalized cold email using the following information:

            LinkedIn Data:
            {linkedin_data}

            Company Name: {company_name}
            Company URL: {company_url}

            Please write a concise and engaging cold email that:
            1. Addresses the person by name
            2. References their professional background or recent achievements
            3. Explains why you're reaching out
            4. Mentions something specific about their company
            5. Includes a clear call-to-action
            6. Keeps the overall length to 4-5 sentences

            The tone should be professional yet friendly, and the email should be tailored to the recipient's background and company.
         """,
    )

    with get_openai_callback() as cb:
        output_parser = StrOutputParser()
        llm_chain = prompt_template | llm | output_parser
        response = llm_chain.invoke(
            {
                "linkedin_data": linkedin_data,
                "company_name": company_name,
                "company_url": company_url,
            }
        )

    return response
