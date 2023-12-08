FROM v131v/sd-deps

WORKDIR /workspace

COPY . ./stablediffusion

RUN pip install -r ./stablediffusion/requirements.txt

CMD [ "python3", "./stablediffusion/main.py" ]
