FROM python:latest

# Config and Setup
WORKDIR /pac

# Dependencies
COPY requirements.txt dev-requirements.txt setup.py /pac/
COPY nlpchain/ /pac/nlpchain/

RUN pip install --no-cache-dir -r requirements.txt -r dev-requirements.txt
