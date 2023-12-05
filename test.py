if __name__ == '__main__':
    x = int(1)
    y = int(1)
    z = int(1)
    n = int(2)
    
    L1 = [a for a in range(x+1) if a <= x]
    L2 = [a for a in range(y+1) if a <= y]
    L3 = [a for a in range(z+1) if a <= z]  

    possibilities = [[i,j,k] for i in L1 for j in L2 for k in L3]
    posscoord = []
    for poss in possibilities:
        if sum(poss) != n:
            posscoord.append(poss)
    print(posscoord)
            
    # posscoord = []
    # num = 0
    # for number in range(n+1):
    #     possibilities = [i[num],j[num],k[num]]
    #     num =+ 1
    #     posscoord.append(possibilities)
    # print(posscoord)

    
    