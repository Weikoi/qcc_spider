
import pickle as pk

data = pk.load(file=open('./province_city_dict.pkl', 'rb'))

print(data['AH'])

for k,v in data.items():
    print(k, v)