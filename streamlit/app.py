import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image
import base64

pickle_in_motor = open("C:\\Users\\Admin\\Desktop\\Capstone\\NNN\\PD_Detection\\model_Motor.pkl","rb")
classifier_motor=pickle.load(pickle_in_motor)

pickle_in_nm = open("C:\\Users\\Admin\\Desktop\\Capstone\\NNN\\PD_Detection\\model_nonMotor.pkl","rb")
classifier_nonMotor=pickle.load(pickle_in_nm)

pickle_in_mm = open("C:\\Users\\Admin\\Desktop\\Capstone\\NNN\\PD_Detection\\model_Merged.pkl","rb")
classifier_merged=pickle.load(pickle_in_mm)


def welcome():
    return "Welcome All"


def predict_Motor(NP1RTOT,NP1PTOT,NP2PTOT,PDTRTMN,NP3TOT,DYSKPRES,NHY,NP4TOT,MSEADLG,ENROLL_AGE):
    prediction=classifier_motor.predict([[NP1RTOT,NP1PTOT,NP2PTOT,PDTRTMN,NP3TOT,DYSKPRES,NHY,NP4TOT,MSEADLG,ENROLL_AGE]])
    print(prediction)
    return prediction

def predict_nonMotor(SDMTOTAL,STAI_TOT,SFT_TOT,SCOPA_AUT_TOT,REMSLEEP_TOT,QUIP_A,QUIP_B,QUIP_C,QUIP_D,QUIP_E,MoCA_score,LNS_TOT,HVLT_TOT_Recall,HVLT_DCR_REC,HVLT_RETENTION,GDS_TOT,GDS_Depressed,ESS_TOT,ESS_Sleepy,BJLOT_TOT):
    prediction=classifier_nonMotor.predict([[SDMTOTAL,STAI_TOT,SFT_TOT,SCOPA_AUT_TOT,REMSLEEP_TOT,QUIP_A,QUIP_B,QUIP_C,QUIP_D,QUIP_E,MoCA_score,LNS_TOT,HVLT_TOT_Recall,HVLT_DCR_REC,HVLT_RETENTION,GDS_TOT,GDS_Depressed,ESS_TOT,ESS_Sleepy,BJLOT_TOT]])
    print(prediction)
    return prediction

def predict_ensemble(NP1RTOT,NP1PTOT,NP2PTOT,PDTRTMN,NP3TOT,DYSKPRES,NHY,NP4TOT,MSEADLG,ENROLL_AGE,SDMTOTAL,STAI_TOT,SFT_TOT,SCOPA_AUT_TOT,REMSLEEP_TOT,QUIP_A,QUIP_B,QUIP_C,QUIP_D,QUIP_E,MoCA_score,LNS_TOT,HVLT_TOT_Recall,HVLT_DCR_REC,HVLT_RETENTION,GDS_TOT,GDS_Depressed,ESS_TOT,ESS_Sleepy,BJLOT_TOT):
    prediction=classifier_merged.predict([[NP1RTOT,NP1PTOT,NP2PTOT,PDTRTMN,NP3TOT,DYSKPRES,NHY,NP4TOT,MSEADLG,ENROLL_AGE,SDMTOTAL,STAI_TOT,SFT_TOT,SCOPA_AUT_TOT,REMSLEEP_TOT,QUIP_A,QUIP_B,QUIP_C,QUIP_D,QUIP_E,MoCA_score,LNS_TOT,HVLT_TOT_Recall,HVLT_DCR_REC,HVLT_RETENTION,GDS_TOT,GDS_Depressed,ESS_TOT,ESS_Sleepy,BJLOT_TOT]])
    print(prediction)
    return prediction

def motor():


    st.write("Movement Disorder Society Unified Parkinsons Disease Rating Scale")
    NP1RTOT = st.number_input("NP1RTOT [MDS-UPDRS Rater Completed Total Score]")
    NP1PTOT = st.number_input("NP1PTOT [MDS-UPDRS Patient Questionnaire Total Score]")
    NP2PTOT = st.number_input("NP2PTOT [MDS-UPDRS Part 2 Total score]")
    PDTRTMN = st.number_input("PDTRTMN [Is the participant on medication or receiving deep brain stimulation]")
    NP3TOT = st.number_input("NP3TOT [MDS-UPDRS Part 3 Total score]")
    DYSKPRES = st.number_input("DYSKPRES [Were Dyskinesias present]")
    NHY = st.number_input("NHY [Hoehn & Yahr Stage]")
    NP4TOT = st.number_input("NP4TOT [MDS-UPDRS Part 4 Total score]")
    MSEADLG = st.number_input("MSEADLG [Modified Schwab and England - Overall]")
    ENROLL_AGE = st.number_input("AGE")
    result=""
    if st.button("Predict"):
        result=predict_Motor(NP1RTOT,NP1PTOT,NP2PTOT,PDTRTMN,NP3TOT,DYSKPRES,NHY,NP4TOT,MSEADLG,ENROLL_AGE)
    
    if result == 0:
        # st.success('The output is {}'.format(result))
        st.success('Patient Have Parkinson Disease')
    elif result == 1:
        st.success('Patient Is SWEDD')
        
    
    elif result == 2:
        st.success('Patient Is At HIGH RISK Of Having Parkinson In future')
    
    elif result == 3:
        st.success('Patient Have Healthy Controls')

    else:
        st.success('Enter Correct Values To Continue')


def nonmotor():



    SDMTOTAL = st.number_input("SDMTOTAL [Symbol Digit Modalities Total Correct]")
    STAI_TOT = st.number_input("STAI_TOT [State Trait Anxiety Inventory Total Score]")
    SFT_TOT = st.number_input("SFT_TOT [Modified Semantic Fluency Total Score]")
    SCOPA_AUT_TOT = st.number_input("SCOPA_AUT_TOT ")
    REMSLEEP_TOT = st.number_input("REMSLEEP_TOT [REM sleep Behaviour Disorder Questionnaire Total Score]")
    QUIP_A = st.number_input("QUIP_A [Questionnaire for Impulsive-Compulsive Disorders Part-A]")
    QUIP_B = st.number_input("QUIP_B [Questionnaire for Impulsive-Compulsive Disorders Part-B]")
    QUIP_C = st.number_input("QUIP_C [Questionnaire for Impulsive-Compulsive Disorders Part-C]")
    QUIP_D = st.number_input("QUIP_D [Questionnaire for Impulsive-Compulsive Disorders Part-D]")
    QUIP_E = st.number_input("QUIP_E [Questionnaire for Impulsive-Compulsive Disorders Part-E]")
    MoCA_score = st.number_input("MoCA_score [Montreal Cognitive Assesment Total Score]")
    LNS_TOT = st.number_input("LNS_TOT [Letter Number Sequencing Trial Total score]")
    HVLT_TOT_Recall  = st.number_input("HVLT_TOT_Recall [Hopkins verbal Learning Test]")
    HVLT_DCR_REC  = st.number_input("HVLT_DCR_REC [Hopkins verbal Learning Test]")
    HVLT_RETENTION  = st.number_input("HVLT_RETENTION [Hopkins verbal Learning Test Derived Retention T-Score]")
    GDS_TOT = st.number_input("GDS_TOT [Geriatric depression Scale Total Score]")
    GDS_Depressed = st.number_input("GDS_Depressed [Geriatric depression Scale]")
    ESS_TOT = st.number_input("ESS_TOT [Epworth Sleepiness Scale]")
    ESS_Sleepy = st.number_input("ESS_Sleepy [Epworth Sleepiness Scale]")
    BJLOT_TOT = st.number_input("BJLOT_TOT [Benton Judgement Of Line Orientation Test]")

    
    result=""
    if st.button("Predict"):
        result=predict_nonMotor(SDMTOTAL,STAI_TOT,SFT_TOT,SCOPA_AUT_TOT,REMSLEEP_TOT,QUIP_A,QUIP_B,QUIP_C,QUIP_D,QUIP_E,MoCA_score,LNS_TOT,HVLT_TOT_Recall,HVLT_DCR_REC,HVLT_RETENTION,GDS_TOT,GDS_Depressed,ESS_TOT,ESS_Sleepy,BJLOT_TOT)
    
    if result == 0:
        # st.success('The output is {}'.format(result))
        st.success('Patient Have Parkinson Disease')
    elif result == 1:
        st.success('Patient Is SWEDD')
        
    
    elif result == 2:
        st.success('Patient Is At HIGH RISK Of Having Parkinson In future')
    
    elif result == 3:
        st.success('Patient Have Healthy Controls')

    else:
        st.success('Enter Correct Values To Continue')


def ensemble():
    NP1RTOT = st.number_input("NP1RTOT [MDS-UPDRS Rater Completed Total Score]")
    NP1PTOT = st.number_input("NP1PTOT [MDS-UPDRS Patient Questionnaire Total Score]")
    NP2PTOT = st.number_input("NP2PTOT [MDS-UPDRS Part 2 Total score]")
    PDTRTMN = st.number_input("PDTRTMN [Is the participant on medication or receiving deep brain stimulation]")
    NP3TOT = st.number_input("NP3TOT [MDS-UPDRS Part 3 Total score]")
    DYSKPRES = st.number_input("DYSKPRES [Were Dyskinesias present]")
    NHY = st.number_input("NHY [Hoehn & Yahr Stage]")
    NP4TOT = st.number_input("NP4TOT [MDS-UPDRS Part 4 Total score]")
    MSEADLG = st.number_input("MSEADLG [Modified Schwab and England - Overall]")
    ENROLL_AGE = st.number_input("AGE")

    SDMTOTAL = st.number_input("SDMTOTAL [Symbol Digit Modalities Total Correct]")
    STAI_TOT = st.number_input("STAI_TOT [State Trait Anxiety Inventory Total Score]")
    SFT_TOT = st.number_input("SFT_TOT [Modified Semantic Fluency Total Score]")
    SCOPA_AUT_TOT = st.number_input("SCOPA_AUT_TOT ")
    REMSLEEP_TOT = st.number_input("REMSLEEP_TOT [REM sleep Behaviour Disorder Questionnaire Total Score]")
    QUIP_A = st.number_input("QUIP_A [Questionnaire for Impulsive-Compulsive Disorders Part-A]")
    QUIP_B = st.number_input("QUIP_B [Questionnaire for Impulsive-Compulsive Disorders Part-B]")
    QUIP_C = st.number_input("QUIP_C [Questionnaire for Impulsive-Compulsive Disorders Part-C]")
    QUIP_D = st.number_input("QUIP_D [Questionnaire for Impulsive-Compulsive Disorders Part-D]")
    QUIP_E = st.number_input("QUIP_E [Questionnaire for Impulsive-Compulsive Disorders Part-E]")
    MoCA_score = st.number_input("MoCA_score [Montreal Cognitive Assesment Total Score]")
    LNS_TOT = st.number_input("LNS_TOT [Letter Number Sequencing Trial Total score]")
    HVLT_TOT_Recall  = st.number_input("HVLT_TOT_Recall [Hopkins verbal Learning Test]")
    HVLT_DCR_REC  = st.number_input("HVLT_DCR_REC [Hopkins verbal Learning Test]")
    HVLT_RETENTION  = st.number_input("HVLT_RETENTION [Hopkins verbal Learning Test Derived Retention T-Score]")
    GDS_TOT = st.number_input("GDS_TOT [Geriatric depression Scale Total Score]")
    GDS_Depressed = st.number_input("GDS_Depressed [Geriatric depression Scale]")
    ESS_TOT = st.number_input("ESS_TOT [Epworth Sleepiness Scale]")
    ESS_Sleepy = st.number_input("ESS_Sleepy [Epworth Sleepiness Scale]")
    BJLOT_TOT = st.number_input("BJLOT_TOT [Benton Judgement Of Line Orientation Test]")

    result=""
    if st.button("Predict"):
        result=predict_ensemble(NP1RTOT,NP1PTOT,NP2PTOT,PDTRTMN,NP3TOT,DYSKPRES,NHY,NP4TOT,MSEADLG,ENROLL_AGE,SDMTOTAL,STAI_TOT,SFT_TOT,SCOPA_AUT_TOT,REMSLEEP_TOT,QUIP_A,QUIP_B,QUIP_C,QUIP_D,QUIP_E,MoCA_score,LNS_TOT,HVLT_TOT_Recall,HVLT_DCR_REC,HVLT_RETENTION,GDS_TOT,GDS_Depressed,ESS_TOT,ESS_Sleepy,BJLOT_TOT)
    
    if result == 0:
        # st.success('The output is {}'.format(result))
        st.success('Patient Have Parkinson Disease')
    elif result == 1:
        st.success('Patient Is SWEDD')
        
    
    elif result == 2:
        st.success('Patient Is At HIGH RISK Of Having Parkinson In future')
    
    elif result == 3:
        st.success('Patient Have Healthy Controls')

    else:
        st.success('Enter Correct Values To Continue')


@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def main():

    st.set_page_config(page_title="Parkinsons Test", page_icon=':👨‍⚕️:')
    
    img = get_img_as_base64("hospital_img.jpg")

    style = "<style>h2 {text-align: center;}</style>"

    st.markdown(style, unsafe_allow_html=True)
    st.columns(3)[1].header("CAPSTONE PROJECT")
    html_temp = """
                    <div style="background-color:tomato;padding:10px">
                    <h2 style="color:white;text-align:center;">Parkinson Disease</h2>
                    </div>
                    <style>
                    [data-testid = "stAppViewContainer"]
                     {
                        background-image: url("data:image/png;base64,{img}");
                            background-size: cover;
                            background-position: center; 
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                    }
                </style>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write(" ")

    

    # page_bg_img = '''
    #             <style>
    #                 [data-testid = "stAppViewContainer"]
    #                  {
    #                     background-image: url("data
    #                      ;image/png;base64,{img}");
    #                         background-size: cover;
    #                 }
    #             </style>'''

    # st.markdown(page_bg_img, unsafe_allow_html=True)

    page = st.sidebar.radio("Navigation",['Motor', 'Non-Motor', 'Ensemble'])
    
    if page == 'Motor':
        motor()

    if page == 'Non-Motor':
        nonmotor()
        pass

    if page == 'Ensemble':
        ensemble()
        pass

    st.write(" ")


    if st.button("About"):
        st.write("Parkinson's disease(PD) is a neuro-degenerative disorder caused due to loss of dopaminergic neurons in the substantia nigra located at the midbrain, disturbing the patient's control over motor movements and non-motor senses. During the early stages of Parkinson's disease, patients may experience bradykinesia, resting tremors, anxiety, disturbance in sleep, depression, vocal impairment or fatigue.")
        st.write("In India, Parkinson's disease poses a significant healthcare burden, with an estimated prevalence of around 1% of the population over the age of 60, translating to millions of affected individuals. The lack of early diagnosis and intervention exacerbates the challenges faced by PD patients and their caregivers, highlighting the urgent need for effective detection methods. Machine learning (ML) models offer promising avenues for addressing this critical need in PD management.")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()