from wnscripts import runGen
from pilot import data

runGen.postprocess()

data.stage_out(
    source = '/data/output.root',
    target = 'http://some/output.root',
)
