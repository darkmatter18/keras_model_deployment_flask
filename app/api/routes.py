from flask import request, Blueprint, jsonify
from app.model.api import predict_ans, create_output
     
api_blueprint = Blueprint('api', __name__)

"""
API endpoint for predict
"""
@api_blueprint.route('/predict', methods=['POST'])
def predict_method():
    if request.method == 'POST':
        file = request.files['image']
        if file.filename == '':
            print('No selected file')
            return 'No selected file'
        img = request.files['image'].read()
        
        pred = predict_ans(img)
        pred = create_output(pred[0])
        
        return jsonify(pred)
    else:
        return "The Predict method only supports POST"

