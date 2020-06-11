# wfms_prototype

```
python gen_sequence.py
./shellseq.sh
```

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
