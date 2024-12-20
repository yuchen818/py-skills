# 小雷愛攀岩I

## Description

小雷很喜歡攀岩，這一天他來到了新的岩館想要大展身手，可是卻發現每一面的岩牆都有好多岩點，分別是屬於不同等級的路線，但小雷因為昨天熬夜寫報告而頭昏腦脹，想請你直接幫他判斷輸入的每一面牆中有幾條「完整的」路線呢？而那些路線分別又是多少等級的呢？

注意：

- 完整的路線代表每一列都要有那個等級的岩點
- 同一列可能有 > 1 個同等級的岩點
- 等級只有 V0 - V8
- 若該牆面沒有任何完整的路線則需輸出 'No valid route'

## Input

第 1 列為接下來會輸入的牆面寬、高 (x,y)，0 < x,y <= 10

第 2 ~ y+1 列為牆面，牆面上的每個數字都是一個岩點，岩點上的數字為其岩點的等級

## Output

1. 先輸出此牆面中有多少條完整的路線，

2. 再輸出分別屬於哪些等級（等級彼此間應該以'/'相隔，並從等級低至高排列）

3. 上面兩條輸出間應以分號';'相隔

4. 若沒有任何完整的路線則需輸出 'No valid route'

## Sample Input / Output

```py
4,6
1267
2317
1376
2713
7331
1726

2;V1/V7
```
```py
5,5
34563
56562
34563
34671
12344

No valid route
```