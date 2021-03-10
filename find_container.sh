#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: find_container.sh PID"
    exit -1
fi

PID=$1
for FILE_PATH in $(find /sys/fs/cgroup/memory/docker/ -mindepth 2 -maxdepth 2 -name cgroup.procs)
do
    if [ $(grep -E "^${PID}\$" "$FILE_PATH") ]
    then
        CONTAINER_ID=`echo "$FILE_PATH" | sed -n "s/.*\/\([a-z0-9]\+\)\/cgroup.procs$/\1/p"`
        echo $CONTAINER_ID
    fi
done
