import os

import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.backend import set_session

MODEL_NAME = 'mnist.h5'

model = None
graph = None
sess = None


def init():
    global model
    global graph
    global sess
    print("Loading Model")
    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.getcwd())
    model_path = os.path.join(os.getcwd(), 'app','model', MODEL_NAME)
    sess = tf.Session()
    set_session(sess)
    m = keras.models.load_model(model_path)
    model = m

    graph = tf.get_default_graph()
    print('Model Loaded')


def get_model():
    global model
    global graph
    global sess
    return (model, graph, sess)
    # return model
