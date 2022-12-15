import json
import pickle
import numpy as np


__cuts = None
__data_columns = None
__model = None


def get_diamond_price(vari1,vari2,vari3,vari4):
    try:
        loc_index = __data_columns.index(vari1.lower())
    except:
        loc_index= -1

    x = np.zeros(len(__data_columns))
    x[0] = vari2
    x[1] = vari3
    x[2] = vari4
    if loc_index >= 0:
        x[loc_index] = 1
    print(" EL PRECIO DEL DIAMANTE ES: ")
    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("loading...")
    global __data_columns
    global __cuts
    
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __cuts = __data_columns[3:]
      
    global __model
    if __model is None:
        with open("./artifacts/diamond_prediction.pickle","rb") as f:
            __model = pickle.load(f)
    print("load done")


def get_cuts_names():
    global __cuts
    return __cuts
    
def get_data_columns():
    return __data_columns

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_cuts_names())
    print(get_diamond_price("cut_ideal" ,-1.2, 0.2, -0.7))
   # predict_price("cut_Ideal" ,-1.2, 0.2, -0.7)
    print(get_diamond_price("cut_Very Good" ,0.9, 0.8, -1.5))
    #print(get_diamond_price("cut_Ideal",-0.2,-0.8,0.2))
    
    