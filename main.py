
def caracterulDinLista(list):
    caracter = ""
    maxApariti = 0
    caracterApariti = 0
    apariti = 0
    for x in list:
        for i in range(len(x)):
            caracter = x[i]
            for y in list:
                for j in range(i,len(x)):
                    if x[j] == caracter:
                        apariti += 1        


def palindrom(element):

    n = len(element)
    for i in range(0, n//2):
        if element[i] != element[n-i-1]:
            return False
    return True


def elementePalindromDinLista(list):
    """Functia afiseaza toate elementele palindroame din lista

    Args:
        list ([string]): [lista de șiruri de caractere]
    """

    listaPalindrom = []
    for x in list:
        if palindrom(x):
            listaPalindrom.append(x)
    print(listaPalindrom)



def verificareListaUnica(list):
    """Functia verifica daca elementele din lista se repeta si afiseaza elementele care se repeta, in caz contrar afiseaza UNIC

    Args:
        list ([list[string]]): [lista de string-uri]
    """

    listaVerificata = []
    for i in range(len(list)):
        ok = True
        for j in range(i, len(list)):
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
    
    list = []
    while True:
        print("1. Citire lista")
        print("2. Verifica dacă un șir de caractere se găsește în listă ")
        print("3. Afiseaza elementele sirului care se repeta")
        print("4. Afiseaza elementele sirului care sunt palindroame ")
        print("5. Afiseaza lista in care elementele care contin caracterul cu cele mai multe apariti sunt inlocuite cu numarul respectiv ")
        print("x. Iesire\n")
        optiuneMeniu = input("Alege o optiune: ")
        if optiuneMeniu == "1":
            citireLista(list)
        elif optiuneMeniu == "2":
            sirDeCautat = input("Dati sirul de caractere care trebuie cautat: \n")
            sirCautatInLista(sirDeCautat, list)  
        elif optiuneMeniu == "3":
            verificareListaUnica(list) 
        elif optiuneMeniu == "4":
            elementePalindromDinLista(list)  
        elif optiuneMeniu == "5":
            caracterulDinLista(list)     
        elif optiuneMeniu == "x":
            break
        else:
            print("Optiune invalida! Reincercati")

main()            
        
