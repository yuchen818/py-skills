# 直角三角形

## Description

我們知道，當三角形的三個邊 a、b、c 符合邊長 c^2 = a^2 + b^2，那麼這三個邊可以組成一個 ab 夾角為直角的三角形。

## Input

輸入為兩行，第一行包含一個正整數 c。第二行包含正整數 y 和正整數 z。請判斷範圍在 y 跟 z 之間（包含 y 和 z，y 可能小於或大於 z），是否存在兩個整數 a, b 滿足 c^2 = a^2 + b^2。(即 c 為三角形長邊)

## Output

若存在則輸出 True，不存在輸出 False

## Sample Input / Output

```py
13
5 12

True
```
```py
3
5 7

False
```