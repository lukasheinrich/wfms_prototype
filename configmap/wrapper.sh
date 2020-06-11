#!/bin/sh
if [ -f $WAITFORFILE ];then
    echo $WAITFORFILE already existed at startup
else
    echo waiting for $WAITFORFILE
fi
if [ -f $TOMBSTTONEFILE ];then
    rm $TOMBSTTONEFILE
fi
while [ ! -f $WAITFORFILE ]
do
    sleep 2
done
script=$1
echo running ${script}
(${script} 2>&1 | tee $LOGFILE) & 
echo "process id $!"
echo $! > $PIDFILE.txt
wait
touch $TOMBSTTONEFILE
