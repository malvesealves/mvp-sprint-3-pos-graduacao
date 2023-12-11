import numpy as np
import pandas as pd
import pickle
from logger import logger
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

class Model:    
    def carrega_modelo(self, path):
        """Carrega o modelo pkl
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(self, model, form):
        """Realiza a predição de classificação um vinho com base no modelo treinado
        """
        X_input = np.array([form.preg, 
                            form.plas, 
                            form.pres, 
                            form.skin, 
                            form.test, 
                            form.mass, 
                            form.pedi, 
                            form.age
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])