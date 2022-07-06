#encoding: utf-8

#vetor com indice que na realidade é o nome
#Um dicionário é uma coleção não ordenada de pares chave-valor.
eng2por = {}
eng2por['one'] = 'um'
eng2por['two'] = 'dois'
eng2por['three'] = 'três'

inventario = {'kiwis': 430, 'bananas': 312, 'laranjas': 525, 'peras': 217}

mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"]) #18

##############################################################################
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # a ordem em que obtemos as chaves não está definida
   print("a chave é", akey, ", e o valor é: ", inventory[akey])

#pega as chaves em vetor
ks = list(inventory.keys())
print(ks)

#deleta do dicionario
del inventory['bananas']

#lista as chaves também
for k in inventory:
   print("Got key", k)