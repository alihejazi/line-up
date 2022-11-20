FROM python:3.10-bullseye
RUN pip3 install fastapi uvicorn requests python-dotenv jsonpickle
COPY ./app /app
WORKDIR /app
RUN ls -la /app/*
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15400", "--reload" ]