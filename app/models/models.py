from datetime import datetime
from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from passlib.hash import pbkdf2_sha256
from .connection import db
import uuid

userDB = db['users']
codesDB = db['codes']

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
            return redirect(url_for('bp.register', error="email_taken"))

        if userDB.insert_one(user):
            
            self.start_session(user)
            return render_template('login.html')
            #return jsonify(user), 200
        
        return redirect(url_for('bp.register', error="registration_failed"))
    
    def signout(self):
        session.clear()
        return render_template('login.html')
    
    def login(self):
        user = userDB.find_one({'email': request.form['email']})

        if user and pbkdf2_sha256.verify(request.form['password'], user['password']):
            self.start_session(user)
            return redirect(url_for('bp.home'))
        
        return redirect(url_for('bp.login', error="invalid_credentials"))
    
    def update_exercise(self, value):

        try:
            update_query = {f"exercise.{value}": True}
            result = userDB.update_one(
                {"_id": session['user']['_id']},
                {"$set": update_query}
            )
            if result.matched_count > 0:
                user = userDB.find_one({'_id': session['user']['_id']})
                self.start_session(user)
                print(f"Documento actualizado exitosamente. Índice {value} ahora tiene el valor {True}.")
            else:
                print("No se encontró el documento.")

        except Exception as e:
            print(f"Error al conectar o actualizar: {e}")

    def get_user(self):
        user = userDB.find_one({'_id': session['user']['_id']})
        del user['password']
        return user

class Codes():

    def submit_code(self, data):

        current_datetime = datetime.now()
        date = current_datetime.strftime('%Y-%m-%d')
        time = current_datetime.strftime('%H:%M:%S')

        codeData = {

            '_userId': session['user']['_id'],
            'code': data['code'],
            'tests': data['test'],
            'idExercise': data['id'],
            'problem': data['problem'],
            'language': data['language'],
            'date': date,
            'time': time
        }
        if codesDB.insert_one(codeData):
            print("Success")
        else:
            print("Failed")
    
    def get_codes(self, index):

        codes = list(codesDB.find({'_userId': session['user']['_id'], 'idExercise': str(index-1)}))
        return codes