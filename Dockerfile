FROM python:3-alpine

WORKDIR /testyapp

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "80" ]
