FROM v131v/sd-deps

WORKDIR /workspace

COPY . ./upscalers
#COPY ./.env ./upscalers

# RUN pip install -r ./upscalers/requirements.txt

CMD [ "python3", "./upscalers/main.py" ]
