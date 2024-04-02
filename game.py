# rock paper scissor for time passs
import random

win =0
draws =0
loss=0
prompt="choose rock(r) paper(p) or scissor(s) or quit (q): "
while True:
    user = input(prompt)
    if user not in("r","p","s","q"):
        print("please choose one of above")
    # print (user)
    elif user == "q":
            break
    else:
        comp=random.choice(["r","p","s"])
        print (comp)
    
        if comp == user:
            print("draw")
            draws+=1
        elif (comp == "r" and user== "s") or (comp =="s" and user =="p") or (comp == "p" and user== "r"):
            print("you loose")
            loss+=1
        else:
            print("you win")
            win+=1
        
        print("total draws", draws, "\ntotal win", win ,"\ntotal losses",loss)
    
    
    
    
    
    
