c,d=0,0
final_sys_score,final_usr_score=0,0
sys_bat,usr_bat=False,False
def usr_batting():
    global c,d
    global usr_bat
    usr_bat=True
    print("User Batting")
    while 1:
        a=int(input())
        if a>6:
            print("Enter 1-6")
        b=random.randint(1,6)
        print(b)
        if a<=6:
            if a!=b:
                c+=a
                # if c>d and d!=0:
                #     break
                if (sys_bat): 
                    if c>d: 
                        # print("Win")
                        break
                
            
            else:
                final_usr_score=c
                print("out")
                break
    print("your score is "+str(c))
    #return c

def sys_batting():  
    global d
    global sys_bat
    sys_bat=True
    print("System Batting")
    while 1:
        a=int(input())
        if a>6:
            print("Enter 1-6")
        b=random.randint(1,6)
        print(b)
        if a<=6:
            if a!=b:
                d+=b
                # if d>c and c!=0:
                #     break
                if (usr_bat):
                    if (d>c): 
                        break
            
            else:
                print("out")
                break
    print("System score is "+str(d))
    #return d 
def superover():
    for i in range(0,6):
            if st=="bat":            
                 usr_batting()
                 sys_batting()
            else:
                 sys_batting()
                 usr_batting()
    
st=input("choose bat or bowl\n")
if st=="bat":
    usr_batting()
    sys_batting()
elif st=="bowl":
    sys_batting()
    usr_batting()
        
if c>d:
    print("You win")
elif d>c:
    print("You lose")
else:
    print("Match tie")
    print("superover")
    superover()