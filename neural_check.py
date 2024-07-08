import time
from datetime import datetime, timezone

from tensorflow import keras
import numpy as np


def neurol_check(data, unique_labels:list, model_path:str)-> tuple[list, int]:
    
    attack_list = []
    model = keras.models.load_model(model_path)
    
    result = model.predict(data)
    
    attack_count = 0 
    for i in range(len(result)):
        max_v = np.where(result[i] == np.amax(result[i]))[0][0]
        if max_v != 0:
            attack_count += 1
            print(f"Обнаружена атака формата {unique_labels[max_v]}")
            attack_time = str(
                datetime.fromtimestamp(time.time(), timezone.utc) 
            ).replace(':','-')
            attack_list.append([unique_labels[max_v], attack_time])
    if attack_count == 0:
        print(f"Атак не обноруженно")
    # attack_count = 0
    
    return attack_list, attack_count