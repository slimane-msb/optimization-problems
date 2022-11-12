# optimization-problems
application of Pulp to implement a linear programming solution for optimization issues



# solving the  blending problem using linear programming and Pulp : 

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




