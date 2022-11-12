import pulp

print ("oil")

def optimize_me(crudes, gasoline, costs, subs):
    return 1

optimize_me (
    crudes =[
        dict ( name = "c1" , octane = 12 , lead = 0.5 ,  price = 45 , max = 5000) ,
        dict ( name = "c2" , octane = 6  , lead = 2   ,  price = 35 , max = 5000) ,
        dict ( name = "c3" , octane = 8  , lead = 3 ,    price = 25 , max = 5000) ,
    ] ,

    gasoline =[
        dict ( name = "super"    , octane = 10 , lead = 1 , price = 70 , max = 3000) ,
        dict ( name = "regular"  , octane = 8  , lead = 2 , price = 60 , max = 2000) ,
        dict ( name = "diesel"   , octane = 6  , lead = 1 , price = 50 , max = 1000) ,
    ] ,
    costs = dict ( ads = 1 , production = 4),
    subs = ["octane", "lead"]
)