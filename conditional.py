# Here its used IF, Elif and else
# lets see an example:

Idade = 17
AcompanhadoPais = True
PodeVerFilme18 = False

if Idade > 18:
    not PodeVerFilme18
    print("Can watch the movie by yourself! :3 ")
elif Idade < 18 and AcompanhadoPais == True:
    not PodeVerFilme18
    print("Can watch the movie, since its with parents. :3 ")
else:
    PodeVerFilme18
    print("Cant watch the movie :(")
    
# Here i used a simple example of cases built in a conditional case if else
# Where it bases the user if he can watch a movie thats 18 rated, and checks its age
# And if its with parents!


# Here its just a simple example oof the use 'break', that its a stop condition in codes;
contador = 0

while True:
    print( contador, "esta aumentando!")
    contador += 1

    if contador == 3:
        break


# Now lets see the use of 'Continue'

for odd_numbers in range(10):

    if odd_numbers % 2 == 0:
        continue
    print(odd_numbers)
    # the code will just print the odd numbers, because when it hits the even number
    # it tells the computer to jump to the next iteration