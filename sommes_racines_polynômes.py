# calcul des différentes sommes des racines d'un polynôme
print("Salut cher utilisateur\nPar ce programme nous calculerons les différentes sommes des racines d'un \npolynôme grace à la formule de viet")
deg=int(input("entrez le degré de votre polynôme: "))
liste=[]
print("Maintenant vous allez entrer les coefficients suivant les puissances croissantes\nC'est à dire du dernier coefficient au premier coefficient de votre polynôme")
for i in range(deg+1):
    liste.append(int(input("entrez le coefficient a{}: ".format(i))))
S=[]
print("les différentes sommes sont: ")
for i in range(1,deg+1):
    S.append(((-1)**i)*(liste[deg-i]/liste[deg]))
    print(f"S{i}={S[i-1]:.3f}")