import numpy as np
def mergeLineup(pokemon1,pokemon2):
    n = len(pokemon1)
    array3 = np.zeros(n,dtype= int)
    
    for i in range(n//2):
        pokemon2[i],pokemon2[n-1-i] = pokemon2[n-1-i],pokemon2[i]
    for i in range(n):
        if pokemon1[i] != None:
            array3[i] += pokemon1[i]
        if pokemon2[i] != None:
            array3[i] += pokemon2[i]
        
    return array3
    print(array3)
    
    



pokemon_1= [4, 5, -1, None, None]
pokemon_2= [2, 27, 7, 12, None]
print(mergeLineup(pokemon_1, pokemon_2))

