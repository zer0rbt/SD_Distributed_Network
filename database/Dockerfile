FROM python

WORKDIR /workspace/

COPY . ./database

RUN apt-get -y update
RUN apt -y install python3-pip
RUN pip3 install -r ./database/requirements.txt

CMD [ "python3", "./database/db_app.py" ]