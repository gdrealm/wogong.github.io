---
layout: wiki
title: regex
date: 2014-10-21
update: 2014-10-21
---
正则表达式30分钟入门教程
<http://deerchao.net/tutorials/regex/regex.htm>


	\ 转义符

## metacharacter 元字符

	\b 代表着单词的开头或结尾，也就是单词的分界处。虽然通常英文的单词是由空格，标点符号或者换行来分隔的，但是\b并不匹配这些单词分隔字符中的任何一个，它只匹配一个位置。
	. 匹配除了换行符以外的任意字符。
	* 指定*前边的内容可以连续重复使用任意次以使整个表达式得到匹配。
	\d 匹配一位数字(0，或1，或2，或……)
	\s 匹配任意的空白符，包括空格，制表符(Tab)，换行符，中文全角空格等
	\w 匹配字母或数字或下划线或汉字等。
	^ 匹配字符串的开始
	$ 匹配字符串的结束

## 限定符

	* 重复零次或更多次
	+ 重复一次或更多次
	? 重复零次或一次
	{n} 重复n次
	{n,} 重复n次或更多次
	{n,m} 重复n到m次
