#! -*- coding: utf-8 -*-
# 根据pid找所属container（docker）

import glob, os, sys

pid = sys.argv[1]
dockers = glob.glob('/sys/fs/cgroup/memory/docker/*/cgroup.procs')
container_id = None

for docker in dockers:
    if pid in open(docker).read().strip().split('\n'):
        container_id = docker[29:-13]
        break

if container_id is None:
    print(u'找不到对应的container')
else:
    commandline = 'docker ps -a --format \'{{.ID}}: {{.Names}}\' --filter id=\'%s\''
    os.system(commandline % container_id)
