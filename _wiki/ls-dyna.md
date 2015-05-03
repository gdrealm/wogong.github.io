---
layout: wiki
title: LS-DYNA
create: 2015-03-20
update: 2015-04-20
---

## Note
1. 时间步长控制
2. 材料参数的单位很重要，注意不要弄错了。

## Material
0. *MAT_RIGID
        *MAT_RIGID
        $ mid ro e pr n couple m alias
        1 4.064E+03 4.000E+08 3.000E-01 0.000E+00 0.000E+00 0.000E+00
        0.000E+00 0.000E+00 0.000E+00
        0.000E+00 0.000E+00 0.000E+00 0.000E+00 0.000E+00 0.000E+00 0.000E+00 0.000E+00
        $

1. MAT_SOIL_CONCRETE

        *MAT_SOIL_CONCRETE
         1       2.500   1.250E-01   1.667E-01   1   2   3   4
        -2.00E-05   0.0 0.3         1
        $
        *DEFINE_CURVE
                  1         0 0.0000000 0.0000000 0.0000000 0.0000000
                          0.0           0.0
                          0.0953        0.230E-01
                          0.1823        0.650E-01
                          0.2624        1.300E-01
                          0.3365        1.750E-01
                          0.4055        2.250E-01
                          0.2700        3.500E-01
        $
        *DEFINE_CURVE
                  2         0 0.0000000 0.0000000 0.0000000 0.0000000
                          0.0           0.0
                          0.400E-02     0.240E-02
                          0.800E-02     0.550E-02
                          1.200E-02     0.950E-02
                          1.400E-02     1.260E-02
                          1.800E-02     1.550E-02
                          1.000E-01     1.550E-02
        $
        *DEFINE_CURVE
                  3         0 0.0000000 0.0000000 0.0000000 0.0000000
                        0.00            0.00
                        1.500E-04       0.00
                        1.000E-03       0.04
                        1.000E-02       0.49
                        1.000E-01       4.90
        $
        *DEFINE_CURVE
                  4         0 0.0000000 0.0000000 0.0000000 0.0000000
                        0.00            0.01
                        1.500E-04       0.01
                        1.000E-03       0.05
                        1.000E-02       0.50
                        1.000E-01       5.00
        $

2. MAT_JOHNSON_COOK

        *MAT_JOHNSON_COOK
                 1   7.83000      0.77    
         7.920E-03 5.100E-03     0.260 0.140E-01      1.03 0.1793E+04       294 0.100E-05
         0.477E-05 -9.00E+00      3.00       0.0      5.00      0.00      0.00      0.00          
              0.00    
        $
        *EOS_GRUNEISEN
                 1    0.4569     1.490      0.00      0.00      2.17      0.46      0.00    
              1.00 

3. KC
        
        $
        *MAT_CONCRETE_DAMAGE_REL3
        $#     mid        ro        pr
                 1      2400      0.20
        $#      ft        a0        a1        a2
           2.64E+6  -3.28E+7
        $# slambda      nout     edrop     rsize       ucf    lcrate  locwidth      npts
             0.000     0.000     0.000 39.369999  1.450E-4     0.000     0.000
        $# lambda1   lambda2   lambda3   lambda4   lambda5   lambda6   lambda7
             0.000     0.000     0.000     0.000     0.000     0.000     0.000
        $#lambda09  lambda10  lambda11  lambda12  lambda13        b3       a0y       a1y
             0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
        $#    eta1      eta2      eta3      eta4      eta5
             0.000     0.000     0.000     0.000     0.000
        $#   eta09     eta10     eta11     eta12     eta13        b2       a2f       a2y
             0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
        $
        *EOS_TABULATED
               1      0.00      0.00      1.00 
            0.00      -0.480E-03        -0.10536        -0.10542        -0.10547 
        -0.10592        -0.10647        -0.11093        -0.11653        -0.12217 
            0.00       0.770E-02           0.800           0.804           0.808 
           0.839           0.877            1.18            1.56            1.93 
            0.00            0.00            0.00            0.00            0.00
            0.00            0.00            0.00            0.00            0.00

4. *MAT_CRUSHABLE_FOAM
        
        $ MPa mm N s g g/mm3
        *MAT_CRUSHABLE_FOAM
        $ mid    ro        e          pr      lcid     tsc   damp
            1       6.756   263   0.01   1         2.5   0.1
        $
        *DEFINE_CURVE
        $ lcid sidr scla sclo offa offo
           1         0 0.0000000 0.0000000 0.0000000 0.0000000
        $               abscissa        ordinate
                            0.00141 0
                            1.30295 0.01079
                            2.56204 0.02172
                            3.21139 0.03266
                            3.46463 0.043
        $

## Contact

        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $                              CONTACT DEFINITIONS                             $
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $
        $弹体与砂浆
        *CONTACT_ERODING_SURFACE_TO_SURFACE
                 4         1         3         3         0         0         0         0
         0.050     0.050     0.000     0.000     0.000             1 0.000    0.1000E+08
         1.000     1.000     0.000     0.000     1.000     1.000     1.000     1.000    
                 1         1         0
        $
        $
        $弹体与块石
        *CONTACT_ERODING_SURFACE_TO_SURFACE
                 4         2         3         3         0         0         0         0
         0.050     0.050     0.000     0.000     0.000             1 0.000    0.1000E+08
         1.000     1.000     0.000     0.000     1.000     1.000     1.000     1.000    
                 1         1         0
        $
        $砂浆与块石
        *CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
                 1         2         3         3         0         0         0         0
         0.572     0.572     0.000     0.000     0.000             0 0.000    0.1000E+08
         1.000     1.000     0.000     0.000     1.000     1.000     1.000     1.000    
        $
        $砂浆与沙土层
        *CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
                 1         3         3         3         0         0         0         0
         0.572     0.572     0.000     0.000     0.000             0 0.000    0.1000E+08
         1.000     1.000     0.000     0.000     1.000     1.000     1.000     1.000    
        $
        $砂浆与砂浆
        *CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
                 1         1         3         3         0         0         0         0
         0.572     0.572     0.000     0.000     0.000             0 0.000    0.1000E+08
         1.000     1.000     0.000     0.000     1.000     1.000     1.000     1.000    
        $
        $块石与块石
        *CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
                 2         2         3         3         0         0         0         0
         0.572     0.572     0.000     0.000     0.000             0 0.000    0.1000E+08
         1.000     1.000     0.000     0.000     1.000     1.000     1.000     1.000    
        $

##　关于 K 文件
0. k文件格式分为标准格式和自由格式（数据之间用逗号隔开）两种，在一个k文件中，两种方式可以并存，但是在一个数据卡中，只能选择一种方式
1. 如果选择标准格式：k文件中除了节点（node）和单元（element）关键字外，通常每一行总共占80个字符长度，每个数据占10个字符长度，修改时千万不要超越这10个字符长度的位置，也不要跑到别的数据的10个字符位置
2. 如果关键字手册里的card介绍中没有提到optional，那么每一行card都不能省略，哪怕它们都是0
3. 为了方便查看10个字符长度，可以用ultraedit软件
4. 每一个关键字必须以\*开头，并且必须顶格写
5. 在k文件中$后面的是注释，求解时不考虑
6. 为了查找和发现具体是那一关键字出错，可以使用lspost打开k文件，然后选择view选项查看