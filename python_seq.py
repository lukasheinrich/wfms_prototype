import multiprocessing
import subprocess
import time
import os
import json
import sys

def call(argv):
    return subprocess.check_call(argv)

spec = json.load(open(sys.argv[1]))
workdir = os.path.abspath('work_'+str(int(time.time())))
cmapdir = os.path.abspath('configmap')
os.makedirs(workdir)

pool = multiprocessing.Pool(processes=4)
pool.map(
    call,
    [
        ['docker','run','--pid=host','--rm','-v',f'{workdir}:/data','-v',f'{cmapdir}:/wlcg', spec['step1']['image'],'sh','-c','LOGFILE=/data/step1.log PIDFILE=/data/step1.pid WAITFORFILE=/data/_wlcg_done_0.txt TOMBSTTONEFILE=/data/_wlcg_done_1.txt /wlcg/wrapper.sh /wlcg/step1.sh'],
        ['docker','run','--pid=host','--rm','-v',f'{workdir}:/data','-v',f'{cmapdir}:/wlcg', spec['step2']['image'],'sh','-c','LOGFILE=/data/step2.log PIDFILE=/data/step2.pid WAITFORFILE=/data/_wlcg_done_1.txt TOMBSTTONEFILE=/data/_wlcg_done_2.txt /wlcg/wrapper.sh /wlcg/step2.sh'],
        ['docker','run','--pid=host','--rm','-v',f'{workdir}:/data','-v',f'{cmapdir}:/wlcg', spec['step3']['image'],'sh','-c','LOGFILE=/data/step3.log PIDFILE=/data/step3.pid WAITFORFILE=/data/_wlcg_done_2.txt TOMBSTTONEFILE=/data/_wlcg_done_3.txt /wlcg/wrapper.sh /wlcg/step3.sh'],
        ['docker','run','--pid=host','--rm','-v',f'{workdir}:/data','-v',f'{cmapdir}:/wlcg', spec['sidecar']['image'],'sh','-c','/wlcg/sidecar.sh 2>&1 | tee /data/sidecar.log'],
    ]
)
pool.close()
pool.join()
