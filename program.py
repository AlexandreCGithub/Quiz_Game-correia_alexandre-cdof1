import os

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

    try:
        with open(fichier_quiz, "r") as file:
            lignes = file.readlines()
    except FileNotFoundError:
        print(f"Le fichier {fichier_quiz} n'a pas été trouvé.")
        return
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")
        return

    if len(lignes) == 0:
        print("Le fichier ne contient aucune question.")
        return

    for ligne in lignes:
        try:
            elements = ligne.strip().split(", ")
            question = elements[0]
            reponses = elements[1:-1]
            bonne_reponse = elements[-1]
            if poser_question(question, reponses, bonne_reponse):
                score += 1
            input("Appuyez sur Entrée pour continuer...")  # Attendez que l'utilisateur appuie sur Entrée
            os.system('cls' if os.name == 'nt' else 'clear')
        except IndexError:
            print("Erreur : Format de ligne incorrect dans le fichier.")
            return
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return

    print(f"Terminé. Votre score est de {score} sur {len(lignes)}")

if __name__ == "__main__":
    main()
