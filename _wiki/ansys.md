---
layout: wiki
title: ansys
create: 2014-01-01
update: 2015-04-01

---

## Note	
1. crack 排查问题的方向：licence server + licence client
2. Solution Methods  
Two solution methods are available for solving structural problems in the ANSYS family of products: the h-method and the p-method. The h-method can be used for any type of analysis, but the p-method can be used only for linear structural static analyses. Depending on the problem to be solved, the h-method usually requires a finer mesh than the p-method. The p-method provides an excellent way to solve a problem to a desired level of accuracy while using a coarse mesh. In general, the discussions in this manual focus on the procedures required for the h-method of solution.
3. Preferences for GUI filtering 只是对GUI显示的内容起过滤作用，其他不影响
4. install on windows  
as a standard user, you should install Ansys as administrator.
then maybe you will get an environment varible error running Ansys. Just copy the ansys related environment varibles to current users. Done.
5. prepost  制作动画，file-movie
6. contact 接触分析
http://v.pps.tv/play_3ECRJX.html 简支梁 点面接触分析视频 4min  

## Process
1. 分析环境设置
    /filename
    /title
    /prep7 进入前处理器

2. 定义单元类型
    ET, ITYPE, Ename, KOP1, KOP2, KOP3, KOP4, KOP5, KOP6, INOPR // Defines a local element type from the element library.
    R, NSET, R1, R2, R3, R4, R5, R6 // Defines the element real constants.
    RMORE, R7, R8, R9, R10, R11, R12 // Adds real constants to a set.

3. 定义材料模型
    MP
    TB, Lab, MAT, NTEMP, NPTS, TBOPT, EOSOPT, FuncName // Activates a data table for material properties or special element input.
    eg: tb, MISO, 1, 0, 9

4. 建立几何模型
    WPAVE, X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3 // Moves the working plane origin to the average of specified points.
    
    CSWPLA, KCN, KCS, PAR1, PAR2 // Defines a local coordinate system at the origin of the working plane.
    
    CSYS, KCN // Activates a previously defined coordinate system.

    KGEN, ITIME, NP1, NP2, NINC, DX, DY, DZ, KINC, NOELEM, IMOVE // Generates additional keypoints from a pattern of keypoints.
    
    BLOCK, X1, X2, Y1, Y2, Z1, Z2 // Creates a block volume based on working plane coordinates.
    
    BLC4, XCORNER, YCORNER, WIDTH, HEIGHT, DEPTH // Creates a rectangular area or block volume by corner points.

    LOVLAP, NL1, NL2, NL3, NL4, NL5, NL6, NL7, NL8, NL9 // Overlaps lines. see help doc fotr illustration 

    CYLIND, RAD1, RAD2, Z1, Z2, THETA1, THETA2 // Creates a cylindrical volume centered about the working plane origin.
    $$

5. 网格划分

    aatt 设置几何模型-面的属性
    KMESH, NP1, NP2, NINC // Generates nodes and point elements at keypoints.
    AMESH, NA1, NA2, NINC // Generates nodes and area elements within areas.

    LESIZE, NL1, SIZE, ANGSIZ, NDIV, SPACE, KFORC, LAYER1, LAYER2, KYNDIV // Specifies the divisions and spacing ratio on unmeshed lines.
    $$ lesize,all,,,8,,,,,

    ESIZE, SIZE, NDIV // Specifies the default number of line divisions.

    LSEL, Type, Item, Comp, VMIN, VMAX, VINC, KSWP // Selects a subset of lines.
    $$ lsel,s,line,,1,1
    $$ lesl,a,line,,2,2
    
    ASEL, Type, Item, Comp, VMIN, VMAX, VINC, KSWP // Selects a subset of areas.
    $$ asel,s,area,,1,1

    VSEL, Type, Item, Comp, VMIN, VMAX, VINC, KSWP // Selects a subset of volumes. eg: vsel,s,volu, ,vmin,vmax, ,
    
    NSEL, Type, Item, Comp, VMIN, VMAX, VINC, KABS // Selects a subset of nodes.
    $$ nsel,s,loc,z,0,0.00001
    

    ESEL, Type, Item, Comp, VMIN, VMAX, VINC, KABS // Selects a subset of elements.

    NSLV, Type, NKEY // Selects those nodes associated with the selected volumes.
    NSLA, Type, NKEY // Selects those nodes associated with the selected areas.
    NSLL, Type, NKEY // Selects those nodes associated with the selected lines.
    

    ESURF, XNODE, Tlab, Shape // Generates elements overlaid on the free faces of existing selected elements.

    vsweep

6. 边界条件
    DL, LINE, AREA, Lab, Value1, Value2 // Defines DOF constraints on lines.
    DLDELE, LINE, Lab // Deletes DOF constraints on a line.    

    D, Node, Lab, VALUE, VALUE2, NEND, NINC, Lab2, Lab3, Lab4, Lab5, Lab6 // Defines degree-of-freedom constraints at nodes.
    $$d,node,all

    DK, KPOI, Lab, VALUE, VALUE2, KEXPND, Lab2, Lab3, Lab4, Lab5, Lab6 // Defines DOF constraints at keypoints.
    
7. 荷载
    SF, Nlist, Lab, VALUE, VALUE2 // Specifies surface loads on nodes.
    SFL, Line, Lab, VALI, VALJ, VAL2I, VAL2J // Specifies surface loads on lines of an area.

    EDVEL, Option, Cname, VX, VY, VZ, OMEGAX, OMEGAY, OMEGAZ, XC, YC, ZC, ANGX, ANGY, ANGZ // Applies initial velocities to nodes or node components in an explicit dynamic analysis.
    $$edvel,vgen,load_face,0,0.5,0

    EDPVEL, Option, PID, VX, VY, VZ, OMEGAX, OMEGAY, OMEGAZ, XC, YC, ZC, ANGX, ANGY, ANGZ // Applies initial velocities to parts or part assemblies in an explicit dynamic analysis.
    $$edpvl,vgen,3,0,-0.5,0

    EDCGEN, Option, Cont, Targ, FS, FD, DC, VC, VDC, V1, V2, V3, V4, BTIME, DTIME, BOXID1, BOXID2 // Specifies contact parameters for an explicit dynamics analysis.

8. 求解
    NSUBST, NSBSTP, NSBMX, NSBMN, Carry // Specifies the number of substeps to be taken this load step.
    OUTRES, Item, Freq, Cname, -- , NSVAR // Controls the solution data written to the database.
    LSSOLVE, LSMIN, LSMAX, LSINC // Reads and solves multiple load steps.

8. Other
    *GET, Par, Entity, ENTNUM, Item1, IT1NUM, Item2, IT2NUM // Retrieves a value and stores it as a scalar parameter or part of an array parameter.
    
    AUTOTS, Key // Specifies whether to use automatic time stepping or load stepping.
    
    PROD, IR, IA, IB, IC, Name, --, --, FACTA, FACTB, FACTC // Multiplies variables.
    OUTRES, Item, Freq, Cname, -- , NSVAR // Controls the solution data written to the database.

    CM, Cname, Entity // Groups geometry items into a component.

    CMSEL, Type, Name, Entity // Selects a subset of components and assemblies.

    MODMSH, Lab // Controls the relationship of the solid model and the FE model.

    *DIM, Par, Type, IMAX, JMAX, KMAX, Var1, Var2, Var3, CSYSID // Defines an array parameter and its dimensions.
    $$ 
    
    *VREAD, ParR, Fname, Ext, --, Label, n1, n2, n3, NSKIP // Reads data and produces an array parameter vector or matrix.
