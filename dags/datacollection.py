import pandas as pd
import openpyxl


file_path = 'jamb data 2017-2018 revised - With YoY Growth Rate.xlsx'
sheet_name = 'Application 2017&2018'

#loading 2017-2018-Jamb Admission rate
def read_jamb_admission1(file_path,sheet_name,skip_rows,index_col): 

    df1 = pd.read_excel(file_path,sheet_name=sheet_name,skiprows=skip_rows,index_col=index_col)
    return df1

df1=read_jamb_admission1(file_path,sheet_name=sheet_name,skip_rows=3,index_col=0)
print(df1)

#renaming columns
admission_rate_df=df1.rename(columns={'F':'2017_F','M':'2017_M','TOTAL':'TOTAL_2017','F.1':'2018_F','M.1':'2018_M','TOTAL.1':'TOTAL_2018'})
print(admission_rate_df)

#loading 2023-2024-MATRICULATION-LIST-OF-ACCEPTED-STUDENTS-ON-JAMB
file_path = "2023-2024-MATRICULATION-LIST-OF-ACCEPTED-STUDENTS-ON-JAMB-CAPS-1.xlsx"
sheet_name ="Table 1"
def read_jamb_admission1(file_path,sheet_name,skip_rows,index_col): 

    df2 = pd.read_excel(file_path,sheet_name=sheet_name,skiprows=skip_rows,index_col=index_col)
    return df2

df2=read_jamb_admission1(file_path,sheet_name=sheet_name,skip_rows=1,index_col=0)
print(df2)

df2 = df2[['RG_SEX','STATE_NAME','RG_AGGREGATE','Admissio n Status']]
print(df2)

#loading the survey response data
file_path = "DataFestAfrica_ DataFlow Survey Form (Responses).xlsx"
sheet_name ="Form Responses 1"
def read_jamb_admission1(file_path,sheet_name,skip_rows,index_col): 

    df3 = pd.read_excel(file_path,sheet_name=sheet_name,skiprows=skip_rows,index_col=index_col)
    return df3

df3=read_jamb_admission1(file_path,sheet_name=sheet_name,skip_rows=1,index_col=0)
print(df3)


# Rename columns using the appropriate names
df3.columns = [
     "Gender", "Age", "Education_Status", "Exam_Type", 
    "WASSCE_Status", "WASSCE_Grades", "JAMB_Status", "JAMB_Score", 
    "Exam_Attempts", "School_Type", "Challenging_Subjects", 
    "Understanding_of_Topics", "Syllabus_Coverage", "Study_Frequency", 
    "Additional_Study_Materials", "Parental_Assistance", "Extra_Classes", 
    "Resources_for_Preparation", "Financial_Challenges", 
    "Home_Environment_Support", "Anxiety_About_Exams", 
    "Sources_of_Anxiety", "Confidence_in_Passing", 
    "School_Facilities", "Comfort_with_CBT"
]

# Display the DataFrame with renamed columns
print(df3.head())


#DAG CONFIGURATION
