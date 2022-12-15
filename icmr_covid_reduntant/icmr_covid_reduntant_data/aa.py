# import datetime

# x = '2022-02-28 00:00:00'

# x = datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")

# x += datetime.timedelta(days=1)
# print(x)
# print(type(str(x)))

# import pickle

# b = {"a":1, "b":3}
# f=['df','xxxxxxx']


# # print(b.get('ax'))

# try:
#     if b.get('a') == 1:
#         print('chalpeyaaa')
#         oo = open("nn.pkl", "wb")
#         pickle.dump(b , oo)
#         pickle.dump(f , oo)
#         oo.close()

#         print('dpne')
#     else:
#         print('elseeeeee')

# except Exception as e:
#     print(e)

# ee = open("nn.pkl","rb")
# y = pickle.load(ee)
# yt = pickle.load(ee)

# print(y ,yt)

import pickle

date_from_list = ['2020-03-01 00:00:00']
date_to_list = ['2020-03-01 23:59:59']

file_date = open("ongoing_date.pkl","wb")
pickle.dump(date_from_list,file_date)
pickle.dump(date_to_list, file_date)
file_date.close()
print("pickleeee ")


print(date_from_list,date_to_list)
file_lod = open("ongoing_date.pkl","rb")
for i in pickle.load(file_lod):
    # date_from_list.append(i)
    print(date_from_list)
for i in pickle.load(file_lod):
    # date_to_list.append(i)
    print(date_to_list)

# def xx():
#     for i in date_from_list:
#         # print(i)
#         return i
# y = xx()
# print(y)