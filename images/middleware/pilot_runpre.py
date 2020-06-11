from wnscripts import runGen
from pilot import data

data.stage_in(
    source = 'http://some/file.root',
    target = '/data/input.root'
)

runGen.preprocess(
    template = '/wlcg/payload.templ.sh',
    output = '/data/_payload.sh',
    fmapping = {
        'IN': '/data/input.root',
        'OUT': '/data/output.root'
    }
)