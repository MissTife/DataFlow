import pandas as pd
import openpyxl

file_path = 'jamb data 2017-2018 revised - With YoY Growth Rate.xlsx'
sheet_name = 'Application 2017&2018'


def read_jamb_admission(file_path,sheet_name,skip_rows,index_col): 

    df1 = pd.read_excel(file_path,sheet_name=sheet_name,skiprows=skip_rows,index_col=index_col)
    return df1

df=read_jamb_admission(file_path,sheet_name=sheet_name,skip_rows=3,index_col=0)
print(df)

#renaming columns
admission_rate_df=df.rename(columns={'F':'2017_F','M':'2017_M','TOTAL':'TOTAL_2017','F.1':'2018_F','M.1':'2018_M','TOTAL.1':'TOTAL_2018'})
print(admission_rate_df)

#DAG CONFIGURATION