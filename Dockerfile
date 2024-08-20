FROM python:3.9

RUN apt -qq update && apt -qq install -y git wget ffmpeg
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
RUN git clone link
WORKDIR /usr/src/app/NAMEOFREPO
RUN chmod 777 /usr/src/app/NAMEOFREPO


RUN pip3 install -r requirements.txt 
CMD ["bash","start.sh"]
