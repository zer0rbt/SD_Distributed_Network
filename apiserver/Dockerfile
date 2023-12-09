FROM python

WORKDIR /workspace/

COPY . ./apiserver

RUN pip install -r ./apiserver/requirements.txt

CMD [ "python3", "./apiserver/main.py" ]