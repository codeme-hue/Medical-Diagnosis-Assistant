import numpy as np
import pandas as pd
import nltk
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer

class Diagnosis:

    def __init__(self):

        # Load the data
        self.data = pd.read_csv("data_med.csv")
        self.X=self.data.iloc[:,1]
        self.Y=self.data.iloc[:,0]

        all_symps = [x for x in (','.join(self.X)).split(',')]

        # Lemmatize the data
        self.lemmatizer= WordNetLemmatizer()
        all_symps=[self.lemmatizer.lemmatize(symp) for symp in all_symps]

        self.all_symptoms=[]
        for i in all_symps:
            if i not in self.all_symptoms:
                self.all_symptoms.append(i)

    def prepare_vect(self, n):
        n= [self.lemmatizer.lemmatize(symps) for symps in n] 
        vect=[]
        for i in self.all_symptoms:
            if i in n:vect.append(1)
            else: vect.append(0)
        
        return vect

    def train(self):
        X1=[]
        for i in self.X:
            X1.append(self.prepare_vect(i.split(',')))

        Y1=[i for i in range(0,3)]

        # Train model
        self.knn = KNeighborsClassifier(n_neighbors=1, p=3, metric='minkowski',weights='distance')
        self.knn.fit(X1,Y1)

        print("[LOG] Training complete.")

    def suggest_symptoms(self, symptom_list):

        X_lemmatized=[]
        for i in self.X:
            i= i.split(",")
            temp= [self.lemmatizer.lemmatize(symps) for symps in i] 
            X_lemmatized.append(temp)

        symptom_list = [self.lemmatizer.lemmatize(symp) for symp in symptom_list]
        test_symp=self.prepare_vect(symptom_list)
        y=self.knn.predict([test_symp])[0]
        temp_X=X_lemmatized[y]
        suggestion_X= list(set(temp_X)-set(symptom_list))  

        return suggestion_X

    def predict(self,gejala):
        test_symp=self.prepare_vect(gejala)

        prediksi_penyakit = self.Y[self.knn.predict([test_symp])[0]]
        penyaranan_obat = self.data.loc[self.data["Penyakit"]==prediksi_penyakit, 'Obat'].iloc[0]
        
        return [prediksi_penyakit, penyaranan_obat]

"""
if __name__=="__main__":
    dObj = Diagnosis()
    dObj.train()
    print("Getting suggestion: ")
    print(dObj.suggest_symptoms(['headache', 'vomit', 'cough']))
    print("Predicting: ")
    print(dObj.predict(['headache', 'dizziness', 'cough', 'fatigue']))
"""


        

        

    

    

