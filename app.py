from flask import Flask, request, render_template
import pickle
import sklearn
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def loadPage():
    return render_template('home.html')


@app.route("/", methods=['GET','POST'])
def predict():
    Database = str(request.form.get('Database'))
    Dealer = int(request.form.get('Dealer'))
    Cloud_Partner = str(request.form.get('Cloud Partner'))
    Training_Provided = str(request.form.get('Training Provided'))
    tenure = int(request.form.get('tenure'))
    Recently_updated = str(request.form.get('Recently updated'))
    Catalog_Type = str(request.form.get('Catalog Type'))
    Region = str(request.form.get('Region'))
    Licence_Security = str(request.form.get('Licence Security'))
    Catalog_Locking = str(request.form.get('Catalog Locking'))
    Licence_Protection = str(request.form.get('Licence Protection'))
    TechSupport = str(request.form.get('TechSupport'))
    Cloud_Pulished = str(request.form.get('Cloud Pulished'))
    GSV_added = str(request.form.get('GSV added'))
    PaperlessBilling = str(request.form.get('PaperlessBilling'))
    PaymentMethod = str(request.form.get('PaymentMethod'))
    MonthlyHours = float(request.form.get('MonthlyHours'))
    TotalHours = float(request.form.get('TotalHours'))

    result=model.predict([['Database', 'Dealer', 'Cloud Partner',
       'Training Provided', 'tenure', 'Recently updated', 'Catalog Type',
       'Region', 'Licence Security', 'Catalog Locking',
       'Licence Protection', 'TechSupport', 'Cloud Pulished', 'GSV added',
       'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyHours',
       'TotalHours']])

    if result[0] == 1:
        result = 'Churn'
    else:
        result = 'not Churn'

    return render_template('home.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8082)
