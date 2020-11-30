import random

randlist=['i n i t i a l i z e ','t e r m i n a t e ','m o u s e ','k e y b o a r d ','n o t e b o o k ','a p p l e ','d e s k t o p ','l a p t o p ','f o r w a r d ','r e l e a s e ','p r o j e c t o r ']
g=''
word=random.choice(randlist)
x=word.split()
l=[]
# print(word)

print("\n\t\t\tWord Guessing Game\n\n")
name=input("Enter your name :\t")
print("Welcome "+name,". Press Enter key to continue")
input()

print(f"The length of word is : {len(x)}")
for i in x:
    print("_",end=" ")
print("\n")


print("\nYou have 10 chances , Enter your guesses...........\nAll the Best !!!")
for i in range(1,11):
    guess = input(f"\nChance {i} : Enter your Guessed letter :\t")
    g += guess

    for j in x:
        if j in g:
            print(j, end=" ")
            l.append(j)
            m = l[(len(l) - len(x)):len(l)]
            # print(l)
            # print(m)
            # print(x)
            if x == m:
                print(f"\n\nWooohhh!! You guessed it right !!! It was \t{word} \nCongratulations !!! You won")
                exit()
        else:
            print("_", end=" ")

m = l[(len(l) - len(x)):len(l)]
if x != m:
    print(f"\n\nShit !!! Your guesses were wrong , Sorry , but you lost the game ......\nThe word was {word}")


