#/bin/sh
echo $(date) - stage in
ls -lrt /wlcg
ls -lrt /data
ls -lrt /code
sleep 2
python3 /code/pilot_runpre.py
echo $(date) - done stage in
