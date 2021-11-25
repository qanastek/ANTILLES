import sys
import threading
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Transformation Conll to Conll++')
parser.add_argument('-corpus', type=str, default="UD_FRENCH", help='The input corpus')
parser.add_argument('-verbose', type=bool, default=False, help='Verbose')
args = parser.parse_args()

# CORPUS = "macaon2-conll"
CORPUS = "UD_FRENCH"

INPUT = "in/" + CORPUS + "/"

OUTPUT = "out/" + CORPUS + "/"
Path(OUTPUT).mkdir(parents=True, exist_ok=True)

DATA = {
    "macaon2-conll": {
        "dev": "ftb.dev.conll07",
        "test": "ftb.test.conll07",
        "train": "ftb.train.conll07",
    },
    "UD_FRENCH": {
        "dev": "fr_gsd-ud-dev.conllu",
        "test": "fr_gsd-ud-test.conllu",
        "train": "fr_gsd-ud-train.conllu",
    },
}

# Pronom Personnel
PPER = {
    "je": "PPER1S",
    "j'": "PPER1S",
    "tu": "PPER2S",

    "il": "PPER3MS",
    "l'": "PPER3MS",
    "elle": "PPER3FS",

    "nous": "PPER1P",
    "vous": "PPER2P",

    "ils": "PPER3MP",
    "elles": "PPER3FP",
}

# COI = {
#     "me": "PPOBJS",
# }

# Return the corresponding corpus
def get(name):
    return DATA[CORPUS][name]

# Process in a separated thread
def process(FILE):

    print(FILE)

    output_file = open(OUTPUT + FILE, "w")

    # Open It
    with open(INPUT + FILE) as f:

        # Read each line
        for line in f:

            # Split the line
            row = line.replace('\n','').split('\t')
            # print(row)

            if len(row) < 4:
                output_file.write(line)
                continue
            else:

                token = row[3]

                if args.verbose == True:
                    print("Before: " + token)

                if len(row) >= 6 and "Gender=" in row[5] and "Number=" in row[5]:

                    infos = dict(p.split('=') for p in row[5].split('|'))
                    # print(infos)

                    genre = infos["Gender"].upper()[0]
                    nombre = infos["Number"].upper()[0]

                    # Déterminant
                    if token == "DET":

                        if "Definite" in infos:

                            definite = infos["Definite"]

                            # Déterminant
                            if definite == "Def":
                                token = "DET" + genre + nombre

                            # Déterminant indéfini
                            elif definite == "Ind":
                                token = "DINT" + genre + nombre

                        # Pronom démonstratif
                        elif "PronType" in infos:

                            pronType = infos["PronType"]

                            # print(row)

                            if pronType == "Dem":
                                token = "PDEM" + genre + nombre

                    # Adjectifs
                    elif token == "ADJ":
                        token = "ADJ" + genre + nombre
                    
                    # Préposition
                    elif token == "ADP":
                        token = "PREP"

                    # Noms
                    elif token == "NOUN":
                        token = "N" + genre + nombre

                    # Pronom
                    elif token == "PRON":

                        pronType = infos["PronType"]

                        # Pronom démonstratif
                        if pronType == "Dem":
                            token = "PDEM" + genre + nombre

                        # Pronom indéfini
                        elif pronType == "Ind":
                            token = "PIND" + genre + nombre

                        # Pronom interrogatif
                        elif pronType == "Int":
                            token = "PINT" + genre + nombre

                        # Pronom relatif
                        elif pronType == "Rel":

                            # print("inside")
                            token = "PREL" + genre + nombre

                        # Pronom personnel
                        elif pronType == "Prs":

                            # print(row)

                            # Pronom personnel
                            if row[1].lower().replace('-','') in PPER:
                                token = PPER[row[1].lower().replace('-','')]

                            # Pronom objet
                            # clear && python transform.py | sort | uniq
                            else:
                                print("PPOBJ: " + row[1].lower())
                                token = "PPOBJ" + genre + nombre
                    # Verbe
                    elif token == "VERB":

                        verbForm = infos["VerbForm"]

                        # Particpe
                        if verbForm == "Part":

                            tense = infos["Tense"]

                            # Particpe passé
                            if tense == "Past":
                                token = "VPP" + genre + nombre

                            # Particpe présent
                            elif tense == "Pres":
                                token = "VPPRE"
            
                # Nombre
                elif token == "NUM":
                    token = "CHIF"

                # Conjonction de coordination
                elif token == "CCONJ":
                    token = "COCO"

                # Conjonction subordonnée
                elif token == "SCONJ":
                    token = "COSUB"
                    
                # Préposition
                elif token == "ADP":
                    token = "PREP"
            
                # Pronom
                elif token == "PRON":

                    # print(row)

                    infos = dict(p.split('=') for p in row[5].split('|'))
                    pronType = infos["PronType"]

                    # Pronom personnel
                    if pronType == "Prs":

                        # possPerson = infos["PossPerson"]

                        pronm = row[1].lower().replace('-','')

                        # Singulier
                        if pronm in ["me","m'","te","t'"]:

                            token = "PREFS"

                        # Pluriel
                        elif pronm in ["vous","nous"]:

                            token = "PREFP"

                        # s' et se
                        elif pronm in ["s'","se"]:

                            token = "PREF"

                        # Pronom personnel
                        elif pronm in list(PPER.keys()):

                            token = PPER[pronm] 
                            
                        # Pronom objet
                        # clear && python transform.py | sort | uniq
                        else:
                            print("PRN OBJ: " + pronm)
                            # print(row)
                            token = "PPOBJ" + genre + nombre

                        # if pronm == "me" or pronm == "m'":

                        #     token = "PREF"

                        # elif pronm == "me" or pronm == "m'":

                        # # Pronom réfléchi
                        # if int(possPerson) == 3:

                    # Pronom relatif
                    if pronType == "Rel":
                        token = "PREL"
                    
                # Nom de famille
                elif token == "PROPN":

                    flat = row[7]

                    if flat == "flat:name":
                        token = "XFAMIL"

                # Ponctuation
                elif token == "PUNCT":

                    punct = row[1]

                    if punct == "/":
                        token = "YPFAI"

                    elif punct == ".":
                        token = "YPFOR"

                # Motif inconnu
                elif token == "X":
                    token = "MOTINC"

                # else:
                #     print("Nothing changed")

                if args.verbose == True:
                    print("After : " + token + "\n")
                
                # row[4] = token
                row[3] = token

            output_line = str('\t'.join(row)) + "\n"
        
            output_file.write(output_line)
            # print(line)
            # print(output_line)

    # sys.exit(0)
    
    output_file.close()

# For each file
t1 = threading.Thread(target=process, args=(get("dev"),))
t1.start()

t2 = threading.Thread(target=process, args=(get("test"),))
t2.start()

t3 = threading.Thread(target=process, args=(get("train"),))
t3.start()

t1.join() 
t2.join() 
t3.join() 

print("Finished!")
