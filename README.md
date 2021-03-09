# 背锅侠

根据进程pid找所属的container（docker）。

## 使用

```python
python beiguo.py <pid>
```

输出：`<container_id>: <container_names>`或`找不到对应的container`。
