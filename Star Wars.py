class film:
    def __init__(self, a, b, c, d, e, f, g):
        self.titre=a
        self.annee=b
        self.episode=c
        self.cout=d
        self.recette=e
        self.collection=f
        self.calculbenefice=g

    def get__titre(self):
        return self.titre

    def get__annee(self):
        return self.annee

    def get__episode(self):
        return self.episode

    def get__cout(self):
        return self.cout

    def get__recette(self):
        return self.recette

    def get__collection(self):
        return self.collection

    def get__calculbenefice(self):
        return self.calculbenefice

    def __str__(self):
        return "le montant du bénéfice est de " + self.calculbenefice

    def __str__(self):
        return "le film s appelle " + self.titre


class acteur:
    def __init__(self, a, b, d, e, c=[]): # "c=[]" attribut duet de personnage pour un acteur
        self.nom=a
        self.prenom=b
        self.duet=c
        self.nbpersonnages=d
        self.nbacteurs=e

    def get__nom(self):
        return self.nom

    def get__prenom(self):
        return self.prenom

    def get__nbpersonnages(self):
        return self.nbpersonnages

    def get__nbacteurs(self):
        return self.nbacteurs #retourne le nombre d’acteurs du film

    def list_str(self): #élément de désignation de l'objet courant
        tmp=" " #reprend la chaine de caractère déjà présente
        for i in self.nbpersonnages:
            tmp=tmp+" "+i.__str__()
        return tmp

    def __str__(self):
        return "les acteurs sont " + self.nom + self.prenom+" "+ self.list_str()

class personnages:
    def __init__(self, a, b):
        self.nom=a
        self.prenom=b

    def get__nom(self):
        return self.nom

    def get__prenom(self):
        return self.prenom

    def __str__(self):
        return "les personnages sont " + self.nom +" "+ self.prenom

g=calculbenefice
g=e
z=acteur("Harison","Ford",[])

f1=film("Star Wars", "1978", "2", "122 000", "345 000",[f],[g])
print(f1)

a=(input("entrez le titre du film:"))
b=(input("entrez l annee de sortie:"))
c=(input("entrez le nom de l episode:"))
d=(input("entrez le cout du film:"))
e=(input("entrez la recette du film:"))

p3=personnages("Dark", "Vador")
p4=personnages("Maitre", "Yoda")
p5=personnages("Will", "Smith")
p6=personnages("Been", "James")

a1=acteur("Daisy"," Ridley",[p3],[p4]) #code pour créer un acteur incarnant deux personnages
print(a1)
a2=acteur("John"," Snow",[p5],[p6])
print(a2)

p1=input("entrez le nom du personnage:")
p2=input("entrez le prenom du personnage:")
print("les personnages sont "+ p1 +" "+ p2)
a3=personnages(p1, p2)


def mystere(l): #afficher les éléments d'une liste. on peut choisir autre chose que mystere
    for elt in l:
        print(elt)

#l=[a1, a2, a3]

list=[a1, a2, a3]
mystere(list)