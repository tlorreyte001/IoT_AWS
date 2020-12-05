FROM python:3.8

WORKDIR .

COPY devices.py ./
COPY requirements.txt ./
ADD keys ./

RUN pip install --no-cache-dir -r requirements.txt

#CMD [ "ls" ]
CMD [ "python", "./devices.py" ]