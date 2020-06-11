import sys
import json
import textwrap
import os
import string


spec = {
    'step1': {
        'image': 'middlewareimage',
    },
    'step2': {
        'image': 'payloadimage',
        'template': textwrap.dedent('''\
            #/bin/sh
            python /code/fancyscript.py %IN %OUT
        '''),
    },
    'step3': {
        'image': 'middlewareimage',
    },
    'sidecar': {
        'image': 'middlewareimage',
    },
}

with open('configmap/payload.templ.sh','w') as paylad_f:
    paylad_f.write(spec['step2']['template'])
os.chmod('configmap/payload.templ.sh', 0o755)

with open('kubeseq.yml.tmpl','r') as templ:
    with open('kubeseq.yml','w') as out:
        r = string.Template(templ.read()).safe_substitute(
            stagein_image = spec['step1']['image'],
            payload_image = spec['step2']['image'],
            stageout_image = spec['step3']['image'],
            sidecar_image =  spec['sidecar']['image'],
        )
        out.write(r)

with open('shellseq.sh.tmpl','r') as templ:
    with open('shellseq.sh','w') as out:
        r = string.Template(templ.read()).safe_substitute(
            stagein_image = spec['step1']['image'],
            payload_image = spec['step2']['image'],
            stageout_image = spec['step3']['image'],
            sidecar_image =  spec['sidecar']['image'],
        )
        out.write(r)
os.chmod('shellseq.sh', 0o755)
