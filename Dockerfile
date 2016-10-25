FROM python:latest

RUN apk -U add \
    perl \
    make \
    && apk -U add --virtual deps \
    py-pip \
    && pip install pelican markdown \
    && apk del deps \
    && rm -rf /var/cache/apk/*


COPY start.sh start.sh
RUN chmod +x start.sh
EXPOSE 9000

#CMD ["/bin/sh", "start.sh"]
