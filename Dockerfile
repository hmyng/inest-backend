FROM python:3.9

WORKDIR /src

COPY /src/requirements.txt /src/requirements.txt

RUN pip install -r requirements.txt

COPY src/app /src/app

CMD ["python", "/src/app/main.py"]