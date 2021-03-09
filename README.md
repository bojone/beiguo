# 背锅侠

这是个很简单的脚本，根据进程pid找所属的container（docker）。

## 场景

当你在服务器上发现某个进程占用了大量CPU/GPU，严重拖慢了服务器进度时，你可能会想找到这个进程对应的负责人。由于使用了docker，user那一栏很可能显示的是root，而无法对应到人。

所以我们需要根据pid找到对应的container，根据container名字找到对应的人进行理论（背锅）。

## 使用

```python
python beiguo.py <pid>
```

输出：`<container_id>: <container_names>`或`找不到对应的container`。

## 交流

QQ交流群：808623966，微信群请加机器人微信号spaces_ac_cn
