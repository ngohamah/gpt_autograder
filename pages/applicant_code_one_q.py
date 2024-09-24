import time

import tkinter as tk
from tkinter import filedialog
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate



from constants import TEMPLATE_INTRO_TASK
from helpers import get_prompt, getText, read_pdf, read_folder_content, create_retriever

def select_folder():
   root = tk.Tk()
   root.withdraw()
   folder_path = filedialog.askdirectory(master=root)
   root.destroy()
   return folder_path

def get_model_response(
        prompt_template,
        description_text,
        good_submission_text,
        context_pdf_text,
        sample_evaluation_text,
        user_input_text,
):

    # llm = ChatOpenAI(model="gpt-4o")
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    llm_chain = prompt_template | llm

    response = llm_chain.invoke({"description": description_text,
                                 "great_submission": good_submission_text,
                                #  "sample_input": context_pdf_text,
                                #  "sample_evaluation": sample_evaluation_text,
                                 "user_input": user_input_text})
    # response = llm_chain.invoke({"description": description_text,
    #                         # "great_submission": good_submission_text,
    #                         # "sample_input": context_pdf_text,
    #                         # "sample_evaluation": sample_evaluation_text,
    #                         "user_input": user_input_text})
    return response


def page_new():
    st.title("Applicant code")

    # uploaded_file = st.file_uploader(
    #     "Upload your report",
    #     type=("pdf"),
    #     accept_multiple_files=False)
    selected_folder_path = st.session_state.get("folder_path", None)
    folder_select_button = st.button("Select Folder")
    if folder_select_button:
        selected_folder_path = select_folder()
        st.session_state.folder_path = selected_folder_path
    if selected_folder_path:
        start = time.perf_counter()
        st.write("Selected folder path:", selected_folder_path)
        input_code = read_folder_content(selected_folder_path)
        bad_code_path = r"C:\Users\Administrator\Documents\test_code\eyerusalem_bad"
        good_code_path = r"C:\Users\Administrator\Documents\test_code\New folder\Algo-Science-Assessment"
        bad_code_review_path = r"C:\Users\Administrator\Documents\test_code\eyerusalem_response\eyerusalem_bad_review.pdf"
        question_path = r"C:\Users\Administrator\Documents\test_code\question\intro_task.pdf"
        bad_code = read_folder_content(bad_code_path)
        good_code = read_folder_content(good_code_path)
        bad_code_review = read_pdf(bad_code_review_path)
        question = read_pdf(question_path)
        total = (time.perf_counter() - start) * 1000
        print(f"Total time used for parsing files= {total}ms")
        input_variables = [
            "description",
            "great_submission",
            # "sample_input",
            # "sample_evaluation",
            "user_input"]
        prompt = get_prompt(TEMPLATE_INTRO_TASK, input_variables)

        response = get_model_response(
            prompt,
            question,
            good_code,
            bad_code,
            bad_code_review,
            input_code
        )

        st.markdown("###### AI Feedback")

        st.info(response.content)

        # retriever = create_retriever(code)
        print(f"{type(input_code)=}")
        print(f"{type(bad_code_review)=}")
        st.write(f"{type(bad_code_review)=}")
        st.write(f"{bad_code_review=}")
        st.write(f"{type(input_code)=}")
        st.write(str(input_code))
    else:
        st.info("Upload file to continue")

    # if uploaded_file is not None:
    #     user_input_text = getText(uploaded_file)

    #     file_path1 = "pdf_files/assignment6/context.pdf"
    #     file_path3 = "pdf_files/assignment6/description.pdf"
    #     file_path4 = "pdf_files/assignment6/sample_evaluation.pdf"
    #     file_path5 = "pdf_files/assignment6/sample_input.pdf"

    #     context_pdf_text = read_pdf(file_path1)
    #     description_text = read_pdf(file_path3)
    #     sample_evaluation_text = read_pdf(file_path4)
    #     sample_input_text = read_pdf(file_path5)

    #     input_variables = [
    #         "description",
    #         "great_submission",
    #         "sample_input",
    #         "sample_evaluation",
    #         "user_input"]
    #     prompt = get_prompt(TEMPLATE_6, input_variables)

    #     response = get_model_response(
    #         prompt,
    #         description_text,
    #         context_pdf_text,
    #         sample_input_text,
    #         sample_evaluation_text,
    #         user_input_text
    #     )

    #     st.markdown("###### AI Feedback")

    #     st.info(response.content)
    # else:
    #     st.info("Upload file to continue")
