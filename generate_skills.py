import sys

tab = "\t"

languages = {
    "Bash": 3,
    "C\\#": 3,
    "JavaScript": 2,
    "C": 5,
    "MatLab": 2,
    "PHP": 2,
    "C++": 4,
    "Java": 5,
    "Python": 4
}

libraries = {
    "CUDA": 4,
    "Keras": 1,
    "OpenGL": 3,
    "MPI": 4,
    "OpenMP": 4,
    "Scikit-learn": 3
}

other = {
    "CSS": 3,
    "\\LaTeX": 4,
    "XML": 3,
    "HTML": 2,
    "Markdown": 3,
    "YAML": 2,
    "JSON": 2,
    "SQL": 3
}

software = {
    "BitBucket": 1,
    "Eclipse": 2,
    "GitLab": 1,
    "Poetry": 3,
    "Visual Studio": 2,
    "Blender": 3,
    "Git": 4,
    "Gradle": 3,
    "PyCharm": 3,
    "Docker": 3,
    "GitHub": 3,
    "Intellij IDEA": 3,
    "\\TeX Studio": 3
}

legend = {
    "ita": [
        "Nessuna esperienza",
        "So leggere un programma e utilizzare le funzionalità di base",
        "Conosco alcune funzionalità avanzate e posso applicare piccole modifiche a programmi esistenti",
        "Posso realizzare semplici programmi senza bisogno di aiuto e so risolvere i problemi più comuni",
        "Posso integrare nuove funzionalità a sistemi già esistenti",
        "Posso realizzare da zero un sistema complesso",
        "Conoscenza completa e approfondita"
    ],
    "eng": [
        "No experience",
        "Can read a program and use most basic features",
        "Know some advanced features and can apply small changes to existing programs",
        "Can develop simple programs without help and solve most common problems",
        "Can integrate new features into existing systems",
        "Can design and develop a system from scratch",
        "Complete and deep knowledge"
    ]
}

def check_dict(d):
    if type(d) is not dict:
        raise TypeError(d, "is not a dictionary")
    for k,v in d.items():
        if type(v) is not int:
            raise TypeError("Value of key", k, "is not int")
        if v <= 0 or v > 6:
            raise ValueError("Invalid value for key", k)

def print_legend(lang, indent=""):
    print(indent+"\\begin{table}[!ht]")
    print(indent+tab+"\\begin{tabular}{cl}")

    for i, s in enumerate(legend[lang]):
        print(indent+tab+tab+"\\drawbar{"+str(i)+"} & "+s+"\\\\")

    print(indent+tab+"\\end{tabular}")
    print(indent+"\\end{table}")

def print_skills(title, d, indent=""):
    print(indent+"\\subsection*{"+title+"}")
    keys = [k for k in d]
    list.sort(keys)
    split_keys = [[], [], []]
    i = 0
    for k in keys:
        split_keys[i].append(k)
        i = (i+1)%3
    
    for i, l in enumerate(split_keys):
        print(indent+tab+"\\begin{minipage}[t]{.3\\textwidth}")
        for k in l:
            print(indent+tab+tab+k+" \\hfill \\drawbar{"+str(d[k])+"}\\\\")
        print(indent+tab+"\\end{minipage}")
        if i != 2:
            print(indent+tab+"\\hfill")
    print(indent+"")

def generate(lang):
    section = {
        "ita": "Competenze",
        "eng": "Skills"
    }

    legend_name = {
        "ita": "Legenda autovalutazione competenze",
        "eng": "Skill self-evaluation scale"
    }

    titles = {
        "prog": {
            "ita": "Linguaggi di programmazione",
            "eng": "Programming languages"
        },
        "lib": {
            "ita": "Librerie/Framework",
            "eng": "Libraries/Frameworks"
        },
        "other": {
            "ita": "Altri linguaggi",
            "eng": "Other languages"
        }
    }

    print("\\documentclass[curriculum-vitae-"+lang+"]{subfiles}\n")
    print("\\begin{document}")
    print(tab+"\\section*{"+section[lang]+"}")
    print(tab+tab+"\\textbf{"+legend_name[lang]+"}")
    print_legend(lang, indent=tab+tab+tab)
    print("")
    print_skills(titles["prog"][lang], languages, indent=tab+tab)
    print_skills(titles["lib"][lang], libraries, indent=tab+tab)
    print_skills(titles["other"][lang], other, indent=tab+tab)
    print_skills("Software", software, indent=tab+tab)
    print("\\end{document}", end="")

def main():
    for d in [languages, libraries, other, software]:
        check_dict(d)
    
    old_stdout = sys.stdout
    
    # Italian
    with open("skills-ita.tex", "w") as f:
        sys.stdout = f
        generate("ita")
        sys.stdout = old_stdout

    # English
    with open("skills-eng.tex", "w") as f:
        sys.stdout = f
        generate("eng")
        sys.stdout = old_stdout

if __name__ == "__main__":
    main()