from get_dict import get_dict
from get_R_Q import initial_R
from get_R_Q import initial_Q
from get_result import get_result

import time

n = int(input('\nEnter number of nodes: '))
source=input('\nEnter Starting node: ')
destination = input('Enter Destination node: ')
dest = ord(destination)-65

R = {}
for i in range(n):
    node = [x for x in input('Enter nodes connected to '+str(chr(i+65))+': ').strip()]
    weight = [int(x) for x in input('Enter weights: ').split(',')]
    wt = {}
    for c,col in enumerate(node):
        idx = ord(col)-65
        wt[ord(col)-65+1] = weight[c]
    #R[chr(i+65)] = wt    
    R[i+1] = wt    


print(R)

Q = initial_Q(R)

print(Q)

#start = 1
start = ord(source)-65+1
#end = [9]
end = [ord(destination)-65+1]

alpha = 0.7 # learning rate
epsilon = 0.1 #greedy policy
n_episodes = 1000

t0 = time.time()
result = get_result(R,Q,alpha,epsilon,n_episodes,start,end)
print("time is:",time.time() - t0)

'''
print(result["ends_find"])
print(result["routes_number"])
'''
print('Minimum distance: {}'.format(result["cost"]))

optimum_path = [chr(x+65) for x in result["all_routes"]]

print('Optimum path: ',end = '')
print(optimum_path)