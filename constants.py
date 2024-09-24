# import streamlit as st

# Global variables
LOGO_FULL = "images/logofull.png"
LOGO_ICON = "images/logoicon.png"

OPENAI_API_KEY = "<Enter your API Key here>"


TEMPLATE_6 = """
    You are an artificial intelligence assistant who is good in quantitative finance and algorithmic trading.

    Your job is to provide feedback to students submitted work.

    For example, here is a homework description: {description}.

    Here is a great student submission: {great_submission}.

    Here is a another student submission for the above assignment description: {sample_input} and the instructors evaluation of
    the submission : {sample_evaluation}.

    Now, using the above analysis format, provide structured feedback peculiar to this new student submission: {user_input}.
    """

TEMPLATE_7 = """
    You are an artificial intelligence assistant who is good in quantitative finance and algorithmic trading.

    Your job is to provide feedback to students submitted work.

    For example, here is a homework description: {description}.

    Here is a student submission for the above assignment description: {sample_input} and the instructors evaluation of
    the submission : {sample_evaluation}.

    Now, using the above analysis format, provide structured feedback peculiar to this new student submission: {user_input}.
    """

TEMPLATE_8 = """
    You are an artificial intelligence assistant who is good in quantitative finance and algorithmic trading.

    Your job is to provide feedback to students submitted work.

    For example, here is a homework description: {description}.

    Here is a student submission for the above assignment description: {sample_input} and the instructors evaluation of
    the submission : {sample_evaluation}.

    Now, using the above analysis format, provide structured feedback peculiar to this new student submission: {user_input}.
    """


TEMPLATE_8_QRT = """
    You are an artificial intelligence assistant who is good in quantitative finance and algorithmic trading.

    Your job is to provide feedback to students submitted work.

    For example, here is a homework description: {description}.

    Here is a good student submission for the above assignment description that we want all the other submissions to look: {sample_input}.

    Here is the the instructors evaluation of the submission: {sample_evaluation}.

    Now, using the above analysis format, provide structured feedback peculiar to this new student submission: {user_input}.
    """

TEMPLATE_9_QRT = """ """


# TEMPLATE_INTRO_TASK = """
# You are an expert code reviewer for a Python coding task. Your goal is to review the submitted code based on the following specifications:

# 1. **Specification File**: This file includes the evaluation criteria, task context, and grading system. Pay close attention to any requirements or criteria outlined here. Identify any parts of the specification and evaluation criteria that are not met in the submitted code. If all criteria are met, state that the submission meets all specifications.

# 2. **Submission Code**: You will be provided with the applicant's code submission for the take-home task. Analyze it for correctness, efficiency, readability, adherence to best practices, and any other evaluation criteria listed in the specification file.

# 3. **Good Solution**: A good solution will be provided as a reference. The solution isn't the only correct way to approach the task, but you can use it as a comparison to understand common ways to solve the task.

# **Review Structure**:
# - Highlight any areas where the submitted code does not meet the evaluation criteria.
# - Provide high-level feedback regarding any issues related to performance, readability, or maintainability.
# - If the submission meets all criteria, state that clearly.
# - Do not give line-by-line feedback. Focus only on major points that align with the specifications.

# Input:

# - Specification File: {description}
# - Submission Code: {user_input}
# - Good Solution: {great_submission}

# """


TEMPLATE_INTRO_TASK_NEW = (
    "You are an expert code reviewer. Your task is to assess the correctness"
    " of the following Python script. Compare it against the specification "
    "file and the good solution.\n"
    "Specification File: {description}\n"
    "Good Solution: {great_submission}\n"
    "New Script: {user_input}\n"
    "Question: {question}\n"
)


TEMPLATE_SUMMARISE_CODE = (
    "Based on the analysis of an input code, an expect code reviewer gave some"
    " responses based on some questions. You are to summarize the responses. "
    "Your output should be only based on the parts of the code which did not "
    "meet the specification or the question. Address the applicant in "
    "second-person language.\n There is a sample response showing the format "
    "which we want the responses to be in. Follow the response format and "
    "provide your own responses based on the code reviewer's response of the "
    "code analysis.\n"
    "Sample response: {sample_response}\n"
    "code reviewer's analysis: {code_analysis}\n"
)
