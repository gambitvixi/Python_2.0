# Prvo, inportujem potrebne module i definisem sebi tablu za igranje, logicno
from random import randint

board = []

# Naravno, posto si lazy af, kreira ti je komp a ne ti sam

for i in range (5):
    board.append(["0"]*5)

# A sada i da je pravilno prikazemo

def print_board(board):
    for i in board:
        print (" ".join(i))

#Znaci .join() dodas nesto stringu
#Sada postavljamo brodic negdje da ga imamo gadjati

def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board)-1)

#Sada da komp sakrije svoj brodic negdje

boat_row = random_row(board)
boat_coll = random_col(board)
print (boat_row + 1)
print (boat_coll + 1)
#Da ne moram svak put kucati ovo.....
#Ok idiote, nauci ovo, NIKADA NE DAVAJ ISTA IMENA funkcijama i varijablama!!!!
def guess_rowf():
    guess_row = int(input("Pogodi red? "))
    guess_row -= 1
    return guess_row

def guess_collf():
    guess_coll = int(input("Pogodi kolonu? "))
    guess_coll -= 1
    return guess_coll

guess_row = guess_rowf()
guess_coll = guess_collf()

#Ovdje koristis or jer ti je bitno da oba budu true jer ova ebena petlja
#radi dok je uslov True, zar ne? Ok, valjda kontam sada.
while guess_row != boat_row or guess_coll != boat_coll:
    print ("Luzeru!")
    board[guess_row][guess_coll]= "x"
    print_board(board)
    print ("Probaj opet!")
    guess_row = guess_rowf()
    guess_coll = guess_collf()
else:
    print ("To jebacu, pogodio si")

#U sustini primjer je gotov. Moze se uzeti sada npr jos doraditi.
#Ubaciti da provjeri da li si dobro unjeo, ograniciti broj pokusaja
#i takve zajebancije, ali za danas dosta