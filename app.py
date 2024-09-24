import sys

import streamlit as st

from constants import LOGO_ICON, LOGO_FULL
sys.path.append("pages/")

from qrt_report2 import page5
from qrt_report1 import page4
from assignment8 import page3
from assignment7 import page2
from assignment6 import page1
from applicant_code import code_review_page
from tutorial import page0

st.set_page_config(page_title="IATACF", page_icon=LOGO_ICON)


# st.logo(LOGO_ICON)
st.image(LOGO_FULL)

pages = {
    "Autograding tool (Beta v0.1)": [
        st.Page(page0, title="How to use this tool")
    ],
    "General Submission": [
        st.Page(page1, title="A6: Midterm Exam"),
        st.Page(page2, title="A7: Strategy Robustness"),
        st.Page(page3, title="A8: Strategy Execution")
    ],
    "QRT Submission": [
        st.Page(page4, title="QRT Report 1 (SA)"),
        st.Page(page5, title="QRT Report 2 (MS)"),
    ],
    "Introductory task review": [
        st.Page(code_review_page, title="Introductory Task Review"),
    ]
}

pg = st.navigation(pages)

pg.run()
