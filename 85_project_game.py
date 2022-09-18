import random
# Snake,Water & Gun Game :-
def gamewin(comp,me):
    if comp==me:
        return None
    elif comp=="s":
        if me=="w":
            return False
        elif me=="g":
            return True

    elif comp=="w":
        if me=="g":
            return False
        elif me=="s":
            return True

    elif comp=="g":
        if me=="s":
            return False
        elif me=="w":
            return True

print("comp turn: snake(s) water(w) gun(g)?")
randno=random.randint(1,3)
if randno==1:
    comp="s"
elif randno==2:
    comp="w"
elif randno==3:
    comp="g"

me=input("my turn: snake(s) water(w) gun(g)? ")
a=gamewin(comp,me)

print(f"Computer chose {comp}")
print(f"Me chose {me}")

if a==None:
    print("The game is a tie!")
elif a:
    print("Me Win!")
else:
    print("Me Lose!")