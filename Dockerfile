FROM admin44449999/area:latest
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

CMD ["bash","start.sh"]
