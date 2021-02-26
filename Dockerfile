FROM python:3.9.2-alpine3.13

ENV PATH="/scripts:${PATH}"

#COPY ./requirements.txt /requirements.txt
RUN pip install pipenv
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers build-base 
RUN apk add openssl openssl-dev python3-dev gmp-dev postgresql-dev sqlite-dev
#RUN pip install -r /requirements.txt
#RUN apk del .tmp
WORKDIR /usr/src
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile
RUN pip install bitcoinlib
RUN mkdir /app
#Change "./app" for your project name
COPY ./cetacoin /app
WORKDIR /app
RUN python manage.py makemigrations
RUN python manage.py migrate
COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]