from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("front.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    

    if prediction==0:
        return render_template('front.html',pred='You Dont have Heart Faliure Desiese {}'.format(prediction),bhai="no heart desiese")
    else:
        return render_template('front.html',pred='You Have Chances Of Heart Faliure  Desiese Visit hosptial Asap {}'.format(prediction),bhai=" heart desiese")


if __name__ == '__main__':
    app.run(debug=True)