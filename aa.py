# import requests
# import json

# base_url_2 = 'https://api.icmr.org.in/covid_data/index.php/covid-data'

# token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjI0IiwidXNlcm5hbWUiOiJyYW5qZWV0LnNpbmdoLm1hc2hvbiIsInNlY19rZXkiOiJtYXNob25AY21jbHVkaGlhbmEuaW4iLCJpYXQiOjE2NjE0ODMyMTEsImV4cCI6MTY2MTQ4NDExMX0.8EuaLfxMS_YZcQcTZzBE17b9Ix23MHryCDAKTpN0vas'


# headers = {'Authorization': "Bearer {}".format(token)}



# icmr_data_request = requests.post(base_url_2,data= json.dumps({"date_from":"2020-01-01 00:00:00", 
#                     "date_to":"2022-08-23 10:00:00",
#                     "offset":'10000'}), headers=headers)

# icmr_response = icmr_data_request.json()

# for i in icmr_response.get('response')['data_result']:
#     print(type(i['date_sample_collection']))
#     i['date_sample_received']
#     i['date_of_sample_tested']

di = {'response':{
    'a':'111',
    'status':'22222'
}}

for a,b in di.items():
    print(a)

if di['status'] == '22222':
    print('yoooo')