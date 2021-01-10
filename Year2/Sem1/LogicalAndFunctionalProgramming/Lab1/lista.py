class Nod:
    def __init__(self, e):
        self.e = e
        self.urm = None
    
class Lista:
    def __init__(self, prim = None):
        self.prim = prim
        
def Concatenate(list1, list2):
    if list2.prim == None:
        return list1
    if list1.prim == None:
        return list2
    result = Lista(Nod(list1.prim.e))
    result.prim.urm = Concatenate(Lista(list1.prim.urm),list2).prim
    return result

def Substitute(list1, list2, elem):
    if list1.prim == None:
        return Lista()
    elif list1.prim.e != elem:
        result = Lista(Nod(list1.prim.e))
        result.prim.urm = Substitute(Lista(list1.prim.urm),list2,elem).prim
        return result
    else:
        return Concatenate(list2,Substitute(Lista(list1.prim.urm),list2,elem))

def GetNth(list, n, index=0):
    if index == n:
        return list.prim.e
    else:
        newList = Lista(list.prim.urm)
        return GetNth(newList,n,index+1)

'''
crearea unei liste din valori citite pana la 0
'''
def creareLista():
    lista = Lista()
    lista.prim = creareLista_rec()
    return lista

def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.urm = creareLista_rec()
        return nod

'''
tiparirea elementelor unei liste
'''
def tipar(lista):
    tipar_rec(lista.prim)
    print('\n')
    
def tipar_rec(nod):
    if nod != None:
        print (nod.e, end=" ")
        tipar_rec(nod.urm)
        

'''
program pentru test
'''
        
def main():
    nod1 = Nod(1)
    nod2 = Nod(2)
    nod3 = Nod(3)
    nod4 = Nod(2)
    
    nod1.urm = nod2
    nod2.urm = nod3
    nod3.urm = nod4

    nod5 = Nod(999)
    nod6 = Nod(888)

    nod5.urm = nod6

    test_list1 = Lista(nod1)
    test_list2 = Lista(nod5)

    el = 2

    result = Substitute(test_list1, test_list2, el)
    tipar(result)
    print(GetNth(result, 2))

    print("=========================")

    list1 = creareLista()
    list2 = creareLista()
    elem = int(input("Element to substitute by: "))

    result = Substitute(list1, list2, elem)
    tipar(result)
    
main() 
    
    
    
    
    