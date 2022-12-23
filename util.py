import json
import pickle
import numpy as np
import pandas as pd

__data_columns = None
__model = None

def get_diamond_price(vari1,vari2,vari3,vari4):
    datacolumns = ["carat", "depth", "table", "cut_Fair", "cut_Good", "cut_Ideal", "cut_Premium", "cut_Very Good"]
    try:
        loc_index = datacolumns.index(vari1)
    except:
        loc_index= -1
    
    #Standarization:
    vari2=(vari2 - 0.797935)/0.473999	
    vari3=(vari3 - 61.749322)/1.432626
    vari4=(vari4 - 57.457251)/2.234549

    x = [0,0,0,0,0,0,0,0]
    x[0] = float(vari2)
    x[1] = float(vari3)
    x[2] = float(vari4)
    if loc_index >= 0:
        x[loc_index] = 1
    x = np.array(x)

    pandazo = pd.DataFrame(x.reshape(1,-1),columns=["carat", "depth", "table", "cut_Fair", "cut_Good", "cut_Ideal", "cut_Premium", "cut_Very Good"])
    predo = __model.predict(pandazo)[0]
    predo = float(predo)
    return predo

def load_saved_artifacts():
    print("loading...")
    global __data_columns
    
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)["data_columns"]
      
    global __model
    if __model is None:
        with open("diamond_prediction.pickle","rb") as f:
            __model = pickle.load(f)

   
def get_data_columns():
    return __data_columns

if __name__ == "__main__":
    load_saved_artifacts()
    # print(get_cuts_names())
    print(get_diamond_price("cut_Ideal" ,20, 500, 300))
   # predict_price("cut_Ideal" ,-1.2, 0.2, -0.7)
    print(get_diamond_price("cut_Very Good" ,15, 600, 20))
    #print(get_diamond_price("cut_Ideal",-0.2,-0.8,0.2))
    
    
    
