import random
print("start to play")
b,d,i=0,0,0
for i in range(0,10):
    a=str(input())
    #print(a)
    list=['rock','paper','scissor']
    c=random.choice(list)
    print(c)
    if a=='rock'and c=='paper':
        d+=1
        print("d="+str(d))
    elif a=='rock' and c=='scissor':
        b+=1
        print("b="+str(b))
    elif a=='paper' and c=='rock':
        b+=1
        print("b="+str(b))
    elif a=='paper' and c=='scissor':
        d+=1
        print("d="+str(d))
    elif a=='scissor' and c=='rock':
        d+=1
        print("d="+str(d))
    elif a=='scissor' and c=='paper':
        b+=1  
        print("b="+str(b))  

    
    i+=1    
print("your score is "+str(b))
print("system score is "+str(d))
if b>d:
    print("You win")
elif d>b:
    print("You lose")
else:
    print("Match tie")