from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from random import choice, sample

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    workouts = db.relationship('Workout', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.email}', '{self.name}')"
    

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pushups = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Workout('{self.pushups}', '{self.comment}', '{self.date_posted}')"
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return redirect(url_for('login'))

        login_user(user, remember=remember)
        return redirect(url_for('profile'))

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            return redirect(url_for('signup'))

        new_user = User(email=email, name=name, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')


randomdatas = [
    {"username": "rasxy45", "workout": 45, "Comment": "What should I do next?"},
    {"username": "fitman24", "workout": 30, "Comment": "Just finished my cardio."},
    {"username": "runnergirl99", "workout": 60, "Comment": "Morning run complete!"},
    {"username": "gymbro89", "workout": 50, "Comment": "Crushed my leg day."},
    {"username": "healthqueen", "workout": 40, "Comment": "Yoga session done!"},
    {"username": "musclemax", "workout": 55, "Comment": "Upper body pump!"},
    {"username": "yogimaster", "workout": 35, "Comment": "Stretching and meditation."},
    {"username": "joggerjane", "workout": 25, "Comment": "Light jog today."},
    {"username": "liftlord", "workout": 70, "Comment": "Heavy lifting completed."},
    {"username": "cardioking", "workout": 45, "Comment": "Sweated through my HIIT workout."},
    {"username": "zenyogi", "workout": 20, "Comment": "Peaceful yoga session."},
    {"username": "runnerguy22", "workout": 90, "Comment": "Long-distance run today."},
    {"username": "weightsqueen", "workout": 50, "Comment": "Strength training session."},
    {"username": "cyclistpro", "workout": 80, "Comment": "Great cycling route today!"},
    {"username": "boxingchamp", "workout": 60, "Comment": "Boxing training done."},
    {"username": "pilatesguru", "workout": 40, "Comment": "Pilates class was intense."},
    {"username": "marathonmike", "workout": 100, "Comment": "Marathon training is on track."},
    {"username": "swimmerjoe", "workout": 45, "Comment": "Laps in the pool today."},
    {"username": "powerliftpat", "workout": 65, "Comment": "Deadlift PR achieved."},
    {"username": "fitnessfan", "workout": 30, "Comment": "Quick home workout done."},
    {"username": "athleteann", "workout": 55, "Comment": "Cross-training complete."},
    {"username": "spinfanatic", "workout": 75, "Comment": "Spinning class was intense."},
    {"username": "dancemaster", "workout": 50, "Comment": "Dance workout complete."},
]

@app.route('/workouts')
def user_workouts():
    selected_post = sample(randomdatas, min(len(randomdatas), choice([3])))
    return render_template('postfeed.html', postfeed=selected_post)

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new_workout():
    if request.method == 'POST':
        pushups = request.form.get('pushups')
        comment = request.form.get('comment')

        workout = Workout(pushups=pushups, comment=comment, author=current_user)
        db.session.add(workout)
        db.session.commit()

        flash('Your workout has been added!')
        return redirect(url_for('profile'))

    return render_template('createworkout.html')


@app.route('/profile')
@login_required
def profile():
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(email=current_user.email).first_or_404()
    workouts = Workout.query.filter_by(author=user).paginate(page=page, per_page=3)
    return render_template('profile.html', workouts=workouts, user=user, name=current_user.name)


@app.route("/workout/<int:workout_id>/update", methods=['GET', 'POST'])
@login_required
def update_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    if request.method == 'POST':
        workout.pushups = request.form['pushups']
        workout.comment = request.form['comment']
        db.session.commit()
        flash('Your workout has been updated!')
        return redirect(url_for('profile'))
    return render_template('updateworkout.html', workout=workout)


@app.route("/workout/<int:workout_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    flash('Your post has been deleted!')
    return redirect(url_for('profile'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/aboutMe')
def goto():
    return redirect('https://sumit0ubey.github.io/My_Portfolios/')

@app.route('/resume')
def resume():
    return redirect('https://drive.google.com/file/d/1NeisIU_PnfXjH9hABX-ggmUbAzQY05Si/view?usp=sharing')

if __name__ == '__main__':
    app.run(debug=True)
