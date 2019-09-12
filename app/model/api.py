import io
import json
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.python.keras.backend import set_session
import numpy as np
from .model import get_model


def predict_ans(img):
    
    # model = get_model()
    model, graph, sess = get_model()
    
    img_raw = io.BytesIO(img)

    #Loading -> Shaping -> Array Convertion -> Normalizing (28, 28, 1)
    imgX = image.img_to_array(image.load_img(img_raw, target_size=(28, 28), color_mode='grayscale')) / 255  

    # Reshaping in (1, 28, 28)
    imgX = imgX.reshape(1, 28, 28)
    
    #Prediction
    # model.predict(imgX)
    with graph.as_default():
        set_session(sess)
        pred = model.predict(imgX)

    return pred.tolist()


def create_output(pred):
    v = int(np.argmax(pred))
    l = [[j, i] for j,i in enumerate(pred)]
    d = {'val': v, 'val_prob': pred[v], 'probs': l}
    
    return d