import random
from operator import itemgetter

dic = {}
for i in range(1,5):
    dic[f"Jogador {i}"] = random.randrange(0,10)
print(dic)
dic_new = sorted(dic.items(), key=itemgetter(1), reverse=True)
print(dic_new)