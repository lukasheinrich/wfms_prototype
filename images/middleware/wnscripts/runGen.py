import sys
import os

def preprocess(template,output,fmapping):
    with open(template,'r') as templ:
        with open(output,'w') as out:
            t = templ.read()
            t = t.replace('%IN',fmapping['IN'])
            t = t.replace('%OUT',fmapping['OUT'])
            out.write(t)
    os.chmod(output, 0o755)


def postprocess():
    print('runGen.py post processing...')