# Blending problem by IBM

Presents the problem of calculating different blends of gasoline according to specific quality criteria.

Blending problems are another typical application of linear programming. Consider the following problem. An oil company manufactures three types of gasoline: super, regular, and diesel. Each type of gasoline is produced by blending three types of crude oil: crude1, crude2, and crude3. Table 1 below depicts the sales price and the purchase price per barrel of the various products. The gasoline must satisfy some quality criteria with respect to their lead content and their octane ratings, thus constraining the possible blendings.



## Prices for the blending problem

||Sales price|| purchase price|
|--|--|--|--|
|super| 70 $ | crude1| 45$|
regular | 60$ | crude2 | 35$|
disel | 50$ | crude3 | 25$|

## quality criteria with respect to their lead content and their octane ratings
||octane rating | Lead content | | octane rating | Lead content |
|--|--|--|--|--|--|
|super|>=10|<=1|crude1|12|0.5|
|regular|>=8|<=2|crude1|6|2|
|diesel|>=6|<=1|crude1|8|3|


## demand and ads : 
The company must also satisfy its customer demand, which is 3,000 barrels a day of super, 2,000 of regular, and 1,000 of diesel. The company can purchase 5,000 barrels of each type of crude oil per day and can process at most 14,000 barrels a day. In addition, the company has the option of advertising a gasoline, in which case the demand for this type of gasoline increases by ten barrels for every dollar spent. Finally, it costs four dollars to transform a barrel of oil into a barrel of gasoline.



# solving the problem with linear programming and Pulp : 

## sets : 
- C = {c1, c2, c3} for crudes
- G = {R, S, D} for gasoline 
- Q = {O,L} for quality criteria 

## variables 
- $n(b) \ such \ that \  b \in C \cup G \ with \ n(b) \ge 0$
- $m(g,c) \ tq \ c \in C \ and \ g \in G \ for \ number \ of \ c \ in \ g \ with \ m(g,c) \ge 0$
- $a(g) \ with \ g \in G \ for \ ads \ in \ g \ with \ a(g) \ge 0$

## objective function 

$$Max (Benifits) \ such \ that$$ 

$$Benifits \ = \ sell - purchase - ads - production$$ 

$$sell = 70 ns + 60 nr + 50 nd \ = \sum_{g \in G} price(g)\times ng$$ 

$$purchase = 45 nc1 + 35 nc2 + 25 nc3 \ = \sum_{c \in C} price(c) \times nc$$

$$ads= as + ar + ad = \sum_{g \in G} a(g)$$

$$production = 4 \times (nc1+nc2+nc3) = 4 \times \sum_{ c \in C} n(c)$$

## constraintes 
- alpha : 

$$nc1 \le 5k$$

$$nc2 \le 5k$$

$$nc3 \le 5k$$

- beta : 

$$ns \ge 3k+10 \times as$$

$$nr \ge 2k+10 \times ar$$

$$nd \ge 1k+10 \times ad$$

- gama : 

$$nc1+nc2+nc3 \le 14k$$

- sigma o: 

$$12 m(s,c1) + 6m(s,c2) + 8m(s,c3) \ge 10$$

$$12 m(r,c1) + 6m(r,c2) + 8m(r,c3) \ge 8$$

$$12 m(d,c1) + 6m(d,c2) + 8m(d,c3) \ge 6$$


- sigma L: 

$$0.5m(s,c1) + 2m(s,c2) + 3m(s,c3) \ge 1$$

$$0.5m(r,c1) + 2m(r,c2) + 3m(r,c3) \ge 2$$

$$0.5m(d,c1) + 2m(d,c2) + 3m(d,c3) \ge 1$$


-  omega : 


$$n(s) \times m(s,c1) + n(r) \times m(r,c1) + n(d) \times m(d,c1) \le n(c1)$$


$$n(s) \times m(s,c2) + n(r) \times m(r,c2) + n(d) \times m(d,c2) \le n(c2)$$

$$n(s) \times m(s,c3) + n(r) \times m(r,c3) + n(d) \times m(d,c3) \le n(c3)$$

 ## converting the problem into a linear problem : 
 $$let \ m'(g,c)= n(g) \times m(g,c)$$

- sigma o ': 

$$12 m'(s,c1) + 6m'(s,c2) + 8m'(s,c3) \ge 10 \times n(s)$$

$$12 m'(r,c1) + 6m'(r,c2) + 8m'(r,c3) \ge 8 \times n(r)$$

$$12 m'(d,c1) + 6m'(d,c2) + 8m'(d,c3) \ge 6 \times n(d)$$


- sigma L ': 

$$0.5m'(s,c1) + 2m'(s,c2) + 3m'(s,c3) \ge 1 \times n(s)$$

$$0.5m'(r,c1) + 2m'(r,c2) + 3m'(r,c3) \ge 2 \times n(r)$$

$$0.5m'(d,c1) + 2m'(d,c2) + 3m'(d,c3) \ge 1 \times n(d)$$


-  omega  ': 


$$m'(s,c1) + m'(r,c1) + m'(d,c1) \le n(c1)$$


$$m'(s,c2) + m'(r,c2) + m'(d,c2) \le n(c2)$$

$$m'(s,c3) + m'(r,c3) + m'(d,c3) \le n(c3)$$

