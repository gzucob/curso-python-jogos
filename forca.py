def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:

        chute = input(str("Digite ume letra: ")) 
        
        for letra in palavra_secreta:
            if  chute == letra:
                print(chute)

        print("Jogando...")    

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
