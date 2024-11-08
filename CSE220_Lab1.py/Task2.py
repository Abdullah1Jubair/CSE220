#Discard Cards
import numpy as np

def discardCards(cards, t):
    occurrence_count = 0
    n = len(cards)
    
    for i in range(n):
        if cards[i] == t:
            occurrence_count += 1    
            if occurrence_count % 2 == 1:  
                cards[i] = 0  
    
    index = 0  
    for i in range(n):
        if cards[i] != 0:  
            cards[index] = cards[i]
            index += 1
        
    for i in range(index, n):
        cards[i] = 0

    return cards  

cards = np.array([1, 3, 7, 2, 5, 2, 2, 2, 0])
print(discardCards(cards, t=2))
print(type(cards))
