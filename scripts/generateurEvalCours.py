import subprocess
import os
import random
import re
import argparse

def create_and_build_latex(latex_filenames, num_questions=None):
    # Lire le contenu de plusieurs fichiers LaTeX
    latex_code_input = ""
    for latex_filename in latex_filenames:
        with open(latex_filename, "r") as f:
            latex_code_input += f.read() + "\n"

    questions = extract_questions(latex_code_input)
    chapter_title = extract_title(latex_code_input)
    
    if num_questions is None or num_questions > len(questions):
        num_questions = len(questions)
    random_questions = random.sample(questions, num_questions) if num_questions < len(questions) else questions
    
    latex_code = rf"""
\documentclass{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage{{amsmath}}
\usepackage{{mathrsfs}}
\usepackage{{enumitem}} 
\usepackage{{environ}}  
\usepackage{{ifthen}}   
\usepackage{{subfiles}} 
\usepackage[top=2cm, bottom=1.5cm, left=1.5cm, right=1.5cm]{{geometry}}
\newboolean{{showsolutions}}

% Définir un environnement pour les solutions
\NewEnviron{{solution}}{{
    \ifthenelse{{\boolean{{showsolutions}}}}{{
        \noindent\textbf{{Solution :}} 
        \BODY
    }}{{}}
}}
\begin{{document}}
% Affichage des questions de cours
\section*{{\centering\huge {chapter_title}}}
\setboolean{{showsolutions}}{{False}}
\begin{{enumerate}}[label=\arabic{{enumi}} - , left=0pt, itemsep=1em]
{''.join(random_questions)}
\end{{enumerate}}
\newpage
\section*{{\centering\huge Réponses :}}
\setboolean{{showsolutions}}{{True}}
\begin{{enumerate}}[label=\arabic{{enumi}} - , left=0pt, itemsep=1em]
{''.join(random_questions)}
\end{{enumerate}}
\end{{document}}
"""

    filename = "../Output/Test-de-connaissance.tex"
    
    # Créer le fichier LaTeX
    with open(filename, "w") as f:
        f.write(latex_code)

    # Compiler le fichier LaTeX
    build_latex(filename)

def extract_title(latex_code_input):
    title_match = re.search(r"\\section\*\{\\centering\s*(.*?)\}", latex_code_input)
    if title_match:
        return title_match.group(1)
    return "Évaluation de cours"

def extract_questions(latex_code_input):
    questions = []
    in_enumerate = False
    current_question = []

    for line in latex_code_input.splitlines():
        if "\\begin{enumerate}" in line:
            in_enumerate = True
        elif "\\end{enumerate}" in line:
            in_enumerate = False
            if current_question:
                questions.append("\n".join(current_question))
                current_question = []
        elif in_enumerate:
            if "\\item" in line and current_question:
                questions.append("\n".join(current_question))
                current_question = [line]
            else:
                current_question.append(line)

    if current_question:
        questions.append("\n".join(current_question))

    return questions

def build_latex(filename: str):
    output_directory = '../Output/'
    try:
        # Compiler le fichier LaTeX avec pdflatex
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory",output_directory, filename], check=True)
        
        # Si le fichier contient des sous-fichiers, il est recommandé de relancer la compilation
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-output-directory", output_directory, filename], check=True)
        
        print(f"Compilation de {filename} terminée avec succès.")
    except subprocess.CalledProcessError:
        print(f"Erreur lors de la compilation de {filename}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générer une évaluation de connaissance")
    parser.add_argument("-f", "--files", nargs='+', required=True, help="Liste des fichiers .tex à utiliser.")
    parser.add_argument("-nq", "--num_questions", type=int, nargs='?', default=None, help="Nombre de questions à tirer au hasard.")
    args = parser.parse_args()

    create_and_build_latex(args.files, num_questions=args.num_questions)