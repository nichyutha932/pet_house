# Previous imports remain...
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
=======
from flask import Flask, render_template, request, jsonify
>>>>>>> 208ca06e742a37a76abbcf00cbd8671c75a8b2b4
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
<<<<<<< HEAD
app.secret_key = "pets list"
=======
>>>>>>> 208ca06e742a37a76abbcf00cbd8671c75a8b2b4


class PetModel(db.Model):
    __tablename__ = 'pet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    type = db.Column(db.String())
    breed = db.Column(db.String(), default=False)
    description = db.Column(db.String())
    hobby = db.Column(db.String())
    vaccination = db.Column(db.String())

    def __init__(self, name, type, breed, description, hobby, vaccination):
        self.name = name
        self.type = type
        self.breed = breed
        self.description = description
        self.hobby = hobby
        self.vaccination = vaccination

    def __repr__(self):
        return f" {self.name}"

    def get_one(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'breed': self.breed,
            'description': self.description,
            'hobby': self.hobby,
            'vaccination': self.vaccination,
        }


class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=passw).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                return 'Dont Loginadfsdafasdfasdf'
        except Exception as e:
            print(e)
            return "Dont now"


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        new_user = User(
            username=request.form['username'],
            password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


@app.route('/api/pets', methods=['POST'])
def save_pets():
    temp = request.form['data']
    temp = json.loads(temp)
    pet = PetModel(temp['name'], temp['type'],
                   temp['breed'], temp['description'], temp['hobby'], temp['vaccination'])
    db.session.add(pet)
    db.session.commit()
    res = {}
    res['success'] = True
    return pet.get_one()


@app.route('/api/pets/<int:id>', methods=['PUT'])
def put_pets(id):
    temp = request.form['data']
    temp = json.loads(temp)
    db_pet = PetModel.query.filter_by(id=id).first()
    db_pet.name = temp['name']
    db_pet.type = temp['type']
    db_pet.breed = temp['breed']
    db_pet.description = temp['description']
    db_pet.hobby = temp['hobby']
    db_pet.vaccination = temp['vaccination']
    db.session.commit()
    return db_pet.get_one()


@app.route('/api/pets/<int:id>', methods=['GET'])
def get_pet_detail(id):
<<<<<<< HEAD
    if session.get('logged_in'):
        db_pet = PetModel.query.filter_by(id=id).first()
        return render_template("pet_detail.html", pet_detail=db_pet.get_one())
    else:
        return redirect(url_for('login'))
=======
    db_pet = PetModel.query.filter_by(id=id).first()
    return render_template("pet_detail.html", pet_detail=db_pet.get_one())
>>>>>>> 208ca06e742a37a76abbcf00cbd8671c75a8b2b4


@app.route('/api/pets/<int:id>/vaccination', methods=['GET'])
def get_pet_vaccination(id):
<<<<<<< HEAD
    if session.get('logged_in'):
        db_pet = PetModel.query.filter_by(id=id).first()
        pet_detail = db_pet.get_one()
        return render_template("Vaccination_detail.html", pet_detail=db_pet.get_one())
    else:
        return redirect(url_for('login'))
=======
    db_pet = PetModel.query.filter_by(id=id).first()
    pet_detail = db_pet.get_one()
    return render_template("Vaccination_detail.html", pet_detail=db_pet.get_one())
>>>>>>> 208ca06e742a37a76abbcf00cbd8671c75a8b2b4


@app.route('/api/pets/<int:id>', methods=["DELETE"])
def delete_pets(id):
<<<<<<< HEAD
    if session.get('logged_in'):
        PetModel.query.filter_by(id=id).delete()
        db.session.commit()
        res = {}
        res['success'] = True
        return res
    else:
        return redirect(url_for('login'))
=======
    PetModel.query.filter_by(id=id).delete()
    db.session.commit()
    res = {}
    res['success'] = True
    return res
>>>>>>> 208ca06e742a37a76abbcf00cbd8671c75a8b2b4


@app.route('/api/pet_one', methods=['POST'])
def pet_one():
<<<<<<< HEAD
    if session.get('logged_in'):
        temp = request.form['data']
        temp = json.loads(temp)
        db_pet = PetModel.query.filter_by(id=int(temp['id'])).first()
        return db_pet.get_one()
    else:
        return redirect(url_for('login'))
=======
    temp = request.form['data']
    temp = json.loads(temp)
    db_pet = PetModel.query.filter_by(id=int(temp['id'])).first()
    return db_pet.get_one()
>>>>>>> 208ca06e742a37a76abbcf00cbd8671c75a8b2b4


@app.route('/api/pets')
def get_pets():
<<<<<<< HEAD
    if session.get('logged_in'):
        page = request.args.get('page', 1, type=int)

        pet_list = PetModel.query.paginate(page=page, per_page=10)

        return render_template("pet_list.html", pet_list=pet_list)
    else:
        return redirect(url_for('login'))
=======
    page = request.args.get('page', 1, type=int)

    pet_list = PetModel.query.paginate(page=page, per_page=10)

    return render_template("pet_list.html", pet_list=pet_list)
>>>>>>> 208ca06e742a37a76abbcf00cbd8671c75a8b2b4


@app.route('/')
def home():
<<<<<<< HEAD
    # if not session.get('logged_in'):
=======
>>>>>>> 208ca06e742a37a76abbcf00cbd8671c75a8b2b4
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
