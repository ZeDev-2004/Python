#Jogo da adivinhação 
#tente vencer o Gênio da adivinhação!

import random 

ale = random.randrange(1 , 5) 

print ("Digite um número de 0 a 5 e tente adivinhar o gênio da adivinhação!\n")

dig = int (input ()) 

if (ale == dig ): 

    print ("Você acertou! Eu escolhi o número {} \n".format(ale))
else: 
    while (ale != dig ): 

        print ("Você errou. O número que eu pensei foi {} \n".format ( ale )) 

        ale = random.randrange(1, 5 ) 
        
        print ("tente novamente!\n ") 
        print ("Digite um número! "); dig = int (input ()) 
        print ("Parabéns! você acertou! o número que eu pensei foi {} ".format(ale))
        