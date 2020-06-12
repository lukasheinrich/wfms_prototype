#/bin/sh
echo $(date) - stage out
ls -lrt /wlcg
ls -lrt /data
ls -lrt /code
sleep 2
python3 /code/pilot_runpost.py
echo $(date) - stage out
