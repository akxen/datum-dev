FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache mariadb-connector-c-dev
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers musl-dev build-base mariadb-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./project /app
WORKDIR /app
COPY ./scripts /scripts
COPY ./config /config

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
RUN chown -R user:user /app/api/migrations
USER user

CMD ["/scripts/entrypoint.sh"]