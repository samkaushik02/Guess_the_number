#made_by_sameer_kaushik
print("===>>>  GUESS  THE  NUMBER  <<===\n")
import random
import math
com=random.randint(0,1024)
l=math.log(int(com),2)
a=math.floor(l)
b=math.ceil(l)
x=2**int(a)
y=2**int(b)
count=0
no=int(b)
while True:
        if count<=a:
                print("You have " +str(no)+" chances")
                guess=input("Guess the number between "+str(x)+" and "+str(y)+" : ")
                print("")
                if com>int(guess):
                        x=guess
                        no=no-1
                        count=count+1
                elif com<int(guess):
                        y=guess
                        no=no-1
                        count=count+1
                else:
                        print(str(com)+" is the number")
                        break
        else:
                print("!!! -> NO MORE CHANCES <- !!!!")
                print(">>> GAME OVER <<<")
