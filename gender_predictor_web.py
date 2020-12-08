from flask import Flask, request, render_template,jsonify
import pickle
import sys
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

def do_something(text1):
    loaded_model = pickle.load(open('finalized_model1.pkl', 'rb'))
    cv = pickle.load(open('vectorizer1.pkl', 'rb'))
    text1 = text1.upper()
    sample_name = [text1]
    vect = cv.transform(sample_name).toarray()
   # print(loaded_model.predict(vect))
    combine = loaded_model.predict(vect)
    if str(combine[0]) == '1':
        return text1+' :  MALE'
    else:
        return text1+' :  FEMALE'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/join', methods=['GET','POST'])
def my_form_post():
    # text1 = request.form['text1']
    text1 = request.args.get('text1')
    province = request.args.get('province')
    st = text1+' '+province
    combine = do_something(st)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    # return jsonify(result=result)
    if "FEMALE" in combine:
        return render_template("female.html",result=combine)
    else:
        return render_template("male.html", result=combine)

if __name__ == '__main__':
    app.run()