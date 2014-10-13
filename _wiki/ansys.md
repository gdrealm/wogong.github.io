---
layout: wiki
title: ansys
create: 2014-01-01
update: 2014-10-10
---

## 一般过程
1. 分析环境设置
	/filename
	/title
	/prep7 进入前处理器
2. 定义单元类型
	/et
3. 定义材料模型
	MP
4. 建立几何模型
	BLOCK
5. 网格划分
6. 边界条件
7. 荷载

APDL 文件输入

AutoCAD Mechanical 导出 IGES file

## note	
1. crack 排查问题的方向：licence server + licence client
2. Solution Methods  
Two solution methods are available for solving structural problems in the ANSYS family of products: the h-method and the p-method. The h-method can be used for any type of analysis, but the p-method can be used only for linear structural static analyses. Depending on the problem to be solved, the h-method usually requires a finer mesh than the p-method. The p-method provides an excellent way to solve a problem to a desired level of accuracy while using a coarse mesh. In general, the discussions in this manual focus on the procedures required for the h-method of solution.
3. Preferences for GUI filtering 只是对GUI显示起作用，其他不影响
4. 

## Keywords

* DL, LINE, AREA, Lab, Value1, Value2
Defines DOF constraints on lines.

* DLDELE, LINE, Lab
Deletes DOF constraints on a line.


## install on windows
as standard user, you should install Ansys as administrator.
then you will get a environment varible error running Ansys. Just copy the ansys related environment varibles to current users. Done.
