import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


from constants import TEMPLATE_3
from helpers import get_prompt, getText, read_pdf
from assignment6 import get_model_response

def page3():
    st.title("A3: Initial Strategy Backtest")

    uploaded_file = st.file_uploader(
        "Upload your report",
        type=("pdf"),
        accept_multiple_files=False)

    if uploaded_file is not None:
        user_input_text = getText(uploaded_file)

        file_path1 = "../pdf_files/assignment3/context3.pdf"
        file_path3 = "../pdf_files/assignment3/description3.pdf"
        file_path4 = "../pdf_files/assignment3/sample_evaluation3.pdf"
        file_path5 = "../pdf_files/assignment3/sample_input3.pdf"

        context_pdf_text = read_pdf(file_path1)
        description_text = read_pdf(file_path3)
        sample_evaluation_text = read_pdf(file_path4)
        sample_input_text = read_pdf(file_path5)

        input_variables = [
            "description",
            "great_submission",
            "sample_input",
            "sample_evaluation",
            "user_input"]
        prompt = get_prompt(TEMPLATE_3, input_variables)

        response = get_model_response(
            prompt,
            description_text,
            context_pdf_text,
            sample_input_text,
            sample_evaluation_text,
            user_input_text
        )

        st.markdown("###### AI Feedback")

        st.info(response.content)
    else:
        st.info("Upload file to continue")
