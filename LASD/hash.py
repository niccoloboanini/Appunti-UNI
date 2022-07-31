from random import seed
from random import randint
import math

m = 8
n = 0
#T = [[] for _ in range(m)]

T1 = [[] for _ in range(m)]
T2 = [[] for _ in range(m)]

collisione_div = 0
collisione_mul = 0

def hashing_func_div(key):
	return key % m

def hashing_func_mul(key):
    A=(math.sqrt(5)-1)/2
    m=len(T2)
    return math.floor(m * ((key * A) %1))

def insert(key, value):
	hash_key = hashing_func_div(key)

	if len(T1[hash_key]) > 0:
	    global collisione_div
	    collisione_div = collisione_div + 1
	T1[hash_key].insert(0,value)

	hash_key = hashing_func_mul(key)	
	if len(T2[hash_key]) > 0:
	    global collisione_mul
	    collisione_mul = collisione_mul + 1
	T2[hash_key].insert(0,value)
	

	global n
	n = n + 1

def display_hash(T): 
    for i in range(len(T)):
        print("|",str(i).rjust(2, '0'),"|", end = "")  	
        
        for j in T[i]:
            print(" >", j , end = "")
        print()
    print()



insert(10,"Rossi")
insert(20,"Russo")
insert(30,"Ferrari")
insert(40,"Esposito")
insert(50,"Bianchi")
insert(60,"Romano")

insert(71,"Rossi")
insert(13,"Rossi")
insert(92,"Rossi")
insert(12,"Rossi")




display_hash(T1)
display_hash(T2)


print()
print("Metodo DIVISIONE       - Totale Collisioni: " , collisione_div, "\n")
print("Metodo MOLTIPLICAZIONE - Totale Collisioni: " , collisione_mul, "\n")
print("Fattore di carico (α=n/m): " , n , "/" , m, "=" , n/m , "\n")