import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


from constants import TEMPLATE_6
from helpers import get_prompt, getText, read_pdf


def get_model_response(
        prompt_template,
        description_text,
        good_submission_text,
        context_pdf_text,
        sample_evaluation_text,
        user_input_text,
):

    llm = ChatOpenAI()
    llm_chain = prompt_template | llm

    response = llm_chain.invoke({"description": description_text,
                                 "great_submission": good_submission_text,
                                 "sample_input": context_pdf_text,
                                 "sample_evaluation": sample_evaluation_text,
                                 "user_input": user_input_text})
    return response


def page6():
    st.title("A6: Midterm Exam")

    uploaded_file = st.file_uploader(
        "Upload your report",
        type=("pdf"),
        accept_multiple_files=False)

    if uploaded_file is not None:
        user_input_text = getText(uploaded_file)

        file_path1 = "../pdf_files/assignment6/context.pdf"
        file_path3 = "../pdf_files/assignment6/description.pdf"
        file_path4 = "../pdf_files/assignment6/sample_evaluation.pdf"
        file_path5 = "../pdf_files/assignment6/sample_input.pdf"

        context_pdf_text = read_pdf(file_path1)
        description_text = read_pdf(file_path3)
        sample_evaluation_text = read_pdf(file_path4)
        sample_input_text = read_pdf(file_path5)

        try: 
            input_variables = [
                "description",
                "great_submission",
                "sample_input",
                "sample_evaluation",
                "user_input"]
            prompt = get_prompt(TEMPLATE_6, input_variables)

            response = get_model_response(
                prompt,
                description_text,
                context_pdf_text,
                sample_input_text,
                sample_evaluation_text,
                user_input_text
            )
        except Exception:
            raise
        
        st.markdown("###### AI Feedback")

        st.info(response.content)
    else:
        st.info("Upload file to continue")
