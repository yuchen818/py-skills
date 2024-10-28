# 學號判斷

## Description

台大學號的規則為英文字母開頭，接上八個數字，英文字母代表不同的身份別，前兩位數字代表入學年份。

舉例來說，B89109039 中 B 代表學士班， 89 代表 89 學年度入學。

身份簡易來說可以分成三種， B 代表學士班，R 代表碩士班，D 代表博士班。

請你寫一個程式，判斷該學號同學的年級為何。

## Input

輸入為一個字串，代表一個學號。

## Output

輸出有兩行。

第一行為該學號的身份別。

第二行為該學號的年級（以 110 學年度為基準），年級最多可為七年級。

## Sample Input / Output

```py
B08502018
學士班
三年級
```
```py
R10922074
碩士班
一年級
```
```py
D04922047
博士班
七年級
```

## Hint

題目以 110 學年度為基準：

sample input 1 為 108 學年度入學，故為三年級。

sample input 2 為 110 學年度入學，故為一年級。

sample input 3 為 104 學年度入學，故為七年級。