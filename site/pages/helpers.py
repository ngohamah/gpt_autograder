from langchain_core.prompts import PromptTemplate

from constants import OPENAI_API_KEY
import os
import PyPDF2

# set environment variable
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY


def getText(file):
    reader = PyPDF2.PdfReader(file)
    text = ''

    number_of_pages = reader.pages

    # iterate over each page in the pdf file and extract the text
    for page_num in range(len(number_of_pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

    return text


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        return getText(file)


def get_prompt(temp, input_variables):

    prompt_template = PromptTemplate(template=temp,
                                     input_variables=input_variables)

    return prompt_template
