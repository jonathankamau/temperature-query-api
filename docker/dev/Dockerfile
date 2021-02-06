FROM python:3.9

LABEL application="Temperature Query"

ENV PYTHONUNBUFFERED 1
RUN mkdir /application
WORKDIR /application
COPY . /application/
RUN pip install -r requirements.txt
COPY scripts/dev.sh /dev.sh
RUN sed -i 's/\r//' /dev.sh \
    && chmod +x /dev.sh

ENTRYPOINT [ "/dev.sh" ]
