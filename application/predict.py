import onnxruntime as rt
import pandas as pd
import pickle

from models import HousingFeatures, AreaFeatures
from models import PredictionResult
# from loadpickle import LoadPickle

import config as config

sess = rt.InferenceSession(config.MODEL_PATH)
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name


def predict(data: HousingFeatures) -> PredictionResult:
    predicted = sess.run([label_name], {input_name: data.to_numpy()})[0]
    print (f'predicted {predicted}')
    return PredictionResult(**{"predicted": float(predicted[0][0])})

def predictpickle(area: AreaFeatures, picklemodel: str) -> PredictionResult:

    input_data = [[area]]

    inheritedmodel = picklemodel

    X_df_new = pd.DataFrame(input_data, columns=['area'])
    predicted_price = int(inheritedmodel.predict(X_df_new)[0].round(0))

    return PredictionResult(**{"predicted": predicted_price})