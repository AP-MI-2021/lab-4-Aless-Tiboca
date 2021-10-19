def verificareListaUnica(list):
    """Functia verifica daca elementele din lista se repeta si afiseaza elementele care se repeta, in caz contrar afiseaza UNIC

    Args:
        list ([list[string]]): [lista de string-uri]
    """

    listaVerificata = []
    for i in range(len(list)+1):
        ok = True
        for j in range(i, len(list)+1):
            if list[i] == list[j]:
                ok = False
        if ok:
            listaVerificata.append(list[i])   
    if listaVerificata is None:
        print("UNIC")
    else:
        print(listaVerificata)    

def sirCautatInLista(sirDeCautat, list):
    """Functia verifica daca exista un sir de caractere intr-o lista si afiseaza DA, daca sirul este gasit, in caz contrar NU

    Args:
        sirDeCautat ([string]): [sirul pe care trebuie sa il cautam]
        list (list[string]): [lista de siruri]
    """
    gasit = False
    for x in list:
        if x == sirDeCautat:
            print("DA")
            gasit = True
    if not gasit:
        print("NU")        


def testSirCautatInLista():
    assert sirCautatInLista("sdv", ["sdv", "ccc", "dds", "sdv"]) == "DA"
    assert sirCautatInLista("drd", ['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == "DA"
    assert sirCautatInLista("cld",['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == "NU"

def citireLista(list):
    list = []
    n = int(input("Dati numarul de elemente a sirului: "))
    print("Dati elementele sirului: ")
    for i in range(n):
        x = input()
        list.append(x)

    return list

def main():

    testSirCautatInLista()

    list = []
    while True:
        print("1. Citire lista")
        print("2. Verifica dacă un șir de caractere se găsește în listă ")
        print("3. Afiseaza elementele sirului care se repeta")
        print("x. Iesire\n")
        optiuneMeniu = input("Alege o optiune: ")
        if optiuneMeniu == "1":
            citireLista(list)
        elif optiuneMeniu == "2":
            sirDeCautat = input("Dati sirul de caractere care trebuie cautat: \n")
            sirCautatInLista(sirDeCautat, list)  
        elif optiuneMeniu == "3":
            verificareListaUnica(list)  
        elif optiuneMeniu == "x":
            break
        else:
            print("Optiune invalida! Reincercati")

main()            
        
