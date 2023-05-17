from flask import *
from flask_socketio import *
import bcrypt
# import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# db_config = {
#     "host": "localhost",
#     "user": "dog",
#     "password": "dog",
#     "database": "chat"
# }
# conn = mysql.connector.connect(**db_config)

def login():
    if request.method == 'POST':
        user_password = request.form['password']
        password = user_password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

        # ログイン処理の実装

    return render_template('login.html')


# cursor = conn.cursor()

# query = "select * from userlogin"
# cursor.execute(query)

# result = cursor.fetchall()


# for row in result:
#     print(row)


# cursor.close()
# conn.close()


socketio = SocketIO(app)
@app.route('/')

def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)


