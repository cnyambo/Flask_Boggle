from crypt import methods
from flask import Flask, request, redirect, render_template, session, jsonify,json
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "123@45#"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

boggle_game = Boggle()



	

@app.route('/')
def index():
    board = boggle_game.make_board()
    session['board'] = board
    score = 0
    session['score'] = score
    session['result']=[] 
    
    return render_template('index.html', board=board)
 
@app.route('/process', methods=['POST'])
def process():
 
    word = request.form['word']
    print(word)
    result = boggle_game.check_valid_word( session['board'], word)
    print("****************word*******************") 
    print(f"word: {word}, result: {result}")
    print("****************word*******************") 
    score = session['score']
    new_word = {word.upper():result }
    if  word and result=='ok':
        res = session['result']
        
        if word in res:
            new_word[word.upper()] = f"{word.upper()} already added"
            return jsonify(worning=new_word )  
        
        

        else:
            score +=1
            new_word['score'] = score
            session['score'] =score 
            res.append(word.upper())
            session['result'] = res 
            return jsonify(word=new_word ) 
             
    return jsonify(error=new_word)