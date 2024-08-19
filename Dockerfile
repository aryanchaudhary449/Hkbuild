FROM admin44449999/aryanmadeallworking:latest

RUN apt -qq update && apt -qq install -y git wget ffmpeg
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . . 

RUN pip3 install -r requirements.txt 

CMD ["bash","start.sh"]
