FROM ponylang/rfc-tool:release AS rfc-tool
FROM alpine

COPY --from=rfc-tool /usr/local/bin/rfc-tool /usr/local/bin/rfc-tool

COPY entrypoint.py /entrypoint.py

RUN apk add --update \
  git \
  py3-pip

RUN pip3 install gitpython PyGithub

ENTRYPOINT ["/entrypoint.py"]
