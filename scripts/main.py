import generateurEvalCours
from InquirerPy import inquirer
from InquirerPy.separator import Separator

def chaptersChoice(_):
    return [
        "Chapitre A1 - Stabilité des systèmes linéaires",
        "Chapitre A2 - Rétroaction",
        "Chapitre A3 - Oscillateurs",
        Separator(),
        "Chapitre B1 - Le champ electrostatique",
        "Chapitre B2 - Circulation du champ electrostatique",
        "Chapitre B3 - Flux du champ électrostatique",
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
        "Chapitre A1 - Stabilité des systèmes linéaires": '../Cours/PartieA/CHAPA1-Stabilite_des_systemes_lineaires.tex',
        "Chapitre A2 - Rétroaction" : '../Cours/PartieA/CHAPA2-Retroaction.tex',
        "Chapitre A3 - Oscillateurs" : '../Cours/PartieA/CHAPA3-Oscillateurs.tex',
        'Chapitre B1 - Le champ électrostatique': '../Cours/PartieB/CHAPB1-Le_champ_electrostatique.tex',
        "Chapitre B2 - Circulation du champ électrostatique": '../Cours/PartieB/CHAPB2-Circulation _du_champ_electrostatique.tex',
        "Chapitre B3 - Flux du champ électrostatique": '../Cours/PartieB/CHAPB3-Flux_du_champ_electrostatique.tex',
        'Chapitre B4 - Le champ magnétostatique': '../Cours/PartieB/CHAPB4-Le_champ_magnetostatique.tex',
        'Chapitre C1 - Statique des fluides': '../Cours/PartieC/CHAPC1-Statique_des_fluides.tex',
    }
    return [chapter_paths[chapter] for chapter in L if chapter in chapter_paths]



if __name__ == "__main__":
    main()