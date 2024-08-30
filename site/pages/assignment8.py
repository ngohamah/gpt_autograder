import streamlit as st

from constants import TEMPLATE_8
from helpers import get_prompt, getText, read_pdf
from assignment7 import get_model_response


def page3():
    st.title("A8: Strategy Execution")

    uploaded_file = st.file_uploader(
        "Upload your report",
        type=("pdf"),
        accept_multiple_files=False)

    if uploaded_file is not None:
        user_input_text = getText(uploaded_file)

        file_path1 = "../pdf_files/assignment8/context.pdf"
        file_path3 = "../pdf_files/assignment8/description.pdf"
        file_path4 = "../pdf_files/assignment8/sample_evaluation.pdf"

        context_pdf_text = read_pdf(file_path1)
        description_text = read_pdf(file_path3)
        sample_evaluation_text = read_pdf(file_path4)

        input_variables = [
            "description",
            "sample_input",
            "sample_evaluation",
            "user_input"]
        prompt = get_prompt(TEMPLATE_8, input_variables)

        response = get_model_response(
            prompt,
            description_text,
            context_pdf_text,
            sample_evaluation_text,
            user_input_text
        )

        st.markdown("###### AI Feedback")

        st.info(response.content)
    else:
        st.info("Upload file to continue")
