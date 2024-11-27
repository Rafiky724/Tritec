from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from passlib.hash import pbkdf2_sha256
from .connection import db
import uuid

userDB = db['users']

class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        #return jsonify(user), 200

    def register(self):
        ejercicio_inicial = [False] * 10
        user = {

            "_id": uuid.uuid4().hex,
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password'],
            "exercise": ejercicio_inicial

        }

        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if userDB.find_one({'email': user['email']}):
            return jsonify({"message": "El correo electrónico ya está en uso"}), 400

        if userDB.insert_one(user):
            
            self.start_session(user)
            return render_template('login.html')
            #return jsonify(user), 200
        
        return jsonify({"error": "El registro falló"}), 400
    
    def signout(self):
        session.clear()
        return render_template('login.html')
    
    def login(self):
        user = userDB.find_one({'email': request.form['email']})

        if user and pbkdf2_sha256.verify(request.form['password'], user['password']):
            self.start_session(user)
            return redirect(url_for('bp.home'))
        
        return jsonify({"message": "Correo electrónico o contraseña incorrectos"}), 401