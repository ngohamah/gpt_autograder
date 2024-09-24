import glob
import os
from io import BufferedReader
import tkinter as tk
from tkinter import filedialog
from typing import List, Union

import PyPDF2
from langchain.docstore.document import Document
from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
    UnstructuredFileLoader,
)
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_community.document_loaders.parsers.pdf import PyPDFParser
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

from constants import OPENAI_API_KEY

# set environment variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


def getText(file: Union[BufferedReader, str]) -> str:
    reader = PyPDF2.PdfReader(file)
    text = ""

    number_of_pages = reader.pages

    # iterate over each page in the pdf file and extract the text
    for page_num in range(len(number_of_pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

    return text


def read_pdf(file_path: str) -> str:
    """
    Reads all pages of a pdf file and returns it as a single string.
    
    Args:
        file_path (str): path to the pdf file.

    Returns:
        (str): A string containing the contents of the pdf file.
    """
    with open(file_path, "rb") as file:
        return getText(file)


def read_python_code(folder_path: str) -> List[Document]:
    """
    Finds all python code in a folder recursively, reads them, splits
    them into smaller chunks and returns them as a list of Documents.

    Args:
        folder_path (str): absolute path to a folder containing
            python files.

    Returns:
        List[Documents]: A list of Documents.
    """
    loader = GenericLoader.from_filesystem(
        folder_path,
        glob="**/[!.]*",
        suffixes=[".py"],
        parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
    )
    documents = loader.load()
    len(documents)
    return split_python_code(documents)


def read_other_files(folder_path: str) -> List[Document]:
    """
    Reads cfg files, requirements files etc and returns them as a list
    of documents.

    Args:
        folder_path (str): absolute path to the folder.

    Returns:
        (List[Document]): a list of documents containing the contents of
            the files.
    """
    results: List[Document] = []
    text_globs = (
        "**/[!.]*.cfg",
        "**/[!.]*.conf",
        "**/[!.]*.config",
        "**/[!.]*.ini",
        "**/[!.]*.service",
        "**/[!.]*.sh",
        "**/[!][Dd][Oo][Cc][Kk][Ee][Rr][Ff][Ii][Ll][Ee]",
        "**/[!.][Rr][Ee][Qq][Uu][Ii][Rr][Ee][Mm][Ee][Nn][Tt][Ss].txt",
    )
    word_files = ("**/[!.]*.docx", "**/[!.]*.docs")
    # img_files = (
    #     "**/[!.]*.bmp",
    #     "**/[!.]*.heic",
    #     "**/[!.]*.jpeg",
    #     "**/[!.]*.png",
    #     "**/[!.]*.tiff",
    # )
    file_loaders = {
        text_globs: TextLoader,
        word_files: UnstructuredFileLoader,
        # img_files: UnstructuredImageLoader,
    }
    for pattern, loader in file_loaders.items():
        loader = DirectoryLoader(
            folder_path, glob=pattern, loader_cls=loader, silent_errors=True
        )
        docs = loader.load()
        if docs:
            results.extend(docs)

    # print(f"read_extra_files = {results=}")
    return results


def split_python_code(documents: List[Document]) -> List[Document]:
    """
    Splits python code into smaller chunks while keeping record of the
    order.

    Args:
        documents (List[Document]): A list of Documents containing
            python code.

    Returns:
        List[Document]: A list containing python code that has been
            divided into smaller chunks.
    """
    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
    )
    return python_splitter.split_documents(documents)


def read_markdown(folder_path: str) -> List[Document]:
    """
    Searches a folder recursively, finds markdown files and returns
    them as a list of Documents.

    Args:
        folder_path (str): absolute path to a folder.

    Returns:
        List[Documents]: It returns a list of Documents containing the
            contents of the md files.
    """
    results = []
    md_files = glob.glob(folder_path + "**/*.md", recursive=True)
    for file in md_files:
        loader = UnstructuredMarkdownLoader(
            file,
            mode="elements",
            strategy="fast",
        )
        md_content = loader.load()
        results.extend(md_content)
    return results


def read_pdf_files(folder_path: str) -> List[Document]:
    """
    Searches a folder recursively, finds pdf files and returns them as
    a list of Documents.

    Args:
        folder_path (str): absolute path to a folder.

    Returns:
        List[Documents]: It returns a list of Documents containing the
            contents of the pdf files.
    """
    loader = GenericLoader.from_filesystem(
        path=folder_path,
        glob="**/[!.]*",
        suffixes=[".pdf"],
        parser=PyPDFParser(extract_images=True),
    )
    pdf_docs = loader.load()
    return pdf_docs


def read_folder_content(folder_path: str) -> List[Document]:
    """
    Reads the contents of a folder, extracting all python code, PDFs
    and markdown files.

    Args:
        folder_path (str): absolute path to the folder.

    Returns:
        (List[Document]): It returns a list of Documents.
    """
    result: List[Document] = []
    code = read_python_code(folder_path)
    if code:
        result.extend(code)
    pdfs = read_pdf_files(folder_path)
    if pdfs:
        result.extend(pdfs)
    mds = read_markdown(folder_path)
    if mds:
        result.extend(mds)
    other = read_other_files(folder_path)
    if other:
        result.extend(other)
    return result


def read_text_file_as_list(file_path: str) -> List[str]:
    """
    Opens a text file and returns its contents as a list with each
    element representing a line in the file.

    Args:
        file_path (str): path to a file.

    Returns:
        (List[str]): A list containing each line in the file as an
            element.
    """
    res = []
    with open(file_path, "r") as curr_file:
        res = curr_file.readlines()
    return res


def select_folder() -> str:
    """
    Opens a dialog box that allows you to select a folder.

    Returns:
        (str): A string containing the absolute path to the selected
            folder.
    """
    root = tk.Tk()
    # root.withdraw()
    # Hide the window
    root.attributes("-alpha", 0.0)
    # Always have it on top
    root.attributes("-topmost", True)
    folder_path = filedialog.askdirectory(master=root)
    root.destroy()
    return folder_path


def get_prompt(temp: str, input_variables: List[str]) -> PromptTemplate:
    """
    Creates and returns a prompt template.
    
    Args:
        temp(str): A prompt which has variables enclosed in curly
            brackets.
        input_variables (List[str]): A list containing the variables
            that were used in the temp string.

    Returns:
        (PromptTemplate): Returns a prompt template.
    """
    prompt_template = PromptTemplate(
        template=temp, input_variables=input_variables
    )

    return prompt_template
