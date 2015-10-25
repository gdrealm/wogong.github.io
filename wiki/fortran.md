title: fortran
date: 2014-01-01
modified: 2015-08-02 19:16:27

## Basic
### 数据类型
- integer
- logical
- real
### 基本结构
- do loop
    
    do i=1,N
        blah
    end do

    do while()
        blah
    end do
- if


或许你会想学 Fortran，却苦于找不到 Fortran 90 编译程式，这一点在近两三年已经不是问题了，因为至少有三个 Fortran 90 编译程式是免费的。第一个就是Lahey 公司的 ELF (Essential Lachey Fortran) ，你可以在http://www.lahey.com 中找到它。它是个 Fortran 90/95 标准的程式，但是ELF 中去掉了一些比较不常用，很复杂的功能；再者，为了让用 ELF 的朋友写作结构良好的程式，它强迫你写作满足某些规格的程式。这并非是个问题，我是很赞成这样做，你用了 ELF 就知道为什么。请注意，ELF 只能在Windows 95/98/NT 之下作业。若想有个完整 Fortran 90/95 编译程式，不妨试试 Lahey的Lahey LF95 Express。

在 Linux 上的情况比较好，目前它已经有了免费的 Fortran 77 编译程式，叫做 g77。要用 Fortran 90 有两条路，第一是用一套叫做 F 的语言。与 ELF 一样，去掉了很多不必要的功能，也强制用户写作的好格局 Fortran 程式，你可在下面的网址抄录免费的 Linux 版 F: http://www.fortran.com/fortran 。

Pasific-Sierra Research 公司最近也提供了一个 Linux 用的完整 Fortran 90 编译程式，在http://www.psrv.com ，这个叫做 VAST/F90 的 Fortran 90 编译程式，也是免费的，也少了一些功能，但对初学者而言，这些少掉了的功能根本不会有什么影响。这也是个 Linux 用的编译程式，却不是个完整的编译系统。

VAST/F90 把你的 Fortran 90 程式翻译成 Fortran 77，再由 Linux 上的g77 翻译成机器语言，所以你的 Linux 系统上必须有 g77，版本多号码至少要是 0.5.21 以上。Pasific-Sierra Research 还有其它有趣的 Fortran 90 产品，例如说支援在Linux 下双处理器的HPF (High Performance Fortran) ，这也免费的。

如果你想要知道Fortran 的功能与其它资讯，你不妨试试http://www.fortran.com (Fortran Market) 与http://www.fortranlib.com (Fortran Link) 。



1. 简洁严格的编译器：elf90

elf90 严格的Fortran90的子集

elf90安装在“Program Files”中在命令行中调用会出现错误，
猜测是因为其中的空格导致。尚未测试。

- doesn't support `print`, `write(*,*)` instead
- `stop` in the end

    if () then
        blah
    else
        blah
    end if

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

矩阵转置

语法格式：result = TRANSPOSE (matrix) 
例子：B is the array 

[ 2 3 4 ]
[ 5 6 7 ]
[ 8 9 1 ].

TRANSPOSE ( 结果是
[ 2 5 8 ]
[ 3 6 9 ]
[ 4 7 1 ].
第二种情况
INTEGER array(2, 3), result(3, 2)
array = RESHAPE((/1, 2, 3, 4, 5, 6/), (/2, 3/))
! array is 1 3 5
! 2 4 6
result = TRANSPOSE(array)
! result is 1 2
! 3 4
! 5 6
END


## compiler
1. gFortran

默认支持的列长有限，需要`-ffree-line-length-0`去除限制

	gfortran polyhedron.f90 qsort.f90 -ffree-line-length-0

2. elf90

3. Compaq Visual Fortran
    debug还是用这个玩意比较靠谱。



1,goto
goto 在Fortran77中就流传下来了，它提供一个任意跳跃到所赋值行代码的位置，如果是在一个do 循环中如
do 30 i=1,N
   if(……)  goto 30
30 continue 
上语句的意思就是如果符合if里的条件，则会进行下一次循环。


2，pause
pause的功能就能跟它的字面意思相同，程序执行到pause 时，会暂停执行，直到用户按下Enter键才会继续执行。


3. continue
continue这个命令没有实际的用途，它的功能就是 继续向下执行程序


4，stop
它可用来结束程序执行。


5，cycle
cycle命令可由略过循环的程序模块中，在cycle命令后面的所有程序代码，直接跳回循环的开头来进行下一次循环。
如
do floor=1,dest
  if(floor==4) cycle
write(*,*) floor
end do

执行结果如下
1 
2
3
5
6
……


6。exit
exit的功能是可以直接跳出一个正在进行的循环，不论是do 循环还是do while 循环。
