#  Quantitative Financial Analytics and Algorithmic Trading (QFAAT) Autograder app

QFAAT Autograder app with Streamlit.

## Overview of the App

This app showcases one use case of LLM in serving as an autograder/autofeedback agent to students submissions.

Currently it provides feedbacks for the following submissions:

- Assignment 3: Initial Strategy Backtest
- Assignment 4: ISB & Adding Hyperparameters
- Assignment 5: Query and Backtest Currency Data
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

*TODO: Remove API key from development env.* 

## Run it locally

```sh
# activate your virtual environment
virtualenv .venv
source .venv/bin/activate

# clone repository
git clone github.com/ngohamah/gpt_autograder
cd gpt_autograder
pip3 install -r requirements.txt
pip install --upgrade streamlit

# run app
streamlit run app.py
```
## Demo 
![Sample Run](https://github.com/ngohamah/gpt_autograder/blob/main/images/demo.png)

## Some limitations of the app

- Only PDF file support.
- Limited model context size to generate wider context. We currently use gpt-3.5 Turbo. The higher the model  the better for more context window.
- Responses are not fixed, which is a feature of LLM models
- No memory, between user uploads or interactions
- #TODO Future feature to add will be an entry box on the UI for the user to include their API key which get's updated at the backend.Currently they need to go to constants.py file and change it manually before running/deployment.

## Possible solutions to some of the limitations

- Use a model which can ingest more data hence generate a wider context.  
- Using history and some langchain database stores such as chroma for saving interactions. However, this comes with storage cost especially if deployed in the cloud.