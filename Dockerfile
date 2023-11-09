FROM python:3.10-slim-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

USER 1000

COPY code .

ENTRYPOINT [ "python3", "/code/raw_extract.py" ]
