#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dockerfile
FROM python:3.10.7-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

