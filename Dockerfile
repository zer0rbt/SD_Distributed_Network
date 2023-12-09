FROM python:3.8.5

RUN python -m pip install --upgrade pip

RUN pip install flask
RUN pip install pika
RUN pip install python-dotenv
RUN pip install Pillow
RUN pip install jsonschema
RUN pip install pymongo
RUN pip install typing
RUN pip install asyncio
RUN pip install requests
RUN pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu116
RUN pip install sdkit


WORKDIR /workspace

COPY ./utils ./utils
COPY ./schemas ./schemas
