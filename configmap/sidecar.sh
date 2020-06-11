#/bin/sh
echo $(date) - sidecar

ls -lrt /data

touch /data/_wlcg_done_0.txt 

MONITOR_PIDFILE=/data/step2.pid.txt

while [ ! -f $MONITOR_PIDFILE ]
do
    sleep 2
done
payload_pid=$(cat $MONITOR_PIDFILE)

echo "payload at ${payload_pid} -- start monitoring"

tail --pid=${payload_pid} -f /dev/null

echo "payload is done ${payload_pid} -- stop monitoring"

ls -lrt /data

echo $(date) - done sidecar
