FROM v131v/sd-deps

WORKDIR /workspace

COPY . ./upscalers

RUN pip install -r ./upscalers/requirements.txt

CMD [ "python3", "./upscalers/main.py" ]
