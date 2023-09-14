from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120))

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to 0x3Devoid HnG2-API CRUD'


@app.route('/people', methods=['GET'])
def get_people():
    people = Person.query.all()
    result = []
    for person in people:
        person_data = {
            'id': person.id,
            'name': person.name,
            'age': person.age,
            'email': person.email
        }
        result.append(person_data)
    return jsonify(result)


@app.route("/people/<int:id>", methods=["GET"])
def get_by_Id(id):
    person_id = Person.query.get(id)
    result = []
    if person_id:
         person_data = {
            'id': person_id.id,
            'name': person_id.name,
            'age': person_id.age,
            'email': person_id.email
        }
         result.append(person_data)
    else:
        error_data = {"error": f"Id number {id} doesnt exist"}
        return jsonify(error_data)
    return jsonify(result)

@app.route('/people', methods=['POST'])
def create_person():
    if request.method == "POST":
        data = request.get_json()
        new_person = Person(name=data['name'], age=data['age'], email=data['email'])
        db.session.add(new_person)
        db.session.commit()
        return jsonify({"message": 'Person created succesfully'}), 201

@app.route('/people/<int:id>', methods=['PUT'])
def update_person(id):
    person_to_update = Person.query.get(id)
    if not person_to_update:
        return jsonify({'message': 'Person doesnt exist'})
    data = request.get_json()
    person_to_update.name = data['name']
    person_to_update.age = data['age']
    person_to_update.email = data['email']
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'})

@app.route("/people/<int:id>", methods=['DELETE'])
def delete_person(id):
    person_to_delete = Person.query.get(id)
    if not person_to_delete:
        return jsonify({'message': 'Person doesnt exist'})
    db.session.delete(person_to_delete)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})





if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
