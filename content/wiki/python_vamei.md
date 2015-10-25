---
layout: wiki
title: python_vamei
date: 2015-06-17
---

作者：Vamei 出处：http://www.cnblogs.com/vamei 欢迎转载，也请保留这段声明。谢谢！

=== Python基础教程（手册） ===
说明

1. 教程将专注于Python基础，语法基于Python 2.7, 适用环境为Linux, 将不会使用到标准库之外的模块

2. 我将专注于python的主干，以便读者能以最快时间对python形成概念。

3. Linux命令行将以 ‘$’ 开始，比如 $ls, $python

4. python命令行将以 '>>>' 开始，比如 >>>print 'Hello World!'

5. 命令行标准输出将以如下标示：

>>>>>>

输出内容

<<<<<<

比如：

>>>>>>

Hello World!

<<<<<<

6. 注释会以 ‘#’ 开始

 

建议

1. 将教程中的命令敲到python中看看效果

2. 你可以在了解之后立即去查看相关的更完备的内容

=== Python基础教程01 Hello World ===
=== Python基础教程02 基本数据类型 ===
=== Python基础教程03 序列 ===
=== Python基础教程04 运算 ===
=== Python基础教程05 缩进和选择 ===
=== Python基础教程06 循环 ===
=== Python基础教程07 函数 ===
函数最重要的目的是方便我们重复使用相同的一段程序。

将一些操作隶属于一个函数，以后你想实现相同的操作的时候，只用调用函数名就可以，而不需要重复敲所有的语句。

1.函数的定义
首先，我们要定义一个函数, 以说明这个函数的功能。
<pre class="brush: python;">
def square_sum(a,b):
c = a**2 + b**2    # 这一句是函数内部进行的运算
return c         # 返回c的值，也就是输出的功能。Python的函数允许不返回值，也就是不用return。
</pre>

这个函数的功能是求两个数的平方和。首先，def，这个关键字通知python：我在定义一个函数。square_sum是函数名。括号中的a, b是函数的参数，是对函数的输入。参数可以有多个，也可以完全没有（但括号要保留）。

我们已经在循环和选择中见过冒号和缩进来表示的隶属关系。
           
return可以返回多个值，以逗号分隔。相当于返回一个tuple(定值表)。

return a,b,c         #相当于 return (a,b,c)

 

在Python中，当程序执行到return的时候，程序将停止执行函数内余下的语句。return并不是必须的，当没有return, 或者return后面没有返回值时，函数将自动返回None。None是Python中的一个特别的数据类型，用来表示什么都没有，相当于C中的NULL。None多用于关键字参数传递的默认值。

 

2.函数的调用和参数传递

定义过函数后，就可以在后面程序中使用这一函数

print square_sum(3,4)
Python通过位置，知道3对应的是函数定义中的第一个参数a， 4对应第二个参数b，然后把参数传递给函数square_sum。

（Python有丰富的参数传递方式，还有关键字传递、表传递、字典传递等，基础教程将只涉及位置传递）

函数经过运算，返回值25, 这个25被print打印出来。

 

我们再看下面两个例子
<pre class="brush:python">
a = 1
def change_integer(a):
a = a + 1
return a
print change_integer(a)
print a
#===(Python中 "#" 后面跟的内容是注释，不执行 )
b = [1,2,3]
def change_list(b):
b[0] = b[0] + 1
return b
print change_list(b)
print b
</pre>
第一个例子，我们将一个整数变量传递给函数，函数对它进行操作，但原整数变量a不发生变化。

第二个例子，我们将一个表传递给函数，函数进行操作，原来的表b发生变化。

对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，从而不影响原来的变量。（我们称此为值传递）

但是对于表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，在函数中对表的操作将在原有内存中进行，从而影响原有变量。 （我们称此为指针传递）

总结：
<pre class="brush: python">
def function_name(a,b,c):
statement
return something  # return不是必须的
</pre>

函数的目的： 提高程序的重复可用性。
return     None
通过位置，传递参数。
基本数据类型的参数：值传递
表作为参数：指针传递

 

练习：

写一个判断闰年的函数，参数为年、月、日。若是是闰年，返回True

=== Python基础教程08 面向对象的基本概念 ===
（面向对象并不难，不要被“面向对象”吓跑）

Python中通过使用类(class)和对象(object)来实现面向对象（object-oriented programming，简称OOP）的编程。

面向对象编程的最主要目的是提高程序的重复使用性，这和函数的目的相类似。

我们这么早切入面向对象编程的原因是，Python的整个概念是基于对象的。了解OOP对于我们深入了解Python很关键。

下面是我对面向对象的理解。

1. 类是属性相近的对象的归类

在人类认知中，会根据属性相近把东西归类，并且给类别命名。比如说，鸟类的共同属性是有羽毛，通过产卵生育后代。任何一只特别的鸟都在鸟类的原型基础上的。

面向对象就是模拟了以上人类认知过程。在Python语言，为了听起来酷，我们把上面说的“东西”称为对象（object）。

先定义鸟类
<pre class="brush:python">
class Bird(object):
have_feather = True
way_of_reproduction = 'egg'
</pre>
我们定义了一个类别（class），就是鸟（Bird）。在隶属于这个类比的语句块中，我们定义了两个变量，一个是有羽毛（have_feather），一个是生殖方式（way_of_reproduction）,这两个变量对应我们刚才说的属性（attribute）。我们暂时先不说明括号以及其中的内容，记为问题1。

假设我养了一只小鸡，叫summer。它是个对象，属于鸟类。使用前面定义的类。

<pre class="brush:python">
summer = Bird()
print summer.way_of_reproduction
</pre>
通过第一句创建对象，并说明summer是类别鸟中的一个对象，summer就有了鸟的类属性，对属性的引用是通过 对象.属性（object.attribute） 的形式实现的。

（可怜的summer，你就是个有毛产蛋的东西，好不精致） 

2. 属性可以是变量，也可以是动作（方法）。

在人类日常认知中，我们在通过属性识别类别的时候，有时候会根据这个东西能做什么事情来区分类别。比如说，鸟会移动 （这样就和房屋的类别区分开了）。而这些动作又会带来一定的结果，通过移动会带来位置的变化。

为了酷起见，我们叫这样的一些属性为方法（method）。Python中通过在类的内部定义函数，来说明方法。

<pre class="brush:python">
summer = Bird()
class Bird(object):
   have_feather = True
   way_of_reproduction = 'egg'
def move(self, dx, dy):
position = [0,0]
position[0] = position[0] + dx
position[1] = position[1] + dy
return position

summer = Bird()
print 'after move:',summer.move(5,8)
</pre>
我们重新定义了鸟这个类别。

鸟新增一个方法属性，就是移动（函数move）。（我承认这个方法很傻，你可以在看过下一讲之后定义个有趣些的方法）

（它的参数中有一个self，它是为了方便我们引用对象自身。方法的第一个参数必须是self，无论是否用到。有关self的内容会在下一讲展开）

另外两个参数，dx, dy表示在x、y两个方向移动的距离。move方法会最终返回运算过的position。

在最后调用move方法的时候，我们只传递了dx和dy两个参数，不需要传递self参数（因为self只是为了内部使用）。

（我的summer现在可以跑一下了） 

3. 类别本身还可以进一步细分成子类

比如说，鸟类可以进一步分成鸡，大雁，黄鹂。

在OOP中，我们通过继承(inheritance)来表达上述概念。

<pre class="brush:python">
summer = Bird()
class Chicken(Bird):
way_of_move = ‘walk’
possible_in_KFC = True

class Oriole(Bird):
way_of_move = 'fly'
possible_in_KFC = False

summer = Chicken()
print summer.have_feather
print summer.move(5,8)
</pre>
我们新定义的鸡（Chicken）类的，新增加了两个属性，移动方式（way_of_move）和可能在KFC找到（possible_in_KFC）

在类定义时，括号里改为了Bird，用来说明，Chicken是属于鸟类（Bird）的一个子类（酷点的说法，Chicken继承自Bird），而自然而然，Bird就是Chicken的父类。通过这个说明，Python就知道，Chicken具有Bird的所有属性。我们可以看到，尽管我只声明了summer是鸡类，它依然具有鸟类的属性（无论是变量属性have_feather还是方法属性move）

另外定义黄鹂(Oriole)类，同样继承自鸟类。这样，我们在有一个属于黄鹂的对象时，也会自动拥有鸟类的属性。

通过继承制度，我们可以避免程序中的重复信息和重复语句。如果我们分别定义两个类，而不继承自鸟类，那么我们就必须把鸟类的属性分别敲到鸡类和黄鹂类的定义中，累啊。

（回到问题1, 括号中的object，当括号中为object时，说明这个类没有父类（到头了））

所以说，面向对象提高了程序的可重复使用性。

我们可以看到，面向对象实际上基于人类认知时的习惯，将各种各样的东西分类，从而了解世界。我们从祖先开始可能已经练习了这个认知过程有几百万年，所以面向对象是很符合人类思维习惯的编程方法。所谓面向过程（也就是执行完一个语句再执行下一个）实际上是机器思维。通过面向对象的编程，我们实际上是更贴近我们自然的思维方式，也更方便和其他人交流我们程序里所包含的想法，甚至于那个人并不是程序员。

总结：

- 将东西根据属性归类 ( 将object归为class )
- 方法是一种属性，表示动作
- 用继承来说明父类-子类关系。子类自动具有父类的所有属性。
- self代表了根据该类定义而创建的对象。
- 定义类：
<pre class="brush:python">
summer = Bird()
class class_name(parent_class):
a = ...
b = ...
def method1():
...
def method2():
...
</pre>
- 建立对一个对象： 对象名 = 类名()
- 引用对象的属性： object.attribute

=== Python基础教程09 面向对象的进一步拓展 ===
上一讲我们熟悉了对象和类的基本概念。这一讲我们将进一步拓展，以便我们真正能实际运用对象和类。

1. 在方法内调用类属性（变量以及其它方法）：

上一讲我们已经提到，在定义方法时，必须有self这一参数，这个参数指的是对象。由于对象拥有类的所有性质，那么我们就可以在方法内部通过self来调用类的其它属性。
<pre class="brush:python">
class Human(object):
laugh = 'hahahaha'
def show_laugh(self):
print self.laugh
def laugh_100th(self):
for i in range(100):
self.show_laugh()
li_lei = Human()              # 李雷
li_lei.laugh_100th()
</pre>
我们这里有一个变量属性laugh，在方法show_laugh()中通过self.laugh被调用。方法show_laugh则在laugh_100th中通过self.show_laugh()被调用。

（在方法中更改类变量属性的值是危险的，这样会影响根据这个类定义的所有对象的这一属性！！）

2. __ init __()方法

__ init __()是一个特殊方法(special method)。Python里会有一些特殊方法，Python会以特别的方式处理它们。特殊方法的名字的特点是前后都有两个下划线。

__ init __()方法的特殊在于，如果你在类中定义了这个方法，一旦你根据这个类建立对象，Python就会自动调用这个方法（这个过程也叫初始化）。（在上一讲中，我们手动调用了move()方法）
<pre class="brush:python">
class happyBird(Bird):
def __init__(self,more_words):
print 'We are happy birds.',more_words
summer = happyBird('Happy,Happy!')
</pre>
（Bird类的定义见上一讲）

屏幕上打印出： We are happy birds.Happy,Happy!

我们看到，尽管我们只是创建了summer对象，但__ init __()方法被自动调用了。最后一行的语句(summer = happyBird...)先创建了对象，然后执行：

    summer.__init__(more_words)

'Happy,Happy!' 被传递给了__ init __()的参数more_words

3. 对象的性质

上一讲我们讲了变量属性和方法属性。要注意，这些属性是类的属性。所有属于一个类的对象都会共享这些属性。比如说，鸟都有羽毛，鸡都不会飞。

在一些情况下，我们需要用到对象的性质。比如说，人是一个类别，我们知道，性别是人类的一个性质，但并不是所有的人类都是男性或者所有的人类都是女性。这个性质的值会随着对象的不同而不同。（李雷是人类的一个对象，性别是男；韩美美也是人类的一个对象，性别是女）。

从上一讲中，我们已经知道了，当定义类的方法时，必须要传递一个self的参数。这个参数指代的就是类的一个对象。当然，这是一个很模糊的一个概念。但一旦我们用类来新建一个对象（比如说我们下面例子中的li_lei）, 那么li_lei就是self所代表的东西。我们已经知道了，li_lei会拥有Human类的属性。进一步，我们通过赋值给self.attribute，给li_lei这一对象增加一些性质（比如说性别）。由于self强制传递给各个方法，方法可以通过引用self.attribute很方便地查询到这些性质，并进行进一步的操作。

这样，我们在类的属性统一的基础上，又给每个对象增添了各自特色的性质，从而能描述多样的世界。
<pre class="brush:python">
class Human(object):
def __init__(self, input_gender):
self.gender = input_gender
def printGender(self):
print self.gender
...
li_lei = Human('male') # 这里，'male'作为参数传递给__init__()方法的input_gender变量。
print li_lei.gender
li_lei.printGender()
</pre>
首先，在初始化中，将参数input_gender赋值给对象li_lei的性质gender。（上一讲，我们已经提到，self指示的是对象, 也就是li_lei）

我们发现，li_lei拥有了属性gender。在类human的定义中，并没有这样一个变量属性。Python是在建立了li_lei这一对象之后，专门为li_lei建立的属性。我们称此为对象的性质。（也有人以类属性，对象属性来区分）。

对象的性质也可以被其它方法调用，正如我们在printGender方法中所看到的那样。

 

总结：

通过self调用类属性

__ init __(): 在建立对象时自动执行

类属性和对象的性质的区别


=== Python基础教程10 反过头来看看 ===

Python进阶01 词典

Python进阶02 文本文件的输入输出

Python具有基本的文本文件读写功能。Python的标准库提供有更丰富的读写功能。

文本文件的读写主要通过open()所构建的文件对象来实现。

1. 打开文件，创建文件对象。

f = open(文件名，模式)

最常用的模式有：

"r"     # 只读

“w”    # 写入

 

2. 文件对象的方法：

读取方法：

content = f.read(N)          # 读取N bytes的数据

content = f.readline()       # 读取一行

content = f.readlines()     # 读取所有行，储存在表中，每个元素是一行。


写入方法：

f.write('I like apple')      # 将'I like apple'写入文件

f.write(list)                    # 将一个包含有多个字符串的表写入文件，每个元素成为文件中的一行。

 

关闭文件：

f.close()

 

3. 循环读入文件：

for line in file(文件名):    print line
利用file()函数，我们创建了一个循环对象。在循环中，文件的每一行依次被读取，赋予给line变量。

 

总结：

f = open(name, "r")

line = f.readline()

f.write('abc')

f.close()

for line in file(name): ...

Python进阶03 模块

我们之前看到了函数和对象。从本质上来说，它们都是为了更好的组织已经有的程序，以方便重复利用。

模块(module)也是为了同样的目的。在Python中，一个.py文件就构成一个模块。通过模块，你可以调用其它文件中的程序。

 

1. 引入(import)和使用模块

我们先写一个first.py文件，内容如下：

def laugh():    print 'HaHaHaHa'
再写一个second.py

import firstfor i in range(10):    first.laugh()
在second.py中，我们并没有定义laugh函数，但通过从first中引入(import)，我们就可以直接使用first.py中的laugh函数了。

 

从上面可以看到，引入模块后，我们可以通过 模块.对象 的方式来调用所想要使用的对象。上面例子中，first为引入的模块，laugh()是我们所引入的对象。

此外，还有其它的引入方式, import a as b, from a import *， 都是处于方便书写的原因，本质上没有差别。

 

2. 搜索路径

Python会在以下路径中搜索它想要寻找的模块：

1. 程序所在的文件夹

2. 标准库的安装路径

3. 操作系统环境变量PYTHONPATH所包含的路径

 

如果你有自定义的模块，或者下载的模块，可以根据情况放在相应的路径，以便python可以找到。

 

3. 模块包

可以将功能相似的模块放在同一个文件夹（比如说dir）中，通过

import dir.module
的方式引入。

 

注意，该文件夹中必须包含一个__init__.py的文件，以便提醒python知道该文件夹为一个模块包。__init__.py可以是一个空文件。

 

总结

import module

module.object

__init__.py



Python进阶04 函数的参数对应


Python进阶05 循环设计


Python进阶06 循环对象


Python进阶07 函数对象


Python进阶01 词典
Python进阶01 词典
Python进阶01 词典
Python进阶01 词典


