import pulp
from itertools import product

print ("sudoku")

def optimize_me(n):
    prob = pulp.LpProblem("sudoku", pulp.LpMinimize)

    range9 = [i for i in range(9)]

    variables = pulp.LpVariable.dicts(
        "variables", (range9,range9,range9), cat=pulp.LpBinary
        )

    # sudoku: 
    prob += variables[0][1][7] == 1
    prob += variables[0][4][2] == 1
    prob += variables[0][7][0] == 1
    prob += variables[1][1][5] == 1
    prob += variables[1][8][3] == 1
    prob += variables[1][2][2] == 1
    prob += variables[2][2][8] == 1
    prob += variables[2][3][1] == 1

    # contraintes one int per zone : 
    for l in range(9): 
        for c in range(9): 
            prob += pulp.lpSum(variables[l][c][k] for k in range(9)) == 1 


    # contraintes lines: one int per line 
    for l,k in product(range(9),range(9)): 
            prob += pulp.lpSum( variables[l][c][k] for c in range(9)) == 1 

    # contraintes column: one int per column  
    for c,k in product(range(9),range(9)): 
            prob += pulp.lpSum( variables[l][c][k]  for l in range(9)) ==1
                

    # contraintes region: one in for region as c = (i%3)+3*(reg%3) and l = (i/3)+3*(reg/3) 
    for reg,k in product(range(9),range(9)): 
            prob += pulp.lpSum( variables[(i//3)+3*(reg//3)][(i%3)+3*(reg%3)][k] for i in range(9)) == 1                 

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    print_sudoku_from_plpvar(variables)
    # print_prob(prob=prob, lpvar=variables)  
    # print_prob_details(prob)   


def print_prob_details(prob):
    print("+", "-" * 78, "+", sep="")
    print(prob)


def print_prob(
    prob: pulp.LpProblem,
    lpvar = None,
    expr: pulp.LpAffineExpression = None,
):
    print("+", "-" * 78, "+", sep="")
    # print("Name", prob.name)
    # print("Status", pulp.LpStatus[prob.status])
    if pulp.LpStatusOptimal != prob.status:
        return   
    print_sudoku_from_plpvar(lpvar)



def print_sudoku_from_plpvar(lpvar): 
    for l in range(9):
        for c in range(9):
            for k in range(9): 
                if lpvar[l][c][k].value() :
                    print(k+1, end=" ") 
        print() 


optimize_me (9)

