lista = ["item1", "item2", "item3"] # Mutável - pode adicionar ou remover elementos

tupla = ("item1", "item2", "item3"); # Imutável

tupla2 = ("string"); # class str
# print(type(tupla2)) # <class 'str'>

tupla3 = ("string",) # class tuple

tupla4 = "item4", "item5", "item6"
# print(tupla4)
# print(type(tupla4)) # class tuple

list2 = list(tupla4); # o mesmo serve para variavel = tuple(list2) - criaria uma tupla usando uma lista
# print(type(list2));

tupla5 = tupla + tupla4; # junção 
# print(tupla5)

for x in tupla5:
    print(x);

(x, y, z, a, b, c) = tupla5;
print(x); #"item1" 
print(y); #"item2"
print(z); #"item3"
print(a); #"item4" 
print(b); #"item5"
print(c); #"item6"

(x, y, *z) = tupla5;
# o uso do * no z vai receber todo o resto da lista que não foi atribuida
print(x); # item1
print(y); # item2
print(z); # ["item3, "4" ...] retorna um array de items
