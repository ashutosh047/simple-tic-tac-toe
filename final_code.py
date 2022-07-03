# write your code here
#functions for counting
def x_count(arr):
    ctr=0
    for i in arr:
        for j in i:
            if(j=='X'):
                ctr+=1
    return ctr
def o_count(arr):
    ctr=0
    for i in arr:
        for j in i:
            if(j=='O'):
                ctr+=1
    return ctr
def e_count(arr):
    ctr=0
    for i in arr:
        for j in i:
            if(j=='_'):
                ctr+=1
    return ctr
#functions for checking rows or columns or diagonals
def xo_check(arr):
    ctr1=0
    ctr2=0
    for i in arr:
        if(i=='X'):
            ctr1+=1
        elif(i=='O'):
            ctr2+=1
    if ctr1==3:
        return 0
    elif ctr2==3:
        return 1
    else:
        return 2
def e_check(arr):
    ctr=0
    for i in arr:
        if(i=='_'):
            ctr+=1
    if ctr==3:
        return 2

#function for checking state of game
def check_state(l):
    flag=0
    ch=1
    res=[]
    while (ch!=9):
        m=[]
        for i in range(3):
            for j in range(3):
                if((ch==1)and(i==0)):
                    m.append(l[i][j])
                    
                elif((ch==2)and(i==1)):
                    m.append(l[i][j])
                    
                elif((ch==3)and(i==2)):
                    m.append(l[i][j])
                    
                elif((ch==4)and(j==0)):
                    m.append(l[i][j])
                    
                elif((ch==5)and(j==1)):
                    m.append(l[i][j])
                    
                elif((ch==6)and(j==2)):
                    m.append(l[i][j])
                    
                elif((ch==7)and(i==j)):
                    m.append(l[i][j])
                    
                elif((ch==8)and((i+j)==2)):
                    m.append(l[i][j])
                    
                
        res.append(xo_check(m))
        ch+=1
    """if((abs(x_count(l)-o_count(l))>=2) or ((0 in res) and (1 in res))):
        print('Impossible')
        return 0"""
    if 0 in res:
        print('X wins')
        flag=1
    elif 1 in res:
        print('O wins')
        flag=1
    elif(((x_count(l)+o_count(l))==9)and(e_count(l)==0)):
        print('Draw')
        flag=1
    else:
        #print("executed ELSE")
        return flag
    """elif(e_count(n)!=0):
        print('Game not finished')
        return 0"""
    return flag
#======================================================#
#main program
n=['_' for x in range(9)]
print('---------')
print('|',n[0],n[1],n[2],'|')
print('|',n[3],n[4],n[5],'|')
print('|',n[6],n[7],n[8],'|')
print('---------')
l=[[0 for j in range(3)]for i in range(3)]
k=0
for i in range(3):
    for j in range(3):
        l[i][j]=n[k]
        k+=1
turn=0
while(check_state(l)!=1):
    flag=0
    #for 1 turn
    while(flag!=1):
        m=input().split(" ")
        try:
            if((ord(m[0])>=ord('0'))and(ord(m[1])<=ord('9'))):
                x=int(m[0])-1
                y=int(m[1])-1
                if(x>2 or y>2 or x<0 or y<0):
                    print('Coordinates should be from 1 to 3!')
                elif(l[x][y]!='_'):
                    print('This cell is occupied! Choose another one!')
                else:
                    if(turn==0):
                        l[x][y]='X'
                        flag=1
                        turn=1
                    elif(turn==1):
                        l[x][y]='O'
                        flag=1
                        turn=0
            else:
                print("You should enter numbers!")
        except TypeError as err:
            print("You should enter numbers!")

    print('---------')
    print('|',l[0][0],l[0][1],l[0][2],'|')
    print('|',l[1][0],l[1][1],l[1][2],'|')
    print('|',l[2][0],l[2][1],l[2][2],'|')
    print('---------')
