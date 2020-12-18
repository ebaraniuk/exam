FROM alpine:3.7
RUN apk add --update python3 py-pip
COPY . /exam
WORKDIR /exam
ENTRYPOINT ["python3"]
CMD ["test.py"]