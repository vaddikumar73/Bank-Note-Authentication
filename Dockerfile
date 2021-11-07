FROM continuumio/anaconda3:2020.07
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip3 install -r requirements.txt
CMD python flasgger_api.py
