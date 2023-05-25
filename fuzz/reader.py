#!/usr/bin/python3

import sys

import atheris
import nestedtext as nt

def TestOneInput(data):
    content = data.decode("utf-8", errors="ignore")
    try:
        nt.loads(content)
    except nt.NestedTextError:
        pass

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
