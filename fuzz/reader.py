#!/usr/bin/python3

import sys

import atheris
import nestedtext as nt

def TestOneInput(data):
    content = data.decode("ascii", errors="ignore")
    try:
        nt.loads(content, top="dict")
    except nt.NestedTextError:
        pass

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
