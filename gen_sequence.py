import sys
import json
import textwrap
import os
import string
import json

spec = json.load(open('jobspec.json'))
with open('configmap/payload.templ.sh','w') as paylad_f:
    paylad_f.write(spec['step2']['template'])
os.chmod('configmap/payload.templ.sh', 0o755)

for templ in ['kubeseq.yml.tmpl','shellseq_docker.sh.tmpl','shellseq_sing.sh.tmpl']:
    outname = templ.replace('.tmpl','')
    with open(templ,'r') as templ:
        with open(outname,'w') as out:
            r = string.Template(templ.read()).safe_substitute(
                stagein_image = spec['step1']['image'],
                payload_image = spec['step2']['image'],
                stageout_image = spec['step3']['image'],
                sidecar_image =  spec['sidecar']['image'],
            )
            out.write(r)
    if outname.endswith('.sh'):
        os.chmod(outname, 0o755)
