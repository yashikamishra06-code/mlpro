from flask import Flask,request,render_template
from src.pipelines.predict_pipeline import predict
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('home.html')
    else:
        gender=request.form.get('gender')
        race=request.form.get('race or ethnicity')
        parental=request.form.get('parental level of education')
        lunch=request.form.get('lunch type')
        course=request.form.get('Test preparation Course')
        reading=request.form.get('reading score out of 100')
        writing=request.form.get('writing score out of 100')
        ans=predict(gender,race,parental,lunch,course,reading,writing)
        return render_template('home.html',ans=ans)
if __name__=='__main__':
    app.run()