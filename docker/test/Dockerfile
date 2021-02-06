FROM python:3.9

LABEL application="Temperature Query"

ENV PYTHONUNBUFFERED 1
RUN mkdir /application
WORKDIR /application
COPY . /application/
RUN pip install -r requirements.txt
COPY scripts/test.sh /test.sh
RUN sed -i 's/\r//' /test.sh \
    && chmod +x /test.sh

ENTRYPOINT [ "/test.sh" ]
