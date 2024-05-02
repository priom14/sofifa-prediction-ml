from flask import Flask, request, render_template, url_for

from src.pipeline.predict_pipeline import CustomData,PredictPipieline


app = Flask(__name__)


@app.route('/')
def home():    
    return render_template("home.html")

@app.route("/predict_data", methods = ['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        name = request.form['name']
        position1 = str(request.form['position1'])
        position2 = request.form['position2']
        age = int(request.form['age'])
        base_potential = int(request.form['base_potential'])
        potential = int(request.form['potential'])
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        preferred_foot = request.form['preferred_foot']
        wage = int(request.form['wage'])
        release_clause = int(request.form['release_clause'])

        
        data = CustomData(
            pos1 = position1,
            age = age,
            base_potential = base_potential,
            potential = potential,
            growth = potential - base_potential,
            height = height,
            weight = weight,
            foot= preferred_foot,
            wage = wage,
            release_clause = release_clause
        )
        
        pred_df= data.get_data_as_dataframe()
        print(pred_df)
        
        predict_pipeline = PredictPipieline()
        predicted_market_value = predict_pipeline.predict(pred_df)
        formatted_market_value = "{:.2f}".format(predicted_market_value[0])
        
    return render_template("predict.html", predicted_market_value=formatted_market_value) 



if __name__ == "__main__":
    app.run(debug=True)
    
