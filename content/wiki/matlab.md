title: matlab
date: 2014-09-10
modified: 2015-07-21 21:43:21

MATLAB MATrix LABoratory

x=solve('x^2+100*x+99=0','x')

　　Matlab作为一门科学计算语言，在求解矩阵运算方面非常方便。　　
　　求解AX=B
　　Matlab代码：X=A\B或者X=mldivide(A,B)或者X=inv(A)*B
　　mldivide()是运算符\的函数封装，作用是一样的。对于\求解X，Matlab采用的是高斯消元法求解。inv()作用是求矩阵的逆，采用inv(A)*B求解X不如\精确。
　　求解XA=B
　　Matlab代码： X=B/A或者X=mrdivide(B,A)或者X=B*inv(A)
　　如果方程没有解，上面方法求解都是一个最小二乘解。


## Install
1. MATLAB运行错误
error while loading shared libraries: libXp.so.6: cannot open shared object file: No such file or directory
MATLAB R2010b linux3.2.8 i686
将安装包中的库文件移动到系统库即可。

sudo cp /mnt/bin/glnx8/libwinstall.so.6 /usr/lib

2. win7 32bit 环境，安装成功后出现键盘映射错误的状况，整体偏移。
经过搜索，发现是字体设置的问题，
在preferences中将font设置全部改为customed即可解决。

## Note
1. `!echo text`  显示text
2. 对于符号积分：首先定义符号变量，对于复杂积分尽量化简，
才有可能求出精确解。大多数情况下
提示：Warning: Explicit integral could not be found. 无法求解。
3. 矩阵求和函数sum
a=sum(A) %列求和
b=sum(A,2) %行求和
c=sum(A(:)) %矩阵求和
假定A为一个矩阵：
sum(A)以矩阵A的每一列为对象，对一列内的数字求和。
sum(A,2)以矩阵A的每一行为对象，对一行内的数字求和。
a(:,1)是求矩阵的第一列
a(1,:)是求矩阵的第一行
4. 取余函数
`mod/rem`
5. 取商函数
`fix(x./y)`
6. MATLAB数据显示格式
FORMAT SHORT Scaled fixed point format with 5 digits.
FORMAT LONG Scaled fixed point format with 15 digits for double and 7 digits for single.
FORMAT SHORT E Floating point format with 5 digits.
FORMAT LONG E Floating point format with 15 digits for double and 7 digits for single.
FORMAT SHORT G Best of fixed or floating point format with 5 digits.
FORMAT LONG G Best of fixed or floating point format with 15 digits for double and 7 digits for single.
FORMAT may be used to switch between different output display formats of all numeric variables as follows:
FORMAT HEX Hexadecimal format.
FORMAT + The symbols +, - and blank are printed for positive, negative and zero elements. Imaginary parts are ignored.
FORMAT BANK Fixed format for dollars and cents.
FORMAT RAT Approximation by ratio of small integers.
FORMAT may be used to affect the spacing in the display of all variables as follows:
FORMAT COMPACT Suppresses extra line-feeds.
FORMAT LOOSE Puts the extra line-feeds back in 
7. `...` 用于多行输入
8. 随机数 0-1均匀分布 rand()
9. 画点 `plot(x,y,'*')`

子程序

    funtion F=functionname(a,b)
        F=a+b;
    end


