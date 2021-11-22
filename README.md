# DevJams21-Project
Website link: <a href="https://forheart.herokuapp.com/">Visit ForHeart</a>
<br>
If you want to run in your local system, then download all files, store them in new folder and open **app.py** file and run it
# Heart Attack Prediction Model

We have made a tool for the prediction of Heart Attack using Machine Learning Model. We have also made a website for the same. The website will take input paramaters related to their health like blood pressure, occurrence of chest pain etc. from the user, and based on it, will provide the output (chances of getting heart attack) from our model on the website.

# Problem Statement
We are observing a recent trend of increase in heart attack fatalities with every passing generation. With the consultation of medical experts, we have figured out, that with the increasing workload, stress, and unhealthy lifestyle, ther's an increase in the upwardness of the curve of heart attack victims. Due to the lack of awareness of the general masses, this trend is not going to reduce in the coming future. We, as a group of four, did a brainstorming session to figure out what we can do, and have tried our best to come to the solution.

# Project Details
* We shall train and validate models and develop a machine learning pipeline for deployment.
* We shall build a HTML front end with an input form for independent variables(age, sex, chest pain type, resting blood pressure etc.)
* Build a back-end of the web application using Flask Framework

# Attributes
* **age**
* **sex:**<br /> 0 = Female <br /> 
            1 = Male <br />
* **chest pain type** (4 values) <br/>
            cp: chest pain type <br />
            -- Value 1: typical angina <br />
            -- Value 2: atypical angina <br />
            -- Value 3: non-anginal pain <br />
            -- Value 4: asymptomatic <br />
* **resting blood pressure**<br />         
            trestbps: resting blood pressure (in mm Hg on admission to the hospital) <br />
* **serum cholestoral in mg/dl**<br />   
            chol: serum cholestoral in mg/dl <br />
* **resting electrocardiographic results** (values 0,1,2)<br />
            restecg: resting electrocardiographic results <br />
            -- Value 0: normal <br />
            -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)<br />
            -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria <br />
* **oldpeak** = ST depression induced by exercise relative to rest<br />
* **maximum heart rate achieved**
* **exercise induced angina**<br />
            exang: exercise induced angina (1 = yes; 0 = no)<br />
* **the slope of the peak exercise ST segment**<br />
            slope: the slope of the peak exercise ST segment<br />
            -- Value 1: upsloping<br />
            -- Value 2: flat<br />
            -- Value 3: downsloping<br />
* **number of major vessels (0-3) colored by flourosopy** <br />
* **thal:** 1 = normal; 2 = fixed defect; 3 = reversable defect <br />
            Thalassemia (thal-uh-SEE-me-uh) is an inherited blood disorder that causes your body to have less hemoglobin than normal. Hemoglobin enables red blood cells to carry             oxygen. Thalassemia can cause anemia, leaving you fatigued. If you have mild thalassemia, you might not need treatment. <br />
