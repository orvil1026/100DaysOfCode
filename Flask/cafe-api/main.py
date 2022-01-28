from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
from distutils.util import strtobool

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


    def to_dict(self):

        dictionary = {}

        for column in self.__table__.columns:

            dictionary[column.name] = getattr(self, column.name)

        return dictionary

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)


    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def all():
    all_cafes = Cafe.query.all()
    cafe_list = []

    for cafe in all_cafes:
        cafe_list.append(cafe.to_dict())

    return jsonify(cafe=cafe_list)

@app.route("/search")
def search():
    location = request.args.get('loc', default='None', type=str)
    cafe_by_location = Cafe.query.filter_by(location=location).first()

    if cafe_by_location is None:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })

    return jsonify(cafe=cafe_by_location.to_dict())

## HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':

        try:
            new_cafe = Cafe(
                name=request.args.get('name'),
                map_url=request.args.get('map_url'),
                img_url=request.args.get('img_url'),
                location=request.args.get('location'),
                seats=request.args.get('seats'),
                has_toilet=strtobool(request.args.get('has_toilet')),
                has_wifi=strtobool(request.args.get('has_wifi')),
                has_sockets=strtobool(request.args.get('has_sockets')),
                can_take_calls=strtobool(request.args.get('can_take_calls')),
                coffee_price=request.args.get('coffee_price'),
            )

            db.session.add(new_cafe)
            db.session.commit()

        except Exception as e:
            print(e)
            return jsonify(response={
                'Error': "Error was faced."
            })
        else:
            return jsonify(response={
                "success": "Successfully added new cafe."
            })

## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    if request.method == "PATCH":
        cafe = Cafe.query.get(cafe_id)
        print(cafe_id)

        if cafe is None:
            return jsonify(response={
                'Error': "Id not found"
            }), 404
        else:
            cafe.coffee_price = request.args.get('new_price')
            db.session.commit()
            return jsonify(response={
                "success": "Successfully changed the price."
            })



## HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    if request.method == "DELETE":
        if request.args.get("api-key") == "TopSecretAPIKey":
            cafe_by_id = Cafe.query.get(cafe_id)

            if cafe_by_id is None:
                return jsonify(error={
                    'Not Found': "Id not found"
                }), 404
            else:
                db.session.delete(cafe_by_id)
                db.session.commit()
                return jsonify(response={
                    "success": "Successfully Deleted"
                })

        return jsonify(error= "Sorry , that's not allowed!"), 403


if __name__ == '__main__':
    app.run(debug=True)
