# 背锅侠

这是个很简单的脚本，根据进程pid找所属的container（docker）。

## 场景

当你在服务器上发现某个进程占用了大量CPU/GPU，严重拖慢了服务器进度时，你可能会想找到这个进程对应的负责人。由于使用了docker，top命令的user那一栏很可能显示的是root，而无法对应到人。

所以我们需要根据pid找到对应的container，根据container名字找到对应的人进行理论（背锅）。

## 使用

```bash
python beiguo.py <pid>
```

输出：`<container_id>: <container_names>`或`找不到对应的container`。

为了方便使用，建议在`~/.bashrc`加一句：
```bash
alias beiguo='python <path_to_beiguo>/beiguo.py'
```
然后就可以直接`beiguo <pid>`了。

## 其他

[find_container.sh](https://github.com/bojone/beiguo/blob/main/find_container.sh)是网友[@BorisPolonsky](https://github.com/BorisPolonsky)贡献的纯bash版本，用法类似，也欢迎尝试。

## 交流

QQ交流群：808623966，微信群请加机器人微信号spaces_ac_cn
