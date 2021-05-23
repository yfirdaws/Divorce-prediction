#%%writefile app.py
 
import pickle
import streamlit as st

# loading the trained model
pickle_in = open('Divorce.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Q2, Q4, Q6, Q15, Q17, Q22, Q24, Q25, Q26, Q29, Q40, Q48, Q49, Q53):
    # Pre-processing user input 
    if Q2=="Never":
        Q2= 0
    elif Q2== "Seldom":
          Q2= 1
    elif Q2== "Averagely":
          Q2= 2
    elif Q2== "Frequently":
          Q2=3
    else:
        Q2 = 4
    
    if Q4 =="Never":
        Q4 = 0
    elif Q4 == "Seldom":
        Q4 = 1
    elif Q4 == "Averagely":
        Q4 = 2
    elif Q4 == "Frequently":
        Q4= 3
    else:
        Q4 = 4

    if Q6 == "Never":
        Q6 = 0
    elif Q6 == "Seldom":
        Q6 = 1
    elif Q2 == "Averagely":
        Q6= 2
    elif Q6== "Frequently":
        Q6 = 3
    else:
        Q6 = 4

    if Q15 == "Never":
        Q15 = 0
    elif Q15 == "Seldom":
        Q15 = 1
    elif Q15 == "Averagely":
        Q15 = 2
    elif Q15== "Frequently":
        Q15 = 3
    else:
        Q15 = 4
    
    if Q17 == "Never":
        Q17= 0
    elif Q17 == "Seldom":
        Q17= 1
    elif Q17 == "Averagely":
        Q17 = 2
    elif Q17== "Frequently":
        Q17= 3
    else:
        Q17 = 4


    if Q22 == "Never":
        Q22 = 0
    elif Q22 == "Seldom":
        Q22 = 1
    elif Q22 == "Averagely":
        Q22 = 2
    elif Q22== "Frequently":
        Q22 = 3
    else:
        Q22 = 4

    if Q24 == "Never":
        Q2 = 0
    elif Q24 == "Seldom":
        Q24 = 1
    elif Q24 == "Averagely":
        Q24 = 2
    elif Q24== "Frequently":
        Q24 = 3
    else:
        Q24 = 4
    
    if Q25 == "Never":
        Q25 = 0
    elif Q25 == "Seldom":
        Q25 = 1
    elif Q25 == "Averagely":
        Q25 = 2
    elif Q25== "Frequently":
        Q25 = 3
    else:
        Q25 = 4

    if Q26 == "Never":
        Q26 = 0
    elif Q26 == "Seldom":
        Q26 = 1
    elif Q26 == "Averagely":
        Q26 = 2
    elif Q26== "Frequently":
        Q26 = 3
    else:
        Q26 = 4

    if Q29 == "Never":
        Q29 = 0
    elif Q29 == "Seldom":
        Q29 = 1
    elif Q29 == "Averagely":
        Q29 = 2
    elif Q29== "Frequently":
        Q29 = 3
    else:
        Q29 = 4

    if Q40 == "Never":
        Q40= 0
    elif Q40 == "Seldom":
        Q40 = 1
    elif Q40 == "Averagely":
        Q40 = 2
    elif Q40== "Frequently":
        Q40 = 3
    else:
        Q40 = 4

    if Q48 == "Never":
        Q48 = 0
    elif Q48 == "Seldom":
        Q48 = 1
    elif Q48 == "Averagely":
        Q48 = 2
    elif Q48== "Frequently":
        Q48 = 3
    else:
        Q48 = 4

    if Q49 == "Never":
        Q49 = 0
    elif Q2 == "Seldom":
        Q49 = 1
    elif Q49 == "Averagely":
        Q49 = 2
    elif Q49== "Frequently":
        Q49 = 3
    else:
        Q49 = 4

    if Q53 == "Never":
        Q53 = 0
    elif Q53 == "Seldom":
        Q53 = 1
    elif Q53 == "Averagely":
        Q53 = 2
    elif Q53== "Frequently":
        Q53 = 3
    else:
        Q53 = 4
      
    # Making predictions 
    prediction = classifier.predict( 
        [[ Q2, Q4, Q6, Q15, Q17, Q22, Q24, Q25, Q26, Q29, Q40, Q48, Q49, Q53]])

    if prediction == 0:
        pred = 'No Divorce'
    else:
        pred = ' Divorce'
    return pred
      
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Divorce Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Q2 = st.selectbox('I know we can ignore our differences, even if things get hard sometimes.',("Never","Seldom","Averagely","Frequently","Always"))
    Q4 = st.selectbox("When I discuss with my spouse, to contact him will eventually work.",("Never","Seldom","Averagely","Frequently","Always"))
    Q6 = st.selectbox("We don't have time at home as partners.",("Never","Seldom","Averagely","Frequently","Always"))
    Q15 = st.selectbox("Our dreams with my spouse are similar and harmonious",("Never","Seldom","Averagely","Frequently","Always"))
    Q17 = st.selectbox("We share the same views about being happy in our life with my spouse",("Never","Seldom","Averagely","Frequently","Always"))
    Q22 = st.selectbox("I know how my spouse wants to be taken care of when she/he sick.",("Never","Seldom","Averagely","Frequently","Always"))
    Q24 = st.selectbox("I can tell you what kind of stress my spouse is facing in her/his life.",("Never","Seldom","Averagely","Frequently","Always"))
    Q25 = st.selectbox("I have knowledge of my spouse's inner world.",("Never","Seldom","Averagely","Frequently","Always"))
    Q26 = st.selectbox("I know my spouse's basic anxieties.",("Never","Seldom","Averagely","Frequently","Always"))
    Q29 = st.selectbox("I know my spouse very well.",("Never","Seldom","Averagely","Frequently","Always"))
    Q40 = st.selectbox("We're just starting a discussion before I know what's going on",("Never","Seldom","Averagely","Frequently","Always"))
    Q48 = st.selectbox("I feel right in our discussions.",("Never","Seldom","Averagely","Frequently","Always"))
    Q49 = st.selectbox("I have nothing to do with what I've been accused of.",("Never","Seldom","Averagely","Frequently","Always"))
    Q53 = st.selectbox("When I discuss, I remind my spouse of her/his inadequacy.",("Never","Seldom","Averagely","Frequently","Always"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Q2, Q4, Q6, Q15, Q17, Q22, Q24, Q25, Q26, Q29, Q40, Q48, Q49, Q53) 
        st.success('Well, I sight {}'.format(result))
        print(result)

if __name__=='__main__': 
    main()




  

 


    