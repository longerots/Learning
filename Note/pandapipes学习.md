# pandapipes学习

## 简介

pandapipes是用于模拟分析区域供热和天然气系统的管网计算程序，使用pandas来作为分析框架。

## 优势

多能互补网络（multi-energy networks)目前已成为愈发热门的研究课题之一。为了模拟多能网络，不仅要考虑各能量部分之间的耦合点，也要考虑关注部分的管网状态。pandapipes就是为此而生。

为什么不采用其他的工具呢？

1. 目前并没有很多致力于多能网络模拟的工具
2. 大部分计算流动网络的软件都为商用
3. 对于其他软件，优势如下
4. ![image-20200913201607336](/Users/wanglong/Library/Application Support/typora-user-images/image-20200913201607336.png)

## 定位

pandapipes志在对平衡流体系统进行静态分析，包括：

- 对使用不可压缩流体或者可压缩流体的网络进行关于压力和速度分布的静态（static）和准静态（quasi-static）分析（假定气体组分是不变的）
- 对于流体网络的温度分布的静态或者准静态分析（目前只考虑不可压缩流体）

## 流体系统模拟

### 数据结构

pandapipes基于表格数据结构，其中每个元素类型由一个包含特定元素的所有参数的表和一个包含不同分析方法的特定元素结果的结果表表示。

表格数据类型给予python的pandas库组成，允许存储任意数据类型的变量，因此参数能够同时用**状态变量**和**元数据**来存储（如名字或者描述）。表格能够通过增加新的列（不会影响到pandapipes的函数）来进行扩展或者自定义，并且所有关于pandas的方法都能够在这里继承使用（读、写、分析）。

### 标准的类型库

pandapipes包含标准类型库，允许使用预定义基础标准类型参数来创建管道（pipe）和泵（pump）。用户能够自定义自己的标准组件或者直接使用预定义的基础标准库用来组建管网。

### 流体物性库

pandapipes包含流体特性库，允许使用预定义的数据来创建流体物性参数。同样，用户可以定义自己的物性参数或者使用预定义的参数。

### 流体系统分析

pandapipes支持下面的流体系统分析函数：Pipe Flow

#### pipe flow

Panpipes管道流动求解器的基础是牛顿拉弗森方法（Newton-Raphson method）

pandapipes提供了两种不同的方法（flat start和 solution vector of a previous calculation）来初始化管道流计算的求解向量

## 测试和验证

目前pandapipes已经成功使用pytest测试。

测试方法：由[STANET](http://www.stafu.de/de/home.html)和[OpenModelica](https://www.openmodelica.org/)来创建测试网络，并使用相应的转换器来转换成pandapipes的网络，并在PyCharm中运行。总共有83个测试案例，包括使用STANET创建的22个水网和21个气网的例子和使用OpenModelica创建的32个水网和8个热网的例子。对于各个具体的案例的调用可以参考pandapipes文档的[Networks](https://pandapipes.readthedocs.io/en/latest/networks.html)章节，所有测试例子的拓扑结构如下:

![cross](https://www.pandapipes.org/images/about/validation/cross.png)

![delta](https://www.pandapipes.org/images/about/validation/delta.png)

![delta_2sinks](https://www.pandapipes.org/images/about/validation/delta_2sinks.png)

![district](https://www.pandapipes.org/images/about/validation/district.png)

### STANET 的测试案例

STANET测试网络以CSV文件的格式存储，方便后续转换为json文件。当误差容错达到要求时，测试就通过了。通常，对于压力计算而言，其相对误差通常低于0.002即可。在其余的两种情况下这个限制将会增加，第一种是增加至0.01，第二种是增加到0.03。
$$
p_{diff}=|(p_{stanet}-p_{pandapipes})/p_{stanet}|
$$
流量计算时，其绝对误差总是要小于0.03
$$
v_{diff,abs} = |v_{stanet} - v_{pandapipes}|
$$

### OpenModelica的测试案例

通过使用包含模拟结果的 mo- 和 mat- 文件，OpenModelica网络可以转换成pandapipes的管网。OpenModelica使用[Navier-Stokes方程](https://www.maplesoft.com/documentation_center/online_manuals/modelica/Modelica_Fluid_UsersGuide_ComponentDefinition.html#Modelica.Fluid.UsersGuide.ComponentDefinition.BalanceEquations)来计算压降和流量，而pandapipes使用的方法与STANET相似（应该都是牛顿拉弗森方法）。因此，误差容错也相应的增加。对于压力的相对误差而言，0.01常常能够满足要求。在3个例子中这个限制增加到了0.02，在两个例子中分别增加到了0.06和0.4（推测，这种偏差是由于网络的复杂性造成的，不太可能是由于泵和阀造成的，因为相对误差为0.01的网络也包含泵和阀）。此外，热网的相对压力偏差范围是0.01到0.05。
$$
p_{diff} = |(p_{modelica} - p_{pandapipes})/p_{modelica}|
$$
流速的绝对误差通常低于0.05
$$
v_{diff,abs} = |v_{modelica}-v_{pandapipes}|
$$
对于换热网络的计算，平均温度Tdiff，均值相对误差的上容限值在0.004 ~ 0.04之间。
$$
T_{diff,mean} = |(T_{mean,modelica}-T_{mean,pandapipes})/T_{mean,modelica}|
$$
