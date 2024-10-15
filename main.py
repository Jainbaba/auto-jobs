import langchain_helper as lch
import streamlit as st

st.title("German Cover Letter Agent")

job_description = st.sidebar.text_area("Job Description")

role = st.sidebar.text_input("Role")

company_name = st.sidebar.text_input("Company Name")

info = """ 
Introduction:
Embarking on a professional journey in the dynamic field of software engineering, I, Hrithik Jain, have 
honed my skills and expertise through hands-on experiences, rigorous learning, and a deep passion for 
technology. This article provides an insightful overview of my educational background, professional journey, 
key projects, certifications, and the story behind my passion for technology.

Education:
Graduating from Christ University in May 2021 with a Bachelor's degree in Computer Science, I laid the 
foundation for my journey into the intricate world of software engineering. My academic endeavors instilled a 
solid understanding of fundamental concepts, laying the groundwork for my future endeavors.

Early Passion for IT:
My enthusiasm for technology blossomed during my school days, where I earned the title of IT head, 
managing the desktop and classroom smart studying system. This early exposure ignited my interest in 
using computers to work intelligently and efficiently.

College Adventures at Christ University:
During my college days at Christ University in Bangalore, I wore many hats. Known for being the IT head 
of my class, I managed to balance academics with a love for gaming. I even challenged the stereotype by 
playing CS:GO on a Mac, proving that gaming on a Mac can be just as enjoyable. In fact, my gaming skills 
earned me 2nd place in a CS:GO tournament, showcasing my competitive spirit.

Hackathon Collaboration:
A significant milestone in my journey was participating in a Hackathon where I collaborated with a 
diverse team of six, including three students from Germany. We spent weeks planning and connecting online, 
culminating in a week of offline collaboration at Christ Campus in Bangalore, which I had the honor of hosting. 
It was during this event that I developed my first Python-based Django Framework project called Svaath, 
sparking my love for creating web applications with Django.

Fast Track Program and Internship at My-Tech Solutions:
To further refine my skills, I enrolled in a Fast Track Program in college, allowing me to complete my last 
semester through an internship. This decision led me to join My-Tech Solutions as a Software Engineer intern. 
Here, I gained valuable experience developing applications using Flutter, Firebase, and Django. Remarkably, 
I managed to complete both the 5th and 6th semester curricula within the duration of a single semester.

Professional Experience at Infosys:
Joining Infosys as a Senior System Associate in March 2018, I have been actively involved in optimizing 
end-to-end insurance application management. Achieving a remarkable 99(%) accuracy, my contributions 
ensured compliance with regulatory standards, showcasing my commitment to precision and excellence.

Innovations at Infosys:
A significant facet of my role involved developing custom Electronic Data Interchange (EDI) 
file handling solutions for clients. This initiative not only reduced lead time by up to 40%, 
delivering cost savings, but also maintained industry standards. My dedication to efficiency 
was further exemplified by mending defects in automation scripts, reducing the risk of malfunction, 
and improving performance by condensing code length and time complexity by 25%.

Manual Testing Expertise:
Within a span of six months, I identified and resolved over 200 bugs in clients' web applications 
through meticulous manual testing. This hands-on experience sharpened my problem-solving skills 
and contributed to the enhancement of application reliability.

Transition to Automation Team:
Acknowledging my comprehensive knowledge and training, I transitioned to the Automation team. A 
three-month intensive training program equipped me with proficiency in C Sharp Programming, 
Database Management, and Test Automation using Selenium and UFT.

Certifications:

Introduction to Python (Infosys):
Credential ID: ZFPUBKEU1S

Advanced Python Concepts (Infosys):
Credential ID: ESNR1HEFLX

Java Programming Fundamentals (Infosys):
Credential ID: DTFEOEQX3M

These certifications underscore my commitment to continuous learning and mastery of programming 
languages, reinforcing my ability to adapt to emerging technologies and industry standards.

Internship at My Tech Solutions Pvt Ltd.:
My stint as a Software Development Engineering Intern at My Tech Solutions Pvt Ltd. from November 
2020 to November 2021 allowed me to explore cutting-edge technologies. Developing an Android app 
with Flutter, I showcased an efficient and scalable platform using Firebase as the backend, resulting 
in a 35(%) increase in efficiency.

Noteworthy Projects:
Connect Dev - Social Media Application (Django Project - February 2023):
Welcome to Connect Dev, the ultimate platform for developers to come together, connect, 
and engage in vibrant discussions about a multitude of topics within the world of technology. 
This Django-based project fosters a sense of community among developers, providing a space where 
they can share their expertise, seek advice, and build connections with like-minded individuals.

IPL Simulation - Cricket Match Stimulator (Python Project - July 2023):
The Cricket Match Simulation project is a comprehensive and flexible script that simulates a 
cricket match. It allows developers and cricket enthusiasts to simulate and analyze cricket 
matches using realistic game mechanics. The project combines multiple classes, modules, and 
utility functions to create an immersive cricket match simulation experience.

SVAATH - Healthcare Platform (Django Project - March 2020):
'SVASTH' is a web application that provides online medical services to everyone at their doorstep. 
This web application is more effective, quick in providing medical help, especially to people in 
remote areas. The digitalization of healthcare systems is needed as hospitals bridge the gap between 
patients all across the country in India.

Passion for Technology and Conclusion:
My journey in software engineering has been marked by a passion for technology, a commitment to excellence, 
and a thirst for knowledge. From optimizing insurance applications to spearheading cutting-edge projects, 
obtaining relevant certifications, and sharing the joy of collaborative learning in international settings, 
I continue to evolve and contribute to the ever-evolving landscape of software development. As I look 
forward to new challenges and opportunities, I am poised to make lasting contributions to the world of 
technology.
""" 

submit = st.sidebar.button("Generate Cover Letter",type="primary")
info = st.sidebar.text_area("Your Information", height=300, help="Enter your personal and professional information here.")

if submit:
    response = lch.generate_cover_letters(job_description,company_name,role,info)
    st.text(response)

question = st.sidebar.text_input("Question")
submitQ = st.sidebar.button("Answer the question",type="primary")

if submitQ:
    response = lch.generate_job_application_answer(job_description,company_name,role,info,question)
    st.text(response)

# New section for cold email generation
st.sidebar.markdown("---")
st.sidebar.subheader("Cold Email Generator")

linkedin_data = st.sidebar.text_area("LinkedIn Data")
cold_email_company_name = st.sidebar.text_input("Cold Email Company Name")
company_url = st.sidebar.text_input("Company URL")

generate_cold_email = st.sidebar.button("Generate Cold Email", type="primary")

if generate_cold_email:
    if linkedin_data and cold_email_company_name and company_url:
        response = lch.generate_cold_email_prompt(linkedin_data, cold_email_company_name, company_url)
        st.subheader("Generated Cold Email")
        st.text(response)
    else:
        st.warning("Please fill in all fields for cold email generation.")
