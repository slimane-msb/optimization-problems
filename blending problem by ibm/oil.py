import pulp

print ("oil")

def optimize_me(crudes, gasolines, costs, subs, prod):
    # variable names: 
    var_names =  [crude["name"] for crude in crudes]
    var_names += [gasoline["name"] for gasoline in gasolines]
    for gasoline in gasolines: 
        var_names += [gasoline["name"]+crude["name"] for crude in crudes]
    var_names += ["a"+gasoline["name"] for gasoline in gasolines]

    # variables: 
    variables = pulp.LpVariable.dicts(
        "Var", var_names, lowBound=0, cat=pulp.LpInteger
    )
    prob = pulp.LpProblem("faster_pb", pulp.LpMaximize)


    # contraintes: 
        # alpha: 
    for crude in crudes: 
        prob += pulp.lpSum(variables[crude["name"]] ) <=  crude["max"]

        # beta : 
    for gasoline in gasolines: 
        prob += pulp.lpSum(variables[gasoline["name"]] ) >= gasoline["max"]+prod["ads_incr"]*var_names["a"+gasoline["name"]]

        # gama : 
    prob += pulp.lpSum(variables[crude["name"]] for crude in crudes ) <=  prod["max_prod"]

        # sigma o: sup
    for sub in subs:
        for gasoline in gasolines: 
            prob += pulp.lpSum(sub["dir"]*crude[sub["name"]]*var_names[gasoline["name"]+crude["name"]] for crude in crudes ) >=  sub["dir"]*gasoline[sub["name"]]

    # fonction objective 
        # sell 
    prob += pulp.lpSum( gasoline["prix"]*variables[gasoline["name"]]  for gasoline in gasolines )
        # purchase 
    prob += pulp.lpSum( (-1)*crude["prix"]*variables[crude["name"]]  for crude in crudes )
        # ads 
    prob += pulp.lpSum( (-1)*costs["ads"]*variables["a"+gasoline["name"]]  for gasoline in gasolines )
        # production 
    prob += pulp.lpSum( (-1)*costs["production"]*variables[crude["name"]]  for crude in crudes )



    # pulp solve: 
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    for v in [variables[v_name] for v_name in var_names]:
        print(v, v.value())


    

optimize_me (
    crudes =[
        dict ( name = "c1" , octane = 12 , lead = 0.5 ,  price = 45 , max = 5000) ,
        dict ( name = "c2" , octane = 6  , lead = 2   ,  price = 35 , max = 5000) ,
        dict ( name = "c3" , octane = 8  , lead = 3 ,    price = 25 , max = 5000) ,
    ] ,

    gasolines =[
        dict ( name = "super"    , octane = 10 , lead = 1 , price = 70 , max = 3000) ,
        dict ( name = "regular"  , octane = 8  , lead = 2 , price = 60 , max = 2000) ,
        dict ( name = "diesel"   , octane = 6  , lead = 1 , price = 50 , max = 1000) ,
    ] ,
    costs = dict ( ads = 1 , production = 4),
    subs = [
        dict ( name = "octane", dir = 1),
        dict ( name = "lead"  , dir = -1),
    ], 
    prod = dict ( ads_incr = 10, max_prod = 14000 )
)