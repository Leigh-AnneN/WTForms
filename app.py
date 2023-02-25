from flask import Flask, url_for, render_template,  redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

###################################################

@app.route('/')
def list_pets():
    """Lists pets in DB"""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets = pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        newpet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(newpet)
        db.session.commit()
        return redirect ('/')
    else:
        return render_template('add.html', form = form)
    
@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet(id):
    """Show pet information and Edit pet"""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f" {pet.name} updated")
        return redirect('/')
    
    else: 
        return render_template("pet_edit_form.html", form=form, pet=pet)

