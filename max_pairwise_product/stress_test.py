# Uses python3
import random
from fn_find_max_prod import find_max_prod
from fn_find_max_prod_starter import find_max_prod_starter

ok = True
tries = 0
while ok & (tries < 100):
    n = random.randint(0, 20)
    a = []
    for i in range (0,n):
        a.append(random.randint(0,100000))
    x = find_max_prod(n,a)
    my_result = x[0]
    top = x[1]
    top2 = x[2]
    starter_result = find_max_prod_starter(n,a) 
    tries += 1
    ok = (my_result == starter_result)
    
print("My result: {}".format(my_result))
print("My factors: {} {}".format(top, top2))
print("Starter result: {}".format(starter_result))
print(sorted(a, reverse=True))
print("Number of tries: {}".format(tries))      

