import pickle
import json
import config
import numpy as np

class FashionProduct():
    def __init__(self,product_name,brand,category,rating,size,color):
        self.product_name = product_name
        self.brand = brand
        self.category = category
        self.rating = rating
        self.size = size
        self.color = color
    def __load_saved_data(self):
        with open (config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open (config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)
        
    def get_predicted_charges(self):
        self.__load_saved_data()
        product_name = self.json_data['Product_Name'][self.product_name]
        brand = self.json_data['Brand'][self.brand]
        category = self.json_data['Category'][self.category]
        size = self.json_data['Size'][self.size]
        color = 'color_'+ self.color
        color_index = self.json_data["Column_Names"].index(color)
        
        test_array = np.zeros([1, self.model.n_features_in_])
        test_array[0,0] = product_name
        test_array[0,1] = brand
        test_array[0,2] = category
        test_array[0,3] = self.rating
        test_array[0,4] = size
        test_array[0,color_index] = 1

        predicted_charges = np.around(self.model.predict(test_array)[0],3)

        return predicted_charges