import pulp

print ("sudoku")

def optimize_me(n):
    var_names = []
    for i in range(9): 
        for j in range(9): 
            for k in range(9):
                var_names.append(f"x{i}{j}{k}")

    print(var_names)
    variables = pulp.LpVariable.dicts(
        "Var", var_names, lowBound=0, upBound= 1, cat=pulp.LpInteger
    )

    prob = pulp.LpProblem("faster_pb", pulp.LpMaximize)

    # case de base: 
    prob += variables["x123"] ==1


    # contraintes lines: 
    for c in range(9): 
        for l1 in range(9): 
                prob += pulp.lpSum( variables["x"+str(l1)+str(c)+str(k)]  for k in range(9)) ==1

    # contraintes column: 
    for l in range(9): 
        for c1 in range(9): 
            prob += pulp.lpSum( variables["x"+str(l)+str(c1)+str(k)]  for k in range(9)) ==1
                

    # contraintes region:
    for lr in range(3):
        for cr in range(3):
            for l1 in range(3):
                for c1 in range(3):
                    x1 = lr*3+l1
                    y1 = cr*3+c1
                    prob += pulp.lpSum( variables["x"+str(x1)+str(y1)+str(k)]  for k in range(9)) ==1

                            
                            



    prob.solve(pulp.PULP_CBC_CMD(msg=True))
    print(prob)
    for v in [variables[v_name] for v_name in var_names]:
       if v.value() :
         print(v, v.value())



optimize_me (9)

