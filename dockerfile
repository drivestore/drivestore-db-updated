FROM postgres:13
RUN apt update  
RUN apt-get install  software-properties-common python3.6 python3-pip -y
RUN pip3 install -U Flask

WORKDIR /app
COPY ./src/app.py app.py
ADD runner.sh /docker-entrypoint-initdb.d/

EXPOSE 8080
EXPOSE 5432


