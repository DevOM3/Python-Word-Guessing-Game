
print("\n\t\t\tWord Guessing Game\n\n")
word='helloworld'
w='h e l l o w o r l d'
x=w.split()
g=''
l=[]

name=input("Enter your name :\t")
print("Welcome "+name,". Press Enter key to continue")
input()

print(f"The length of word is : {len(word)}")
for i in word:
    print("_",end=" ")
print("\n")


print("\nYou have 10 chances , Enter your guesses...........\nAll the Best !!!")
for i in range(1,11):
    guess = input(f"\nChance {i} : Enter your Guessed letter :\t")
    g += guess

    for j in word:
        if j in g:
            print(j,end=" ")
            l.append(j)
            m = l[(len(l) - len(x)):len(l)]
            # print(l)
            # print(m)
            # print(x)
            if x == m:
                print(f"\n\nWooohhh!! You guessed it right !!! It was \t{word} \nCongratulations !!! You won")
                exit()
        else:
            print("_",end=" ")

m = l[(len(l) - len(x)):len(l)]
if x != m:
    print(f"\n\nShit !!! Your guesses were wrong , Sorry , but you lost the game ......\nThe word was {word}")





