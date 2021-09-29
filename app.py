# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:40:20 2021

@author: sush1
"""

import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, render_template

app=Flask(__name__)

def charcters_ofthe_password(pwds):
    pass_char=[]
    for char in pwds:
        pass_char.append(char)
        
    return pass_char

@app.route('/')
def home():
    return render_template('home.html', measure="")

@app.route('/checkstrength', methods=['Get','POST'])
def checkStrength():
    if request.method == 'POST':
        password = request.form['pwd']
        confirm_password = request.form['confirmPassword']
        
        if password != confirm_password:
            return render_template('home.html', message='Passwords are not matching')
        else:
            input_pwd = np.array([password])
            # load the model from disk
            loaded_model = pickle.load(open('passwordtsrengthXGB.pkl', 'rb'))
            prediction = loaded_model.predict(input_pwd)
            if prediction == 0:
                strength_message="Weak"
            elif prediction == 1:
                strength_message="Medium"
            else:
                strength_message="Strong"
            return render_template('strengthmeasure.html',password= password,measure=strength_message)
    
if __name__=='__main__':
    
    app.run(host='localhost',port=8000)
    