import pickle
import pandas as pd
import numpy as np
import streamlit as st

data = pd.read_csv("C:/Users/ASUS/OneDrive/Desktop/dataset9000.csv")
model1 = pickle.load(open('C:/Users/ASUS/descisiontree.sav','rb'))
label = pickle.load(open('C:/Users/ASUS/label.sav','rb'))

columns = ['Database Fundamentals', 'Computer Architecture','Distributed Computing Systems', 'Cyber Security', 'Networking',
       'Software Development', 'Programming Skills', 'Project Management',
       'Computer Forensics Fundamentals', 'Technical Communication', 'AI ML',
       'Software Engineering', 'Business Analysis', 'Communication skills',
       'Data Science', 'Troubleshooting skills', 'Graphics Designing', 'Role']





st.title('CAREER GUIDANCE SYSTEM')
DATABASE_FUNDAMENTALS = st.selectbox('DATABASE FUNDAMENTALS',(0,1,2,3,4,5,6))
COMPUTER_ARICHTECTURE = st.selectbox('COMPUTER_ARICHTECTURE',(0,1,2,3,4,5,6))
DISTRIBUTED_COMPUTER_SETTINGS = st.selectbox('DISTRIBUTED COMPUTER SETTINGS',(0,1,2,3,4,5,6))
CYBER_SECURITY = st.selectbox('CYBER SECURITY',(0,1,2,3,4,5,6))
NETWORKING = st.selectbox('NETWORKING',(0,1,2,3,4,5,6))
SOFTWARE_DEVELOPEMENT = st.selectbox('SOFTWARE DEVELOPEMENT',(0,1,2,3,4,5,6))
PROGRAMMING_SKILLS = st.selectbox('PROGRAMMING SKILLS',(0,1,2,3,4,5,6))
PROJECT_MANAGEMENT = st.selectbox('PROJECT MANAGEMENT',(0,1,2,3,4,5,6))
COMPUTER_FORENCISCS_FUNDAMENTALS = st.selectbox('COMPUTER FORENCISCS FUNDAMENTALS',(0,1,2,3,4,5,6))
TECHNICAL_COMMUNICATION = st.selectbox('TECHNICAL COMMUNICATION',(0,1,2,3,4,5,6))
AI_ML = st.selectbox('AI ML',(0,1,2,3,4,5,6))
SOFTWARE_ENGINEERING = st.selectbox('SOFTWARE ENGINEERING',(0,1,2,3,4,5,6))
BUSINESS_ANALYSIS = st.selectbox('BUSINESS ANALYSIS',(0,1,2,3,4,5,6))
COMMUNICATION_SKILLS = st.selectbox('COMMUNICATION SKILLS',(0,1,2,3,4,5,6))
DATASCIENCE = st.selectbox('DATASCIENCE',(0,1,2,3,4,5,6))
TROUBLE_SHOOTING_SKILLS = st.selectbox('TROUBLE SHOOTING SKILLS',(0,1,2,3,4,5,6))
GRAPHICS_DESINGING = st.selectbox('GRAPHICS DESINGING',(0,1,2,3,4,5,6))

#from sklearn import preprocessing 
#label_encoder = preprocessing.LabelEncoder() 

#DATABASE_FUNDAMENTALS = label_encoder.fit_transform(['Database Fundamentals'])
#COMPUTER_ARICHTECTURE = label_encoder.fit_transform(['Computer Architecture'])
#DISTRIBUTED_COMPUTER_SETTINGS = label_encoder.fit_transform(['Distributed Computing Systems'])
#CYBER_SECURITY = label_encoder.fit_transform(['Cyber Security'])
#NETWORKING = label_encoder.fit_transform(['Networking'])
#SOFTWARE_DEVELOPEMENT = label_encoder.fit_transform(['Software Development'])
#PROGRAMMING_SKILLS = label_encoder.fit_transform(['Programming Skills'])
#PROJECT_MANAGEMENT = label_encoder.fit_transform(['Project Management'])
#COMPUTER_FORENCISCS_FUNDAMENTALS = label_encoder.fit_transform(['Computer Forensics Fundamentals'])
#TECHNICAL_COMMUNICATION = label_encoder.fit_transform(['Technical Communication'])
#AI_ML = label_encoder.fit_transform(['AI ML'])
#SOFTWARE_ENGINEERING = label_encoder.fit_transform(['Software Engineering'])
#BUSINESS_ANALYSIS = label_encoder.fit_transform(['Business Analysis'])
#COMMUNICATION_SKILLS = label_encoder.fit_transform(['Communication skills'])
#DATASCIENCE = label_encoder.fit_transform(['Data Science'])
#TROUBLE_SHOOTING_SKILLS = label_encoder.fit_transform(['Troubleshooting skills'])
#GRAPHICS_DESINGING = label_encoder.fit_transform(['Graphics Designing'])

#df2['Role'] = label_encoder.fit_transform(df2['Role'])
#df2.head()



submit = st.button('predict' )



ansr = [DATABASE_FUNDAMENTALS,COMPUTER_ARICHTECTURE,DISTRIBUTED_COMPUTER_SETTINGS,CYBER_SECURITY,NETWORKING,SOFTWARE_DEVELOPEMENT,PROGRAMMING_SKILLS,PROJECT_MANAGEMENT,COMPUTER_FORENCISCS_FUNDAMENTALS,TECHNICAL_COMMUNICATION,AI_ML,SOFTWARE_ENGINEERING,BUSINESS_ANALYSIS,COMMUNICATION_SKILLS,DATASCIENCE,TROUBLE_SHOOTING_SKILLS,GRAPHICS_DESINGING]
#inputs = label.fit_transform(ansr)
if submit == True:
    #model1.predict([DATABASE_FUNDAMENTALS,COMPUTER_ARICHTECTURE,DISTRIBUTED_COMPUTER_SETTINGS,CYBER_SECURITY,NETWORKING,SOFTWARE_DEVELOPEMENT,PROGRAMMING_SKILLS,PROJECT_MANAGEMENT,COMPUTER_FORENCISCS_FUNDAMENTALS,TECHNICAL_COMMUNICATION,AI_ML,SOFTWARE_ENGINEERING,BUSINESS_ANALYSIS,COMMUNICATION_SKILLS,DATASCIENCE,TROUBLE_SHOOTING_SKILLS,GRAPHICS_DESINGING])
    ansr1 = model1.predict([ansr])
    st.success(ansr1)