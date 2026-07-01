############################# TICk - Tac Game ################################
L1=[" ","|"," ","|"," "]
L2=["-","-","-","-","-"]
L3=[" ","|"," ","|"," "]
L4=["-","-","-","-","-"]
L5=[" ","|"," ","|"," "]

def tick_tac_game(play,symbol):
    list_posit=play[:2]
    posit=int(play[2])
    
    if list_posit == "L1":
        L1[posit]=symbol
    elif list_posit == "L3":
        L3[posit]=symbol
    elif list_posit == "L5":
        L5[posit]=symbol
    

    print("".join(L1))
    print("".join(L2))
    print("".join(L3))
    print("".join(L4))
    print("".join(L5))
    print("_____________________________")
    print("")

for turns in range(0,9):
    with open("tick_tac.txt") as file:
        print(file.read())
    
    if turns in [0,2,4,6,8]:
        play=input("Enter Player 'X', position: ")
        tick_tac_game(play,symbol="X")
    else:
        play=input("Enter Player '0', position: ")
        tick_tac_game(play,symbol="0")
    
    winnerX="Player X is Winner"
    winner0="Player 0 is Winner"

'''
    flagX = False
    flag0 = False

    for i in (L1,L3,L5):
        c1=0
        c2=0
        for j in (0,2,4):
            if i[j] == "X":
                c1+=1
                if c1 == 3:
                    flagX = True
            elif i[j] == "0":
                c2+=1
                if c2 == 3:
                    flag0 = True

    if flagX:
        print(winnerX)
        break
    elif flag0:
        print(winner0)
        break


'''
    if L1[0]=="X" and L1[2]=="X" and L1[4]=="X":
        print(winnerX)
        break
    elif L1[0]=="0" and L1[2]=="0" and L1[4]=="0":
        print(winner0)
        break
    elif L3[0]=="X" and L3[2]=="X" and L3[4]=="X":
        print(winnerX)
        break
    elif L3[0]=="0" and L3[2]=="0" and L3[4]=="0":
        print(winner0)
        break
    elif L5[0]=="X" and L5[2]=="X" and L5[4]=="X":
        print(winnerX)
        break
    elif L5[0]=="0" and L5[2]=="0" and L5[4]=="0":
        print(winner0)
        break
    elif L1[0]=="X" and L3[0]=="X" and L5[0]=="X":
        print(winnerX)
        break
    elif L1[0]=="0" and L3[0]=="0" and L5[0]=="0":
        print(winner0)
        break
    elif L1[2]=="X" and L3[2]=="X" and L5[2]=="X":
        print(winnerX)
        break
    elif L1[2]=="0" and L3[2]=="0" and L5[2]=="0":
        print(winner0)
        break
    elif L1[4]=="X" and L3[4]=="X" and L5[4]=="X":
        print(winnerX)
        break
    elif L1[4]=="0" and L3[4]=="0" and L5[4]=="0":
        print(winner0)
        break
    elif L1[0]=="X" and L3[2]=="X" and L5[4]=="X":
        print(winnerX)
        break
    elif L1[0]=="0" and L3[2]=="0" and L5[4]=="0":
        print(winner0)
        break

'''
print("".join(L1))
print("".join(L2))
print("".join(L3))
print("".join(L4))
print("".join(L5))
'''
