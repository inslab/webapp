FROM ubuntu:14.04
MAINTAINER Docker Education Team <education@docker.com>
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-all python-pip
RUN apt-get install -y python-dev
RUN apt-get install -y nginx
ADD ./webapp/requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
ADD ./webapp/nginx-conf /tmp/nginx-conf
ADD ./webapp/nginx-main /tmp/nginx-main
RUN mv /tmp/nginx-conf /etc/nginx/sites-available/default && mv /tmp/nginx-main /etc/nginx/nginx.conf && service nginx restart
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 5000
CMD ["gunicorn", "app:app", "-w", "4", "-b", ":5000", "-k", "gevent", "--worker-connections", "10000"]
