import time
import requests
import json
import psycopg2
from tokenGen import xyz
import datetime 
import pickle




save_data_list =[]

tokenlist= []

date_from_list = ['']
date_to_list = ['']


def abc():
    try:
        conn = psycopg2.connect(
        database="icmr_covid_db", user='postgres', password='veryvery', host='127.0.0.1')
        cursor = conn.cursor()

        print(tokenlist)

        base_url_2 = 'https://api.icmr.org.in/covid_data/index.php/covid-data'

        def token_list(tokenlist):
            for i in tokenlist:
                token = i
                return token

        def date_from_fc(date_from_list):
            for i in date_from_list:
                date_from = i
                print(date_from)
                return date_from

        def date_to_fc(date_to_list):
            for i in date_to_list:
                date_to = i
                print(date_to)
                return date_to
        

        headers = {'Authorization': "Bearer {}".format(token_list(tokenlist))}
        

        str_offset= len(save_data_list)

        print(str_offset) 

        def continue_data_req(str_offset):
            print('continueee')
            data_req = requests.post(base_url_2,data= json.dumps({"date_from":f"{date_from_fc(date_from_list)}", 
                        "date_to":f"{date_to_fc(date_to_list)}",
                        "offset":f'{str_offset}'}), headers=headers)

            print('3333' , data_req)
            return data_req

        def initial_data_req():
            print('iinnitilll')
            x = date_from_fc(date_from_list)
            y = date_to_fc(date_to_list)
            data_req = requests.post(base_url_2,data= json.dumps({"date_from":f"{x}", 
                        "date_to":f"{y}"}), headers=headers)
            print('444' , data_req)
            
            return data_req

        try:
            if str_offset > 0 :
                    print('offset is presnt ')
                    icmr_data_request = continue_data_req(str_offset)
            else:
                    print('NOOO offset')
                    icmr_data_request = initial_data_req()
                    
        except Exception as e :
            print('initial exceptionsss')
            print(e) 


        icmr_response = icmr_data_request.json()

        for a,b in icmr_response.items():
            print('uuuuuu' ,a)

        try:
            print('tryyyy')
            if icmr_response.get('response') != None:
                error_icmr_response = icmr_response.get('response')
                if error_icmr_response.get('error_msg')  == "Invalid Input"  :
                    print('errorrr --->>> Invalid Input')
                    file_lod = open("ongoing_date.pkl","rb")
                    for i in pickle.load(file_lod):
                        date_from_list.clear()
                        date_from_list.append(i)
                    for i in pickle.load(file_lod):
                        date_to_list.clear()
                        date_to_list.append(i)
                    
                    if str_offset > 0 :
                                    
                            icmr_data_request = continue_data_req(str_offset)

                    else:
                            icmr_data_request = initial_data_req()

                elif error_icmr_response.get('error_msg') == 0:
                    print('errorr---->> Zero')
                    for i in date_from_list:
                        print(i)
                        i = datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
                        i += datetime.timedelta(days=1)
                        date_from_list.clear()
                        date_from_list.append(str(i))
                        print(date_from_list)

                    for i in date_to_list:
                        i = datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
                        i += datetime.timedelta(days=1)
                        date_to_list.clear()
                        date_to_list.append(str(i))
                        print(date_to_list)
                    file_date = open("ongoing_date.pkl","wb")
                    pickle.dump(date_from_list,file_date)
                    pickle.dump(date_to_list, file_date)
                    file_date.close()

                    if str_offset > 0 :
                                    
                            icmr_data_request = continue_data_req(str_offset)

                    else:
                            icmr_data_request = initial_data_req()


            elif icmr_response['status'] == 'Wrong number of segments':
                        print('wrong number of segment')
                        token = xyz ()
                        tokenlist.clear()
                        tokenlist.append(token)
                        headers = {'Authorization': "Bearer {}".format(token_list(tokenlist))}
                        print(headers)

                        if str_offset > 0 :
                                
                                icmr_data_request = continue_data_req(str_offset)

                        else:
                                icmr_data_request = initial_data_req()

            elif icmr_response['status'] == 'Expired token':
                        print('expired token')
                        token = xyz ()                          
                        tokenlist.clear()
                        tokenlist.append(token)
                        headers = {'Authorization': "Bearer {}".format(token_list(tokenlist))}

                        if str_offset > 0 :
                                icmr_data_request = continue_data_req(str_offset)
                                print(icmr_data_request)

                        else:
                                icmr_data_request = initial_data_req()
            
                
        except Exception as e:
            print('status excpetion')
            print(e)
        

        icmr_response = icmr_data_request.json()
        
        if icmr_response.get('response') != None:
            succ = icmr_response.get('response')
            if succ.get('data_result') != None:
               
                print('length of data retrived ---->>  ' , len(succ.get('data_result')))
                
                for i in icmr_response.get('response')['data_result']:

                    save_data_list.append(i)


                if len(succ.get('data_result')) < 10000:

                    for i in save_data_list:
                        query = """insert into icmr1 (icmr_id,clinical_id,age, age_in, gender, patient_category,state_residence,district_residence,lab_id,date_sample_collection,date_sample_received,date_of_sample_tested,symptoms,underlying_medical_condition,testing_kit_used,egene_screening,ct_value_screening,rdrp_confirmatory,ct_value_rdrp,orf1b_confirmatory,ct_value_orf1b,final_test_result,entry_date,updated_on) values (%s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s )""" 
                        listt =  (i['icmr_id'],i['clinical_id'],i['age'],i['age_in'],i['gender'],i['patient_category'],i['state_residence'],i['district_residence'],i['lab_id'],i['date_sample_collection'],i['date_sample_received'],i['date_of_sample_tested'],i['symptoms'],i['underlying_medical_condition'],i['testing_kit_used'],i['egene_screening'],i['ct_value_screening'],i['rdrp_confirmatory'],i['ct_value_rdrp'],i['orf1b_confirmatory'],i['ct_value_orf1b'],i['final_test_result'],i['entry_date'],i['updated_on'])


                        cursor.execute(query , listt)
                        conn.commit()
                        

                    print('success ---- icmr1')
                    save_data_list.clear()
                    time.sleep(2)
                    
                    for i in date_from_list:
                        print(i)
                        i = datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
                        i += datetime.timedelta(days=1)
                        date_from_list.clear()
                        date_from_list.append(str(i))
                        print(date_from_list)

                    for i in date_to_list:
                        i = datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
                        i += datetime.timedelta(days=1)
                        date_to_list.clear()
                        date_to_list.append(str(i))
                        print(date_to_list)
                    file_date = open("ongoing_date.pkl","wb")
                    pickle.dump(date_from_list,file_date)
                    pickle.dump(date_to_list, file_date)
                    file_date.close()
                    print("pickleeee ")

            else:
                print(succ)
                print('databaseerror')
    except Exception as e :
        print('final exception')
        print(e)
    conn.close()
    return abc()

abc()

    



