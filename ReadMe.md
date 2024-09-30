#  Quantitative Financial Analytics and Algorithmic Trading (QFAAT) Autograder app

QFAAT Autograder app with Streamlit.

## Overview of the App

This app showcases one use case of LLM in serving as an autograder/autofeedback agent to students submissions.

Currently it provides feedbacks for the following submissions:

- Assignment 6: Midterm Exam
- Assignment 7: Strategy Robustness
- Assignment 8: Strategy Execution
- QRT Report 1: Stability Analysis Report

## Demo App

### Get an OpenAI API key

You can get your own OpenAI API key by following the following instructions:

1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.

## Run it locally

Before running app go to constants.py file and 
insert your OPENAI_API_KEY

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
## Sample output

![Sample LLM Output](images/gpt_autograder_output)

<img src="https://media.trekbikes.com/image/upload/f_auto,fl_progressive:semi,q_auto,w_1920,h_1440,c_pad/Procaliber95-25-47223-A-Portrait" alt="Mountain Bike" width="300" height="200">

## Some limitations of the app

- Only pdf support.
- Fewer files to generate wider context.
- Responses are not fixed, which is a feature of LLM models
- No memory, between user uploads or interactions
