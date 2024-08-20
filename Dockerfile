FROM python:3.9

RUN apt -qq update && apt -qq install -y git wget ffmpeg
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
RUN git clone https://github.com/mahesh-kadali/testout4gb
WORKDIR /usr/src/app/testout4gb
RUN chmod 777 /usr/src/app/testout4gb


RUN pip3 install -r requirements.txt 
CMD ["bash","start.sh"]
