#https://www.trading-attitude.com/comment-lancer-un-script-python-depuis-google-sheets
# le port local de la web app est http://127.0.0.1:5000
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def launch():
    # Specify the path to your .bat or .cmd file

    try:
        return '{"data": "Hello, World!", "data2": "coucou"}'       
        
    
    except Exception as e:
        msg = f"An error occurred: {str(e)}"
        return msg
    
    
if __name__ == '__main__':
    # Run the Flask application    
    app.run(debug=True)
