#!/usr/bin/python3

import sys

import atheris

with atheris.instrument_imports():
    import nestedtext as nt

def TestOneInput(data):
    content = data.decode("utf-8", errors="ignore")
    try:
        nt.loads(content, top="dict")
    except nt.NestedTextError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
