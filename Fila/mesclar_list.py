class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    inicio = ListNode()
    atual = inicio

    while list1 is not None and list2 is not None:

        if list1.val <= list2.val:
            atual.next = list1
            list1 = list1.next
        else:
            atual.next = list2
            list2 = list2.next

        atual = atual.next

    if list1 is not None:
        atual.next = list1
    else:
        atual.next = list2

    return inicio.next

def criar_lista(valores):
    inicio = None
    atual = None

    for valor in valores:
        novo = ListNode(valor)

        if inicio is None:
            inicio = novo
            atual = novo
        else:
            atual.next = novo
            atual = novo

    return inicio

def exibir_lista(lista):
    valores = []

    while lista is not None:
        valores.append(lista.val)
        lista = lista.next

    print(valores)

list1 = criar_lista([1, 2, 4])
list2 = criar_lista([1, 3, 6])

resultado = merge_two_lists(list1, list2)

exibir_lista(resultado)
