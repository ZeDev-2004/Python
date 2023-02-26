#Leia 4 valores inteiro. A, B, C, D 
#se B for maior do que C.
#E se D for maior do que A. 
#E a soma de C com D for maior que a soma de A e B.
#E se C e D, ambos, forem positivos.
#E se a viariável A for par. Escreva a mensagem "Valores aceitos", se não escrever "Valores não aceitos."

A, B, C, D = input().split(' ')

A = int(A)
B = int(B)
C = int(C)
D = int(D)

#Números para mim guadar. 
#F = int 
#G = int

if B > C and D > A  and  C + D > A + B  and C > 0 and D > 0 and A %2 == 0 : 
    print ('Valores aceitos')
else:
    print ('Valores nao aceitos')



#Fiquei maluco resolvendo isso aqui. Quase coringuei!
