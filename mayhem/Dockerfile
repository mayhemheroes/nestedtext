FROM fuzzers/atheris:2.0.7-python3.9

RUN pip install ..
COPY fuzz/reader.py /reader.py

# Set to fuzz!
ENTRYPOINT []
CMD ["/reader.py"]
