# German CV Generator

German CV Generator is a Streamlit-based web application that helps users create tailored cover letters, answer job application questions, and generate cold emails for job applications in Germany.

## Features

1. Cover Letter Generation
2. Job Application Question Answering
3. Cold Email Generation

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/german-cv-generator.git
   cd german-cv-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Usage

Run the Streamlit app:
    ```
    streamlit run main.py
    ```

Navigate to the provided local URL in your web browser to use the application.

### Cover Letter Generation
1. Enter the your information, job description, role, and company name in the sidebar.
2. Click "Generate Cover Letter" to create a tailored cover letter.

### Job Application Question Answering
1. Enter a job application question in the sidebar.
2. Click "Answer the question" to get multiple suitable responses.

### Cold Email Generation
1. Enter LinkedIn data, company name, and company URL in the sidebar.
2. Click "Generate Cold Email" to create a personalized cold email.

## Project Structure

- `main.py`: The main Streamlit application file
- `langchain_helper.py`: Contains helper functions for language model interactions
- `requirements.txt`: List of project dependencies

## Dependencies

- langchain
- streamlit
- python-dotenv
- openai

## Note

Ensure that you have a valid OpenAI API key and sufficient credits to use the language model features.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/german-cv-generator/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)


