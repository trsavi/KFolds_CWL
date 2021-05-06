FROM python:3.9

WORKDIR /cwl

COPY ./ ./

RUN pip install -r requirements.txt

CMD ["cwltool", "scatterPython.cwl.yaml", "config.yaml"]
