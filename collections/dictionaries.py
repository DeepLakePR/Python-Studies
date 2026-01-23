# Listas: Coleção ordenada, mutável e que permite valores duplicados
# Tuplas: Coleção ordenada, imutável e que permite valores duplicados
# Dicionários: Coleção não ordenada, mutável e que não permite vlaores duplicados 

list = ["teatea", "eg21f"]
tupla = ("item2", "item97");

dictionarie = {
    "key": "Gabriel",
    "key2": 1515151,
    "boolean": True,
    "boolean": False
}

# print(dictionarie.keys())

for key in dictionarie.keys():
    print(f"{key:10} -> {dictionarie[key]}");

    # print('key: ' + str(dictionarie[key]));
