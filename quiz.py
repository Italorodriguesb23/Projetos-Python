print("Seja muito bem vindo ao quiz!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 1

print("Começando...")
print("Quem é o cantor conhecido como rei do pop? \n (A) Michael Jackson \n (B) Elton Jhon \n (C) Bruno Mars \n (D) Prince \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é o maior país do mundo?\n (A) Brasil \n (B) Russia \n (C) Canadá \n (D) Holanda \n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é o jogador que mais vezes conquistou a copa do mundo?\n (A) Messi \n (B) Buffon \n (C) Pelé \n (D) Romário \n")
answer_3 = input("Resposta: ")

if answer_3 == "BC":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual cientista é conhecido como o descobridor da gravidade?\n (A) Isaac Newton \n (B) Albert Einstein \n (C) Robert Oppenheimer \n (D) Stephen Hawking \n")
answer_4 = input("Resposta: ")

if answer_4 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print(f"Quiz acabou... Pontuação: {score}/4")