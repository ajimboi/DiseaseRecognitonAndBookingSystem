from django.shortcuts import render
import pandas as pd
from joblib import load



def index(request):
    return render(request, 'index.html')

def model1(request):
    model = load('model1.joblib')
    context = {}
    if request.method == 'POST':
        question_1 = int(request.POST['question_1'])
        question_2 = int(request.POST['question_2'])
        question_3 = int(request.POST['question_3'])
        question_4 = int(request.POST['question_4'])
        question_5 = int(request.POST['question_5'])
        question_6 = int(request.POST['question_6'])
        question_7 = int(request.POST['question_7'])
        question_8 = int(request.POST['question_8'])
        question_9 = int(request.POST['question_9'])

        data = pd.DataFrame({
            'Q1': [question_1],
            'Q2': [question_2],
            'Q3': [question_3],
            'Q4': [question_4],
            'Q5': [question_5],
            'Q6': [question_6],
            'Q7': [question_7],
            'Q8': [question_8],
            'Q9': [question_9]
        })
        
        predict = model.predict(data)
        if predict[0]==0:
            result = "Allergies is not detected"
        else:
            result = "Allergies is detected"    
        context = {'predict': result}
    return render(request, 'model1.html', context)
    
def model2(request):
    model = load('model2.joblib')
    context = {}
    if request.method == 'POST':
        question_1 = int(request.POST['question_1'])
        question_2 = int(request.POST['question_2'])
        question_3 = int(request.POST['question_3'])
        question_4 = int(request.POST['question_4'])
        question_5 = int(request.POST['question_5'])
        question_6 = int(request.POST['question_6'])
        question_7 = int(request.POST['question_7'])
        question_8 = int(request.POST['question_8'])

        data = pd.DataFrame({
            'Q1': [question_1],
            'Q2': [question_2],
            'Q3': [question_3],
            'Q4': [question_4],
            'Q5' : [question_5],
            'Q6': [question_6],
            'Q7': [question_7],
            'Q8': [question_8]
        })
        
        predict = model.predict(data)
        if predict[0]==0:
            result = "Colds and flu is not detected"
        else:
            result = "Colds and flu is detected" 
        context = {'predict': result}
    return render(request, 'model2.html',context)

def model3(request):
    model = load('model3.joblib')
    context = {}
    if request.method == 'POST':
        question_1 = int(request.POST['question_1'])
        question_2 = int(request.POST['question_2'])
        question_3 = int(request.POST['question_3'])
        question_4 = int(request.POST['question_4'])
        question_5 = int(request.POST['question_5'])
        question_6 = int(request.POST['question_6'])
        question_7 = int(request.POST['question_7'])
        question_8 = int(request.POST['question_8'])

        data = pd.DataFrame({
            'Q1': [question_1],
            'Q2': [question_2],
            'Q3': [question_3],
            'Q4': [question_4],
            'Q5' : [question_5],
            'Q6': [question_6],
            'Q7': [question_7],
            'Q8': [question_8]
        })
        predict = model.predict(data)
        if predict[0]==0:
            result = "Conjunctivitis is not detected"
        else:
            result = "Conjunctivitis is detected" 
        context = {'predict': result}
    return render(request, 'model3.html',context)

def model4(request):
    model = load('model4.joblib')
    context = {}
    if request.method == 'POST':
        question_1 = int(request.POST['question_1'])
        question_2 = int(request.POST['question_2'])
        question_3 = int(request.POST['question_3'])
        question_4 = int(request.POST['question_4'])
        question_5 = int(request.POST['question_5'])
        question_6 = int(request.POST['question_6'])
        question_7 = int(request.POST['question_7'])
        question_8 = int(request.POST['question_8'])

        data = pd.DataFrame({
            'Q1': [question_1],
            'Q2': [question_2],
            'Q3': [question_3],
            'Q4': [question_4],
            'Q5' : [question_5],
            'Q6': [question_6],
            'Q7': [question_7],
            'Q8': [question_8]
        })
        predict = model.predict(data)
        if predict[0]==0:
            result = "Diarrhea is not detected"
        else:
            result = "Diarrhea is detected" 
        context = {'predict': result}
    return render(request, 'model4.html',context)

def model5(request):
    model = load('model5.joblib')
    context = {}
    if request.method == 'POST':
        question_1 = int(request.POST['question_1'])
        question_2 = int(request.POST['question_2'])
        question_3 = int(request.POST['question_3'])
        question_4 = int(request.POST['question_4'])
        question_5 = int(request.POST['question_5'])
        question_6 = int(request.POST['question_6'])
        question_7 = int(request.POST['question_7'])
        question_8 = int(request.POST['question_8'])

        data = pd.DataFrame({
            'Q1': [question_1],
            'Q2': [question_2],
            'Q3': [question_3],
            'Q4': [question_4],
            'Q5' : [question_5],
            'Q6': [question_6],
            'Q7': [question_7],
            'Q8': [question_8]
        })
        predict = model.predict(data)
        if predict[0]==0:
            result = "Headaches is not detected"
        else:
            result = "Headaches is detected" 
        context = {'predict': result}
    return render(request, 'model5.html',context)

def model6(request):
    model = load('model6.joblib')
    context = {}
    if request.method == 'POST':
        question_1 = int(request.POST['question_1'])
        question_2 = int(request.POST['question_2'])
        question_3 = int(request.POST['question_3'])
        question_4 = int(request.POST['question_4'])
        question_5 = int(request.POST['question_5'])
        question_6 = int(request.POST['question_6'])
        question_7 = int(request.POST['question_7'])
        question_8 = int(request.POST['question_8'])

        data = pd.DataFrame({
            'Q1': [question_1],
            'Q2': [question_2],
            'Q3': [question_3],
            'Q4': [question_4],
            'Q5' : [question_5],
            'Q6': [question_6],
            'Q7': [question_7],
            'Q8': [question_8]
        })
        predict = model.predict(data)
        if predict[0]==0:
            result = "Mononucleosis is not detected"
        else:
            result = "Mononucleosis is detected" 
        context = {'predict': result}
    return render(request, 'model6.html',context)

def model7(request):
    model = load('model7.joblib')
    context = {}
    if request.method == 'POST':
        question_1 = int(request.POST['question_1'])
        question_2 = int(request.POST['question_2'])
        question_3 = int(request.POST['question_3'])
        question_4 = int(request.POST['question_4'])
        question_5 = int(request.POST['question_5'])
        question_6 = int(request.POST['question_6'])
        question_7 = int(request.POST['question_7'])
        question_8 = int(request.POST['question_8'])

        data = pd.DataFrame({
            'Q1': [question_1],
            'Q2': [question_2],
            'Q3': [question_3],
            'Q4': [question_4],
            'Q5' : [question_5],
            'Q6': [question_6],
            'Q7': [question_7],
            'Q8': [question_8]
        })
        predict = model.predict(data)
        if predict[0]==0:
            result = "Stomach ache is not detected"
        else:
            result = "Stomach ache is detected" 
        context = {'predict': result}
    return render(request, 'model7.html', context)