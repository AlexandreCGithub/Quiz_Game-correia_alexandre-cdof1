import os
import random

def poser_question(question, reponses, bonne_reponse):
    print(question)
    for i, reponse in enumerate(reponses, start=1):
        print(f"{i}. {reponse}")

    while True:
        choix_utilisateur = input("Votre réponse (entrez le numéro) : ")
        if choix_utilisateur.isdigit() and 1 <= int(choix_utilisateur) <= len(reponses):
            choix_utilisateur = int(choix_utilisateur)
            break
        else:
            print('\033[93m' + "Veuillez entrer un numéro valide." + '\033[0m')

    if reponses[choix_utilisateur - 1] == bonne_reponse:
        print('\033[92m' + "Correct !\n" + '\033[0m')
        return True
    else:
        print('\033[91m' + f"Incorrect. La bonne réponse était : {bonne_reponse}\n" + '\033[0m')
        return False

def main():
    fichier_quiz = "questions_answers_list.txt"
    score = 0

    with open(fichier_quiz, "r") as file:
        lignes = file.readlines()[:10]  # Read only the first 10 lines

    num_questions = len(lignes)
    print(f"Le quiz contient {num_questions} questions.")

    random.shuffle(lignes)  # Shuffle the order of questions

    for ligne in lignes:
        elements = ligne.strip().split(", ")
        question = elements[0]
        reponses = elements[1:-1]
        bonne_reponse = elements[-1]
        if poser_question(question, reponses, bonne_reponse):
            score += 1
        input("Appuyez sur Entrée pour continuer...")  # Wait for user to press Enter
        os.system('cls' if os.name == 'nt' else 'clear')

    print("Terminé. Votre score est de " + str(score) + " sur " + str(num_questions))

if __name__ == "__main__":
    main()

