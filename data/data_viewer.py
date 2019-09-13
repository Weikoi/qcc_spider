
import pickle as pk

data = pk.load(file=open('./citycode_2_CN.pkl', 'rb'))

print(len(data)*5000)
# print(data['AH'])
# #
# # for k,v in data.items():
# #     print(k, v)