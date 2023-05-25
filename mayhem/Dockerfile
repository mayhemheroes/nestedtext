FROM fuzzers/atheris:2.0.7-python3.9

ADD . /project
WORKDIR /project

RUN pip install .
COPY fuzz/reader.py /reader.py
RUN chmod +x /reader.py

# Set to fuzz!
ENTRYPOINT []
CMD ["/reader.py"]
