import streamlit as st
from langchain_openai import ChatOpenAI

from constants import TEMPLATE_7
from helpers import get_prompt, getText, read_pdf


def get_model_response(
        prompt_template,
        description_text,
        context_pdf_text,
        sample_evaluation_text,
        user_input_text,
):

    llm = ChatOpenAI()
    llm_chain = prompt_template | llm

    response = llm_chain.invoke({"description": description_text,
                                 "sample_input": context_pdf_text,
                                 "sample_evaluation": sample_evaluation_text,
                                 "user_input": user_input_text})
    return response


def page2():
    st.title("A7: Strategy Robustness")
    uploaded_file = st.file_uploader(
        "Upload your report",
        type=("pdf"),
        accept_multiple_files=False)

    if uploaded_file is not None:
        user_input_text = getText(uploaded_file)

        file_path1 = "pdf_files/assignment7/context.pdf"
        file_path3 = "pdf_files/assignment7/description.pdf"
        file_path4 = "pdf_files/assignment7/sample_evaluation.pdf"

        context_pdf_text = read_pdf(file_path1)
        description_text = read_pdf(file_path3)
        sample_evaluation_text = read_pdf(file_path4)

        input_variables = [
            "description",
            "sample_input",
            "sample_evaluation",
            "user_input"]
        prompt = get_prompt(TEMPLATE_7, input_variables)

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
