FROM python

WORKDIR /workspace/

COPY . ./database

RUN pip install -r ./database/requirements.txt

CMD [ "python3", "./database/main.py" ]