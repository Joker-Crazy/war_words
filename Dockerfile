FROM debian:stable-slim

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install python3 python3-setuptools python3-pip

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
# ADD . /project
RUN mkdir /project
WORKDIR /project


CMD ["python3", "src/main.py"]
#echo $(curl -X GET https://docs.google.com/spreadsheets/d/1SR5-7gx23mAYxNfN1IrmThh0VqQZfICeAYnSYXorg_M/export?format=csv&id=1SR5-7gx23mAYxNfN1IrmThh0VqQZfICeAYnSYXorg_M&gid=852582718) > ukrainian_military_losses.csv
