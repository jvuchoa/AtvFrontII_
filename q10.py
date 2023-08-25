import random

def get_user_choice():
    while True:
        user_choice = input("Escolha Pedra, Papel ou Tesoura: ").lower()
        if user_choice in ["pedra", "papel", "tesoura"]:
            return user_choice
        else:
            print("Escolha inválida. Por favor, escolha entre Pedra, Papel ou Tesoura.")

def get_computer_choice():
    choices = ["pedra", "papel", "tesoura"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"
    elif (user_choice == "pedra" and computer_choice == "tesoura") or \
         (user_choice == "papel" and computer_choice == "pedra") or \
         (user_choice == "tesoura" and computer_choice == "papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

def main():
    print("Bem-vindo ao Pedra, Papel e Tesoura!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Você escolheu: {user_choice}")
    print(f"O computador escolheu: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    print(winner)

if __name__ == "__main__":
    main()