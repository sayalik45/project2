import numpy as np 
import pickle
import json

class car_data():
    def __init__(self,data):
        self.data = data

    def loading_files(self):
        with open('artifacts/car_model.pkl','rb') as file :
            self.model = pickle.load(file)

        with open('artifacts/car_scaler.pkl','rb') as file :
            self.scaler = pickle.load(file)

        with open('artifacts/project_data.json','r') as file :
            self.project_data = json.load(file)

    def car_prediction(self):
        self.loading_files()
        
        Present_Price = self.data['html_Present_Price']
        Kms_Driven = self.data['html_Kms_Driven']
        Fuel_Type = self.data['html_Fuel_Type']
        Seller_Type =self.data['html_Seller_Type']
        Transmission = self.data['html_Transmission']
        Owner = self.data['html_Owner']

        user_data = np.zeros(len(self.project_data['columns']))
        user_data[0] = Present_Price
        user_data[1] = Kms_Driven
        user_data[2] = self.project_data['Fuel_Type'][Fuel_Type]
        user_data[3] = self.project_data['Seller_Type'][Seller_Type]
        user_data[4] = self.project_data['Transmission'][Transmission]
        user_data[5] = Owner

        scaled_data = self.scaler.transform([user_data])
        prediction = self.model.predict(scaled_data)[0]
        print(f"Prediction = {prediction}")
        return prediction
