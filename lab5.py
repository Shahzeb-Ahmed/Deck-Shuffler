import random

def deck(categories, num_of_cards_per_cat):
    """
    (list, int) -> list
    Given a list of strings representation as category names and an integer
    indicating the number of cards in one category,
    return a deck of cards as a list. For example, with ["spades", "hearts"], 2,
    return a list of list: [["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]],
    where 1 and 2 are the index of the cards.
    """
    length = len(categories)
    num = int(num_of_cards_per_cat)
    deckList = []
    final = []
    if num >= 1:
        for i in categories:
            for x in range(1,num + 1):
                deckList.append((i,x))
        for a in range(0,length*num):
            final.append(list(deckList[a]))
    else:
        final = []
    return final


def random_shuffle(lst):
    """
    (list) -> list
    Receives a deck of cards and returns a randomly ordered
    list containing all of the same elements.
    The returned list should preserve the order of the categories. See below
    console outputs as an example, where "s" and "d" stay in the same order as
    the input and only the numbers are shuffled.
    >> random_shuffle([["s",1],["s",2],["s",3],["d",1],["d",2],["d",3]])
    [["s",3],["s",1],["s",2],["d",2],["d",1],["d",3]]
    """  
    if len(lst) == 1:
        final = lst
    for i in range(len(lst)-1):
        
        if lst[i][1] == lst[i+1][1]:
            final = lst
    
        else:
            
            dic = {}
            for i in lst:
                if i[0] not in dic:
                    dic[i[0]] = [i[1]]
                else:
                    dic[i[0]].append(i[1])
            
            
            final = []
            for i in lst:
                final.append([i[0]])
                
                
            num = []
            for i in dic:
                num.append(dic[i])
            
            
            shuff = []
            def shuffle(num):
                for i in num:
                    shuff.append(random.sample(i,len(i)))
                return shuff
            
            shuffle(num)
            
            for i in range(len(shuff)):
                while shuff[i] == num[i]:
                    shuff[i] = random.sample(num[i],len(num[i]))
                
            
            sub = []
            for i in shuff:
                sub.extend(i)
                
            for i in range(len(final)):
                final[i].append(sub[i])
    return final



def reverse(lst):
    """
    (list) -> list
    Receives a list and returns a reverse ordered list containing all of the same elements.
    >> reverse([["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]])
    [["hearts", 2], ["hearts", 1], ["spades", 2],["spades",1]]
    """
    final = []
    final.extend(lst[::-1])
    return final