
import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize


def read_csv(filepath:str, stopor:int=-7)-> pd.DataFrame:
# shared_folder_path = './data/'

# data_path = shared_folder_path + "web_attacks_balanced.csv"
    data = pd.read_csv(filepath).replace([np.inf, -np.inf], np.nan).dropna(how="any")
    data = data.iloc[:, :stopor]
    _ = data.pop('Label')
    return data


def preprocessor(data: pd.DataFrame, stopor:int=3000):
    #convert data from pd to numpy arrary
    neuron_data = data[:stopor].to_numpy()

    neuron_data=neuron_data.astype('float32')
    #normalize data
    neuron_data = normalize(neuron_data, axis=1, norm='l1')
    #reshape data to 3D (потому что в основе и первым слоем идет сверточная нейронная сеть (она работает с фото))
    neuron_data=neuron_data.reshape(neuron_data.shape[0],neuron_data.shape[1],1)
    
    return neuron_data
