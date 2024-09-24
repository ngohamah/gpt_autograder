import os
from typing import Any, Dict, List, Tuple

import streamlit as st
from helpers import (get_prompt, read_folder_content, read_pdf,
                     read_text_file_as_list, select_folder)
from langchain.docstore.document import Document
from langchain_core.messages.base import BaseMessage
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from constants import TEMPLATE_INTRO_TASK, TEMPLATE_SUMMARISE_CODE


@st.cache_data
def read_data_for_query() -> Tuple[str, List[Document], List[str], str]:
    """
    Reads the folders and files containing the specification file, a
    good version of the code and the questions which will be used in
    the query and returns them.

    Returns:
        (Tuple[str, List[Document], List[str]]): A tuple containing the
            specification document, a good sample code for the task and
            the list of questions that the LLM will be asked.
    """
    main_folder = os.path.dirname(os.path.dirname(__file__))
    sample_files_folder = os.path.join(
        main_folder, "pdf_files", "applicant_code"
    )
    good_code_path = os.path.join(sample_files_folder, "good_code")
    specs_path = os.path.join(
        sample_files_folder, "specification", "intro_task.pdf"
    )
    questions_path = os.path.join(
        sample_files_folder, "questions", "intro_questions.txt"
    )
    sample_response_path = os.path.join(
        sample_files_folder, "sample_response", "sample_response.pdf"
    )

    good_code = read_folder_content(good_code_path)
    specs = read_pdf(specs_path)
    questions = read_text_file_as_list(questions_path)
    sample_response = read_pdf(sample_response_path)
    return specs, good_code, questions, sample_response


def get_model_response(
    prompt_template: PromptTemplate,
    query_data: Dict[str, Any],
) -> BaseMessage:
    """
    Queries the LLM using the prompt template and query data and
    returns the response.

    Args:
        prompt_template (PromptTemplate): A prompt template.
        query_data (Dict[str, Any]): A dictionary containing the names
            of the variables expected by the prompt template as keys
            and the actual values of the variables as values of the
            dictionary.

    Returns:
        (BaseMessage): It returns the response from the LLM as a
            BaseMessage.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    llm_chain = prompt_template | llm

    response = llm_chain.invoke(query_data)

    return response


def analyse_code_with_llm(
    prompt: PromptTemplate,
    specs: str,
    good_code: List[Document],
    questions: List[str],
    input_code: List[Document],
    verbose: bool = True,
) -> List[str]:
    """
    Goes through the list of questions and for each question, adds the
    necessary context to the prompt and returns a list containing the
    questions and the response.

    Args:
        prompt (PromptTemplate): The prompt template.
        specs (str): The contents of the specification file.
        good_code (List[Document]): The list of documents containing a
            code base that meets specification.
        questions (List[str]): A list of questions that will be used in
            queries to the LLM.
        input_code (List[Document]): The current code that is being
            evaluated.
        verbose (bool): If true, each response from the LLM is shown on
            the webpage.

    Returns:
        (List[str]): A list of questions and the response from the LLM.
    """
    code_analysis: List[str] = []
    progress_text = "Analysing code..."
    my_bar = st.progress(0.0, text=progress_text)
    total = len(questions)

    query_data = {
        "description": specs,
        "great_submission": good_code,
        "user_input": input_code,
    }

    for idx, question in enumerate(questions):
        if not question:
            pass
        query_data["question"] = question

        response = get_model_response(prompt, query_data)
        data = f"Q{idx+1}. {question}\n {response.content}\n\n"
        if verbose:
            st.info(data)
        code_analysis.append(data)
        fraction = (idx + 1) / total
        progress = f"{idx+1}/{total} checks complete..."
        my_bar.progress(fraction, text=progress)

    return code_analysis


def code_review_page():
    """
    Function for the contents of the code review page.
    """
    st.title("Introductory Task Auto Reviewer")
    selected_folder_path = st.session_state.get("folder_path", None)
    verbose = st.toggle("Verbose response", value=True)

    folder_select_button = st.button("Select Folder")
    if folder_select_button:
        selected_folder_path = select_folder()
        st.session_state.folder_path = selected_folder_path
    if selected_folder_path and folder_select_button:
        st.write("Selected folder path:", selected_folder_path)
        input_code = read_folder_content(selected_folder_path)
        specs, good_code, questions, sample_response = read_data_for_query()
        input_variables = [
            "description",
            "great_submission",
            "user_input",
            "question",
        ]
        prompt = get_prompt(TEMPLATE_INTRO_TASK, input_variables)

        st.markdown("###### AI Feedback")

        code_analysis = analyse_code_with_llm(
            prompt, specs, good_code, questions, input_code, verbose
        )
        input_variables_2 = ["sample_response", "code_analysis"]
        prompt = get_prompt(TEMPLATE_SUMMARISE_CODE, input_variables_2)
        query_data = {
            "sample_response": sample_response,
            "code_analysis": code_analysis,
        }
        response = get_model_response(prompt, query_data)
        st.info(f"SUMMARY\n\n{response.content}")

    else:
        st.info("Select a folder to continue")
