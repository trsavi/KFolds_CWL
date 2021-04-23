FROM python:3.9

WORKDIR /cwl

COPY ./ ./

RUN pip install -r requirements.txt
RUN pip install cwltool

CMD ["cwltool", "scatterPython.cwl.yaml", "config.yaml"]
