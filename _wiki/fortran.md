---
layout: wiki
title: fortran
create: 2014-01-01
update: 2014-05-18
---

1. 简洁严格的编译器：elf90

elf90 严格的Fortran90的子集

elf90安装在“Program Files”中在命令行中调用会出现错误，
猜测是因为其中的空格导致。尚未测试。

- doesn't support `print`, `write(*,*)` instead
- `stop` in the end


----

where结构：

    where(数组条件)
	    数组赋值
		...
	elsewhere
		数组赋值
		...
	end where

* 形状相同
* 不许嵌套
* 最多两个分支

cycle与exit语句
		
    do
		...
		if(cond1) cycle
		...
		if(cond2) exit
		...
	end do
	...


Memory：单精度
Register：双精度

elf未经优化，step by step，C先算出结果存储到临时变量，存入memory，再调入寄存器比较。

CVF，Debug未优化，Release优化，即使人为添加中间变量，Release依旧优化！（设置enable floating consistency，则同Debug，因为考虑了浮点数的一致性）

Lesson:Always use double precision floating numbers, which is adopted by this course.

重视数值精度的概念，数据结构。	


1. SIZE函数  C = SIZE(A[,DIM]) [] []
   
   其中A是被查询数组，可以是假定大小数组，但不能是未定
义的指针数组或未分配空间的可分配数组。当DIM等于1
时，表示查询数组有几行；当DIM等于2时，表示查询数组
有几列；当DIM被省略时，表示查询数组有多大（即有多少
个元素）。
   
   整型查询函数，
   如果指定了DIM参数，则返回数组特定维度的宽度，否则，将返回所有数组的个数。
  ARRAY是任意类型的数组，一定不能是无关联的指针或者未分配的可分配数组。DIM为整数，且 1<=DIM<=r ，如果ARRAY不定大小的数组，则必须指定DIM参数，而且其值必须小于r
SIZE(ARRAY, dim) is a function which returns the number of elements in an array ARRAY, if DIM is not given, and the number of elements in the relevant dimension if DIM is included.

2. 数组赋值
fortran 列优先。如 2 times 3 的矩阵，第 1、2 行分别为 1 2 3、4 5 6
应该这样赋值。/1, 4, 2, 5, 3, 6/


## subroutine



## 固有函数

- random_seed()
- random_number()
- qsort() http://nf.nci.org.au/facilities/software/FORTRAN/Intel10/doc/main_for/mergedProjects/lref_for/source_files/rfqsort.htm
- 