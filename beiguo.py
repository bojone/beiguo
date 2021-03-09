#! -*- coding: utf-8 -*-
# 根据pid找所属container（docker）

import glob, os, sys

pid = sys.argv[1]
dockers = glob.glob('/sys/fs/cgroup/memory/docker/*/cgroup.procs')
is_found = False

for docker in dockers:
    if pid in open(docker).read().strip().split('\n'):
        is_found = True
        container_id = docker.replace('/sys/fs/cgroup/memory/docker/', '')
        container_id = container_id.replace('/cgroup.procs', '')
        break

if is_found:
    commandline = 'docker ps --format \'{{.ID}}: {{.Names}}\' | grep %s'
    os.system(commandline % container_id[:12])
else:
    print(u'找不到对应的container')
