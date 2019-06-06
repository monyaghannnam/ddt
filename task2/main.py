import random
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/get/<int:array_length>', methods=['GET'])
def get(array_length):
    """rest api fill array with random number
    :param array_length:length of array
    :return:json object of filled array
    """
    if array_length <0:
        return jsonify({'result':"array_length cant be negative"})
    elif type(array_length) in [str,float,None]:
        return jsonify({'result':"array_length must be non-negative int"})

    arr=[]
    for i in range(array_length):
        arr.append(random.randint(0, 10))
    return jsonify({'arr':arr})




def main():
    app.run(debug=True)

if __name__=="__main__":
    main()