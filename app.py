import sys
import streamlit as st

from constants import LOGO_ICON, LOGO_FULL

st.set_page_config(page_title="IATACF", page_icon=LOGO_ICON)


sys.path.append("pages/")

from qrt_report2 import page10
from qrt_report1 import page9
from assignment8 import page8
from assignment7 import page7
from assignment6 import page6
from assignment5 import page5
from assignment4 import page4
from assignment3 import page3
from tutorial import page0

# st.logo(LOGO_ICON)
st.image(LOGO_FULL)

pages = {
    "Autograding tool (Beta v0.1)": [
        st.Page(page0, title="How to use this tool")
    ],
    "General Submission": [
        st.Page(page3, title="A3: Initial Strategy Backtest"),
        st.Page(page4, title="A4: ISB & Adding Hyperparameters"),
        st.Page(page5, title="A5: Query & Backtest Currency Data"),
        st.Page(page6, title="A6: Midterm Exam"),
        st.Page(page7, title="A7: Strategy Robustness"),
        st.Page(page8, title="A8: Strategy Execution"),
    ],
    "QRT Submission": [
        st.Page(page9, title="QRT Report 1 (SA)"),
        st.Page(page10, title="QRT Report 2 (MS)"),
    ],
}

pg = st.navigation(pages)

pg.run()
