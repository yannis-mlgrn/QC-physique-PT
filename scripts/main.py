import generateurEvalCours
from InquirerPy import inquirer
from InquirerPy.separator import Separator

def chaptersChoice(_):
    return [
        "Chapitre B1 - Le champ electrostatique",
        "Chapitre B4 - Le champ magnétostatique",
        Separator(),
        "Chapitre C1 - Statique des fluides",
    ]

def main() :
    chapters = inquirer.checkbox(
        message="Selectionner le ou les chapitres à réviser",
        choices=chaptersChoice,
        validate=lambda result: len(result) >= 1,
        invalid_message="Vous devez selectionner au moins 1 chapitre",
        instruction="(selectionner au moins 1 chapitre)",
    ).execute()
    chapters = createListPath(chapters)

    nombresDeQuestions = inquirer.number(message="Nombres de question:", default=0, instruction="(Toutes les questions : 0)").execute()
    if nombresDeQuestions == '0' : # Je sais c'est sale mais ça marge (à modifier)
        nombresDeQuestions = 9999
    generateurEvalCours.create_and_build_latex(chapters, int(nombresDeQuestions))
    
def createListPath(L: list) -> list:
    chapter_paths = {
        'Chapitre B1 - Le champ electrostatique': '../Cours/PartieB/CHAPB1-Le_champ_electrostatique.tex',
        'Chapitre B4 - Le champ magnétostatique': '../Cours/PartieB/CHAPB4-Le_champ_magnetostatique.tex',
        'Chapitre C1 - Statique des fluides': '../Cours/PartieC/CHAPC1-Statique_des_fluides.tex',
    }
    return [chapter_paths[chapter] for chapter in L if chapter in chapter_paths]



if __name__ == "__main__":
    main()