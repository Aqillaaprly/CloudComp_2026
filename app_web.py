from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    app_name = os.environ.get('APP_NAME', 'Default App')
    return f'''
    <h1>🚀 {app_name}</h1>
    <p>Deployment berhasil di Platform PaaS!</p>
    <p>Tugas 6 - Cloud Computing 2026</p>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)