# JLD2 库的学习

## 读写数据



示例一：

```Julia
using JLD2
# 写入数据
hello = "world"
foo = :bar
@save "example.jld2" hello foo

# 读取数据
@load "example.jld2" hello foo
```

JLD2包自己内置了两个宏 **@load** **@save** ,使用方法如下

@save   <filename>  写入数据到filename中

@ load  <filename>   从filename中读取数据

