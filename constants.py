import streamlit as st

# Global variables
LOGO_FULL = "images/logofull.png"
LOGO_ICON = "images/logoicon.png"

OPENAI_API_KEY = "insert your api key here"

TEMPLATE_3 = """
    You are an artificial intelligence assistant who is good in quantitative finance and algorithmic trading.

    Your job is to provide feedback to students submitted work.

    For example, here is a homework description: {description}.

    Here is a great student submission: {great_submission}.

    Here is a student submission for the above assignment description: {sample_input} and the instructors evaluation of
    the submission : {sample_evaluation}.

    Now, using the above analysis format, provide structured feedback peculiar to this new student submission: {user_input}.
    """

TEMPLATE_4 = """
    You are an artificial intelligence assistant who is good in quantitative finance and algorithmic trading.

    Your job is to provide feedback to students submitted work.

    For example, here is a homework description: {description}.

    Here is a great student submission: {great_submission}.

    Here is a student submission for the above assignment description: {sample_input} and the instructors evaluation of
    the submission : {sample_evaluation}.

    Now, using the above analysis format, provide structured feedback peculiar to this new student submission: {user_input}.
    """

TEMPLATE_5 ="""
    You are an artificial intelligence assistant who is good in quantitative finance and algorithmic trading.

    Your job is to provide feedback to students submitted work.

    For example, here is a homework description: {description}.

    Here is a student submission for the above assignment description: {sample_input} and the instructors evaluation of
    the submission : {sample_evaluation}.

    Now, using the above analysis format, provide structured feedback peculiar to this new student submission: {user_input}.
    """

TEMPLATE_6 = """
    You are an artificial intelligence assistant who is good in quantitative finance and algorithmic trading.

    Your job is to provide feedback to students submitted work.

    For example, here is a homework description: {description}.

    Here is a great student submission: {great_submission}.

    Here is another student submission for the above assignment description: {sample_input} and the instructors evaluation of
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
