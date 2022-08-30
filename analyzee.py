import sweetviz as sv
import psycopg2
import pandas as pd

conn = psycopg2.connect(
   database="icmr_covid_db", user='postgres', password='veryvery', host='127.0.0.1')




df = pd.read_sql_query('select * from icmrcoviddetails limit 1000000' , conn)



analyze_report = sv.analyze(df)
analyze_report.show_html('icmrcovid.html' , open_browser = True)