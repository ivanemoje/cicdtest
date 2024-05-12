
import pandas as pd

# @celery.task(name="create_task", bind=True, )
def predict_model(self, area, model):
    # train and get the resulting metric and best model
    input_data = [[area]]
    X_df_new = pd.DataFrame(input_data, columns=['area'])
    predicted_price = int(model.predict(X_df_new)[0].round(0))
    
    return predicted_price

import pickle

def LoadPickle():
    """ https://stackoverflow.com/questions/74630503/how-to-send-pickle-file-to-fastapi-call-as-input
        https://redfoxsec.com/blog/insecure-deserialization-in-python/

    Pickle files not a secure format. 

    """
    # TODO: MOVE TO /models. ISSUE WITH THE PATH REFERENCE
    # TODO: TRY ./models/model.pkl
    model_file_path = f"pickles/model.pkl"
    with open(model_file_path , 'rb') as f:
        model = pickle.load(f)

    print ("Loading pickle...")

    return model

