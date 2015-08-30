---
layout: wiki
title: code
date: 2014-12-08
update: 2014-12-08
---

OJ系统的基本输入语句：

/*
這本來的某考上大學的非資訊社同學問我的，剛好有空就把它整理出來
以下是一些我臨時想到的，歡迎補充。
這些對論壇中大部人已經是基礎了吧~不過我想對下一屆學弟還是有用的。
我自己是習慣用 cin 和 string 來做 input，雖然有些題目真的需要用 scanf 速度上才過得了…
但 scanf 跟我不是很熟，怕誤導學弟，就等其它人來寫了。
以下都以例子來說明。
註：這些寫法不是唯一的，存在著許多不同寫法可以有同樣效果。

目錄：
1. 單筆測資 (int)
2. 單筆測資 (string)
3. 多筆測資：單行
4. 多筆測資：多行
5. 指令式輸入
6. string 整行輸入
7. 如何處理多餘字元
*/

/*
1. 單筆測資 (int)
單筆測資，測資只有一行，有兩個 int，請輸出兩數之和。
# Sample Input:
-1 2
# Sample Output:
1
*/
#include <iostream>
using namespace std;

int main() {
    int a, b;
    while (cin >> a >> b) {
        cout << (a+b) << endl;
    }
        
    return 0;
}

/*
2. 單筆測資 (string)
單筆測資，測資只有一行，該行有兩個英文單字（保證只有英文字母），以空白作分隔。
若兩個單字完全相等，輸出 "yes"（不含引號），若不相等，輸出 "no"（不含引號）
# Sample Input:
math science
# Sample Output:
no
*/
#include <iostream>
using namespace std;

int main() {
    string a, b;
    // string 也適用 cin
    cin >> a >> b;
    cout << ((a == b) ? "yes": "no") << endl;
    
    return 0;
}

/*
3. 多筆測資：單行
多筆測資，每筆測資只有一行，每行有兩個相異整數，皆為 int。
每筆測資請輸出較大的正整數。
# Sample Input:
2 5
-4 8
-1 11
# Sample Output:
5
8
11
*/
#include <iostream>
using namespace std;

int main() {
    int a, b;
    while (cin >> a >> b) {
        cout << max(a, b) << endl;
    }
    
    return 0;
}

/* 
4. 多筆測資：多行
給你 n 個相異英文單字（保證只含英文字母），請將這 n 個單字依字典順序排序後輸出。
多筆測資，每筆測資第一行為一個小於 100 的正整數，代表 n。之後 n 行為英文單字。每筆測資之間不含空白行。
輸出為每個單字一行。測資與測資之間不需加空白行。
# Sample Input:
3
python
cpp
haskell
2
java
csharp
# Sample Output:
cpp
haskell
python
csharp
java
*/
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;
    string data[100];
    
    while (cin >> N) {
        // input
        for (int i=0; i<N; i++)
            cin >> data[i];
        
        sort(data, data+N);
        
        // output
        for (int i=0; i<N; i++)
            cout << data[i] << endl;
    }
    return 0;
}

/*
5. 指令式輸入
Input 除最後一行外皆為以下格式：
command a b
command 可能為 max 或 min，a, b 保證為 int
此時請依 command 輸出 a, b 的較大者或較小者。
Input 的最後一行為
quit
代表程式結束
# Sample Input:
max 3 5
min 3 6
min 7 110
max 2 6
quit
# Sample Output:
5
3
7
6
*/
#include <iostream>
using namespace std;

int main() {
    string cmd;
    while (cin >> cmd) {
        if (cmd == "quit") break;
        
        int a, b;
        cin >> a >> b;
        
        if (cmd == "max")
            cout << max(a, b) << endl;
        else    // cmd = "min"
            cout << min(a, b) << endl;
    }
    
    return 0;
}

/*
6. string 整行輸入
多筆測資，每筆測資只有一行，請反轉該行後輸出。
# Sample Input
test time tokyo
reverse -1
# Sample Output
oykot emit tset
1- esrever
*/
#include <iostream>
#include <algorithm>

int main() {
    string inp;
    while (getline(cin, inp)) {
        reverse(inp.begin(), inp.end());
        cout << inp;
    }
    
    return 0;
}

/*
7. 如何處理多餘字元
常有題目的 input 會出現不需要的字元，例如：
多筆測資，每筆資只有一行,格式為：
a, b
保證 a, b 為 int，請輸出較大者。
# Sample Input:
2, 3
-4, -1
# Sample Output:
3
-1
此時我們可以利用 cin 讀入時的特性：會根據變數來決定讀入的內容。
先讀入一個 int 再讀入一個字元把逗號吃掉，再讀入一個 int，這樣就可以正確的讀入了。
*/
#include <iostream>
using namespace std;

int main() {
    int a, b;
    char comma;
    while (cin >> a >> comma >> b) {
        cout << max(a, b) << endl;
    }
    return 0;
}

## algorithm
1. sort(a,a+10)
