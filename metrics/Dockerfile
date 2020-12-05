FROM python:3.8

WORKDIR .

COPY metrics.py ./
COPY requirements.txt ./
ADD keys ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD [ "python", "./metrics.py" ]