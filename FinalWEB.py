from flask import Flask, render_template,request
import pickle
app = Flask(__name__)
@app.route("/")


def hello_world():
    title = "Fake News"
    heading = "Fake News Detector"
    return render_template('index.html')



@app.route('/submit', methods=['POST'])


def submit():
	from flask import jsonify
	if request.method == 'POST':
		text = request.form['text']
		load_model = pickle.load(open('final_model.sav', 'rb'))
		prediction = load_model.predict([text])
		prob = load_model.predict_proba([text])
		y=prob[0][1]
		if y<=0.50:
			x="FAKE"
		else:
			x="TRUE"
		return render_template('user_details.html', x=x, y=y)
	else:
		return render_template('index.html')
if __name__ == "__main__":
    app.debug = True
    app.run()