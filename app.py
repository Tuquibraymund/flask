from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return ('Raymund B. Tuquib,'
            '3rd Year A 2nd 25,'
            'System Integration and Architecture 1,'
            'Semi-Finals Exam')

if __name__ == '__main__':
    port = int(os.eviron.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)