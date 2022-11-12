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

## constraintes 