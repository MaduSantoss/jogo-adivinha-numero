from random import randint

print("----- Jogo de Adivinhação! -----")

numero_secreto = randint(1, 100)

while True:
    try:
        palpite = int(input("\nTente adivinhar o número entre 1 e 100: "))
        
        if palpite < numero_secreto:
            print("\nMuito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("\nMuito alto! Tente novamente.")  
        else:
            print("Parabéns! Você adivinhou o número secreto.")
            break
    
    except ValueError:
        print("\nPor favor, insira um número válido.")
    
print("Fim do jogo.")
        

