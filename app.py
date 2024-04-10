#https://www.trading-attitude.com/comment-lancer-un-script-python-depuis-google-sheets
# le port local de la web app est http://127.0.0.1:5000
from flask import Flask
import socket
import subprocess

app = Flask(__name__)

@app.route('/')
def launch():
    # Specify the path to your .bat or .cmd file

    try:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 9100
        mysocket.connect(("172.31.40.105", port))
        contenu = f'''^XA
    ^XFE:TEMPLATE.ZPL^FS
    ^FN1^FDJohn^FS
    ^FN2^FDDoe^FS
    ^PQ1
    ^XZ'''.encode()
        mysocket.send(contenu)
        mysocket.close() # fermeture de la connexion
        return '{"data": "Version 2"}'       
        
    
    except Exception as e:
        msg = f"An error occurred: {str(e)}"
        return msg


    
    
if __name__ == '__main__':
    # Run the Flask application    
    app.run()#debug=True
