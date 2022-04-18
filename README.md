
# Breast Cancer Survival Prediction

This project is for my internship at futurereadytalent.

# What will the project do?

This project helps to predict whether a patient will survive a deadly disease like breast cancer or not using certain medical parameters given to the system.

## A complete Overview Towards the project:

The project is based on machine learning using Python.


We have a dataset of over 400 breast cancer patients who underwent surgery for the treatment of breast cancer. Below is the information of all columns in the dataset:

1. Patient_ID: ID of the patient
2. Age: Age of the patient
3. Gender: Gender of the patient
4. Protein1, Protein2, Protein3, Protein4: expression levels
5. Tumor_Stage: Breast cancer stage of the patient
6. Histology: Infiltrating Ductal Carcinoma, Infiltration Lobular Carcinoma, Mucinous Carcinoma
7. ER status: Positive/Negative
8. PR status: Positive/Negative
9. HER2 status: Positive/Negative
10. Surgery_type: Lumpectomy, Simple Mastectomy, Modified Radical Mastectomy, Other
11. DateofSurgery: The date of Surgery
12. DateofLast_Visit: The date of the last visit of the patient
13. Patient_Status: Alive/Dead

The dataset that was used above is collected from Kaggle. You can view/download this dataset from [here](https://www.kaggle.com/datasets/amandam1/breastcancerdataset).

Firstly, we download the dataset from kaggle. Then we need to import the necessary libraries and dataset. 
Then we have to check whether the columns of dataset contain any null values or not(null values are missing values) if there are any null values then we have to drop it.
Then we analyzed the different parameter of dataset i.e Gender, Tumour Stage, Histology, etc.
After analyzing the data we found the the dataset has a lot of categorical features. To use this data to train a machine learning model we have transformed values of all the categorical columns.
 Then we split the data into two sets, first part train dataset and second part test dataset. After that we choose an algorithm for classification and then train it.
 Then at last we have input all the features to make the prediction.

 After creating the model we have to deploy our Classification model into web application . For that purpose we use a Python framework called Flask . Flask is basically used to link our model with templates made using HTML and CSS. Different app routes are also created in our app.py file.
## Deployment :

To deploy this project we have used Azure service called Azure Web App. This web app will provide the necessary environment for running the model.
The Azure service will provide a base for our model and it will help to publish it over internet.

### How we deployed our model in Azure web app?
Firstly we created the resource group , choosen appropriate name, choosen region and App service plan and deployed it.
Then we go to the Deployment center and We set the source as Github and selected the project repository from the Github account. Then the Deployment was processed and finally we can test our web app for the survival prediction.

## Deployment Link of Web App(Deployed using Azure portal) :
https://breastcancersurvivalpred.azurewebsites.net/

### Repository link :
https://github.com/kushalking/BreastCancerSurvival_precdiction


## Screenshots

![2022-04-19 00_51_33-](https://user-images.githubusercontent.com/61675024/163883804-ea4f9649-c055-4469-9316-404d423f5564.png)


![2022-04-19 00_51_45-](https://user-images.githubusercontent.com/61675024/163883821-8e11eaa9-7284-4e38-8b30-062c5f06877e.png)

![2022-04-19 00_52_00-](https://user-images.githubusercontent.com/61675024/163883834-b748c5da-aca3-4ddb-a0a7-71dad4729d69.png)

![2022-04-19 00_52_14-](https://user-images.githubusercontent.com/61675024/163883861-28a8e52e-0c82-4b2d-ba9f-9c91957d4701.png)

