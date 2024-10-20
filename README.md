# Questions de cours de physique-chimie au programme pour la classe préparatoire scientifique PT :
>  programme de la banque PT de l'année 2024-2025

- Les questions de cours sont accessible [ici](Output/QCphysique.pdf)

## Utilisation des scripts de générations de contrôles de connaissances :

### 1- Installation :
**Prérequis : Vous devez avoir installé  [pdflatex](https://gist.github.com/rain1024/98dd5e2c6c8c28f9ea9d)**

Se rendre dans le dossier scripts :
```bash
cd scripts
```
Création d'un environnement virtuel ( faculatif ):
```bash
python -m venv .venv
source .venv/bin/activate
```
Installation des dépendances python:
```bash
pip install -r requirements.txt
```

### 2- Utilisation :
#### génération via le menu de configuration ( le plus simple) :
lancer le script principal
```bash
python main.py 
```

#### generateurEvalCours.py :

```bash
python generateurEvalCours.py -f fichier.tex -nq nombre-de-questions

```
exemple : 
```bash
python generateurEvalCours.py -f ../Cours/PartieC/CHAPC1-Statique_des_fluides.tex -nq 4
```
sinon lancer le programme avec l'argument --help


