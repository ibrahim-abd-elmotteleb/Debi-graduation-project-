Arabic Sentiment Analysis for Company Reviews
Overview
This project implements a sentiment analysis model to predict the sentiment (positive or negative) of Arabic company reviews, with a focus on platforms like Talabat. Using logistic regression, the model processes Arabic text to provide insights into customer opinions, helping businesses understand user feedback. The project leverages natural language processing (NLP) techniques tailored for Arabic, including morphological analysis and tokenization.

Features
Sentiment classification of Arabic reviews using logistic regression.

Preprocessing of Arabic text with tools like qalsadi for morphological analysis.

Support for analyzing reviews from platforms like Talabat.

A user-friendly web interface built with Flask and Streamlit, allowing users to input Arabic reviews and view sentiment analysis results in real-time.

Built with Python and popular NLP libraries for robust text processing.

Results
The logistic regression model achieves 85% accuracy on a test set on Arabic review sentiment classification. It effectively handles the complexities of Arabic text, such as morphology and dialect variations.

Requirements
python 3.9
Create new environment using the following command
$ conda create -n Arabic-sentiment python=3.9
Activate the environment
$ conda activate Arabic-sentiment
(Optional) Setup you command line interface for better readability
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$"
Installation
Install the required packages
$ pip install -r requirements.txt
Run
Run the flask server
$ python app.py
open another terminal in the same directory and Run the streamlit application
$ streamlit run UI.py
