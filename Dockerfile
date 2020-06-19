FROM frolvlad/alpine-python3

WORKDIR /app

ADD . ./

RUN pip install -r requirements.txt

EXPOSE 8889

CMD python exporter.py