from operator import itemgetter
#
# dic = {'Jonas': 'jonasreiter@hotmal.com',
#        'susan': 'susan.reiter@hotmail.com',
#        'professora': 'contato@reiter.page'}
#
# dic['Acesso'] = 'entra21@acesso.com.br'
# dic["Vinicius"] = 'vinereisch522@gmail.com'
# dic['susan'] = 'susan@gmail.com'
#
# dic.update({'Jonas': 'jonas123@hotmail.com'})
#
# dic['Professaura'] = dic.pop('professora')
# print(dic.keys())
# print(dic.values())
# dic.popitem()
#
# for i in dic:
#        print(i)
# for i in dic:
#        print(dic[i])
# for k, v in dic.items():
#        print(f"{k}----------{v}")
# if 'Jonas' in dic:
#        print('encontrei')
#
# chaves = ["a", "c", "b"]
# valor = 0
#
# novo_dic = dict.fromkeys(chaves,valor)
# print(novo_dic)
#
# lista1 = ['jonas', 'raul', 'stefan']
# lista2 = [30, 30, 50]
# dic3 = {}
# for i in range(len(lista1)):
#        dic3[lista1[i]] = lista2[i]
# dic4 = {** dic, ** dic3}
# print(dic4)

times = {"Palmeiras": 18,
         "Flamengo": 12,
         "Coritiba": 22}

timesnovo = sorted(times.items(), key=itemgetter(1), reverse=True)

print(timesnovo)

for i, time in enumerate(timesnovo):
       print(f'{i+1} - {time[0]} - {time[1]}')