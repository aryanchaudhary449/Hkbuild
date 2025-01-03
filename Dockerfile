FROM aryanchaudhary449/test:latest
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

CMD ["bash","start.sh"]
