import string
import re
import hashlib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from flask import Flask, request, jsonify, render_template

def check_password_strength(password):
    # Define character types using regex
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'[0-9]')
    special_regex = re.compile(r'[{}]'.format(re.escape(string.punctuation)))
    
    character_types = [bool(uppercase_regex.search(password)),
                       bool(lowercase_regex.search(password)),
                       bool(digit_regex.search(password)),
                       bool(special_regex.search(password))]

    length = len(password)

    with open('passwords.txt', 'r', encoding='utf-8') as f:
        common_passwords = f.read().splitlines()

    if password in common_passwords:
        print("Your password was found in the common list. Score 0 / 7")
        return

    # Calculate score based on length
    score = 0
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length >= 24:
        score += 1

    # Calculate score based on character types
    score += sum(character_types)
    print(f"Password length is {length}, adding {score} points!")
    print(f"Password contains {sum(character_types)} different character types.")

    # Password strength score
    if score < 4:
        print(f"Your Password Score: {score} / 7")
    elif score == 4:
        print(f"Your Password Score: {score} / 7")
    elif 4 < score < 6:
        print(f"Your Password Score: {score} / 7")
    elif score > 6:
        print(f"Your Password Score: {score} / 7")

def train_model():
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        passwords = f.read().splitlines()
    X = np.array([list(map(len, passwords))]).T
    y = np.array([int(p in common_passwords) for p in passwords])

    # RandomForestClassifier
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_strength', methods=['POST'])
def check_strength():
    password = request.form['password']
    hashed_password = hash_password(password)
    return jsonify({'strength': 'strong'})

if __name__ == "__main__":
    with open('passwords.txt', 'r', encoding='utf-8') as f:
        common_passwords = set(f.read().splitlines())

    train_model()
    
    # Run Flask
    app.run(debug=True)
