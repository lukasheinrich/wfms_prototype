# wfms_prototype

<img src="schema.png" height="300px"/>

(from slides at [link](https://indico.cern.ch/event/925900/contributions/3890902/attachments/2051032/3437998/container_follow_up.pdf) )

This is a prototype of runninng

* a sequence of containers [stage in, payload, stage out]
* a monitoring container (started before the first container, exiting after payload)

either as
* a standalone script with individual calls to a container runtime
* a pod in kubernetes


### Running without Kubernetes (think setupATLAS -c)

#### Docker
```
$> cat shellseq_docker.sh
#!/bin/sh

datadir="${PWD}/work_$(date '+%s')"
mkdir $datadir

docker run --pid=host --rm -v $datadir:/data -v $PWD/configmap:/wlcg lukasheinrich/middlewareimage  sh -c 'LOGFILE=/data/step1.log PIDFILE=/data/step1.pid WAITFORFILE=/data/_wlcg_done_0.txt TOMBSTTONEFILE=/data/_wlcg_done_1.txt /wlcg/wrapper.sh /wlcg/step1.sh'  &
docker run --pid=host --rm -v $datadir:/data -v $PWD/configmap:/wlcg lukasheinrich/payloadimage  sh -c 'LOGFILE=/data/step2.log PIDFILE=/data/step2.pid WAITFORFILE=/data/_wlcg_done_1.txt TOMBSTTONEFILE=/data/_wlcg_done_2.txt /wlcg/wrapper.sh /wlcg/step2.sh'  &
docker run --pid=host --rm -v $datadir:/data -v $PWD/configmap:/wlcg lukasheinrich/middlewareimage sh -c 'LOGFILE=/data/step3.log PIDFILE=/data/step3.pid WAITFORFILE=/data/_wlcg_done_2.txt TOMBSTTONEFILE=/data/_wlcg_done_3.txt /wlcg/wrapper.sh /wlcg/step3.sh'  &
docker run --pid=host --rm -v $datadir:/data -v $PWD/configmap:/wlcg lukasheinrich/middlewareimage  sh -c '/wlcg/sidecar.sh 2>&1 | tee /data/sidecar.log'  &

jobs -p > pids.txt
wait < pids.txt
rm pids.txt
```
#### Singularity

```
$> cat shellseq_sing.sh
#!/bin/sh

datadir="${PWD}/work_$(date '+%s')"
mkdir $datadir

singularity exec -B $datadir:/data -B $PWD/configmap:/wlcg docker://lukasheinrich/middlewareimage  sh -c 'LOGFILE=/data/step1.log PIDFILE=/data/step1.pid WAITFORFILE=/data/_wlcg_done_0.txt TOMBSTTONEFILE=/data/_wlcg_done_1.txt /wlcg/wrapper.sh /wlcg/step1.sh'  &
singularity exec -B $datadir:/data -B $PWD/configmap:/wlcg docker://lukasheinrich/payloadimage  sh -c 'LOGFILE=/data/step2.log PIDFILE=/data/step2.pid WAITFORFILE=/data/_wlcg_done_1.txt TOMBSTTONEFILE=/data/_wlcg_done_2.txt /wlcg/wrapper.sh /wlcg/step2.sh'  &
singularity exec -B $datadir:/data -B $PWD/configmap:/wlcg docker://lukasheinrich/middlewareimage sh -c 'LOGFILE=/data/step3.log PIDFILE=/data/step3.pid WAITFORFILE=/data/_wlcg_done_2.txt TOMBSTTONEFILE=/data/_wlcg_done_3.txt /wlcg/wrapper.sh /wlcg/step3.sh'  &
singularity exec -B $datadir:/data -B $PWD/configmap:/wlcg docker://lukasheinrich/middlewareimage  sh -c '/wlcg/sidecar.sh 2>&1 | tee /data/sidecar.log'  &

jobs -p > pids.txt
wait < pids.txt
rm pids.txt
```

```
./shellseq_sing.sh.sh
```

### Run with Kubernetes

```
python gen_sequence.py
kubectl create configmap wrapper --from-file=configmap -o yaml --dry-run|kubectl replace -f - --force
kubectl replace -f kubeseq.yml --force
```

check logs with

```
kubectl get pods -l job-name=mljob -o name|xargs kubectl logs -c stage1
kubectl get pods -l job-name=mljob -o name|xargs kubectl logs -c stage2
kubectl get pods -l job-name=mljob -o name|xargs kubectl logs -c stage3
kubectl get pods -l job-name=mljob -o name|xargs kubectl logs -c sidecar
```
