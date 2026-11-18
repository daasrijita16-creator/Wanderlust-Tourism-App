from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret123"

# ======================
# DATABASE CONFIG
# ======================
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/tourism_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ======================
# MODELS
# ======================

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class Package(db.Model):
    __tablename__ = 'packages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(50))
    image_url = db.Column(db.String(255))


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id'))


# ======================
# AUTH
# ======================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(
            username=request.form['username'],
            password=request.form['password']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()

        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect('/')

        return "Invalid login"

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ======================
# HOME + SEARCH + FILTER
# ======================

@app.route('/')
def index():
    search = request.args.get('search')
    country = request.args.get('country')

    query = Package.query

    # 🔍 SEARCH FIX
    if search:
        query = query.filter(
            (Package.title.ilike(f"%{search}%")) |
            (Package.description.ilike(f"%{search}%"))
        )

    # 🌍 COUNTRY FILTER
    elif country:
        query = query.filter(Package.title.ilike(f"%{country}%"))

    packages = query.all()

    return render_template('index.html', packages=packages)


# ======================
# DASHBOARD
# ======================

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    packages = Package.query.all()
    return render_template('dashboard.html', packages=packages)


# ======================
# ADD PACKAGE
# ======================

@app.route('/add', methods=['GET', 'POST'])
def add_package():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        pkg = Package(
            title=request.form['title'],
            description=request.form['description'],
            price=request.form['price'],
            duration=request.form['duration'],
            image_url=request.form['image_url']
        )
        db.session.add(pkg)
        db.session.commit()
        return redirect('/dashboard')

    return render_template('add_package.html')


# ======================
# EDIT PACKAGE
# ======================

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_package(id):
    if 'user_id' not in session:
        return redirect('/login')

    pkg = Package.query.get_or_404(id)

    if request.method == 'POST':
        pkg.title = request.form['title']
        pkg.description = request.form['description']
        pkg.price = request.form['price']
        pkg.duration = request.form['duration']
        pkg.image_url = request.form['image_url']

        db.session.commit()
        return redirect('/dashboard')

    return render_template('edit_package.html', pkg=pkg)


# ======================
# DELETE PACKAGE
# ======================

@app.route('/delete/<int:id>')
def delete_package(id):
    if 'user_id' not in session:
        return redirect('/login')

    pkg = Package.query.get_or_404(id)
    db.session.delete(pkg)
    db.session.commit()
    return redirect('/dashboard')


# ======================
# BOOK PACKAGE
# ======================

@app.route('/book/<int:package_id>')
def book(package_id):
    if 'user_id' not in session:
        return redirect('/login')

    booking = Booking(
        user_id=session['user_id'],
        package_id=package_id
    )

    db.session.add(booking)
    db.session.commit()

    return redirect('/my-bookings')


# ======================
# MY BOOKINGS
# ======================

@app.route('/my-bookings')
def my_bookings():
    if 'user_id' not in session:
        return redirect('/login')

    bookings = db.session.query(Booking, Package).join(
        Package, Booking.package_id == Package.id
    ).filter(Booking.user_id == session['user_id']).all()

    return render_template('my_bookings.html', bookings=bookings)

@app.route('/cancel-booking/<int:booking_id>')
def cancel_booking(booking_id):
    if 'user_id' not in session:
        return redirect('/login')

    booking = Booking.query.get_or_404(booking_id)

    # only allow user to delete own booking
    if booking.user_id != session['user_id']:
        return "Unauthorized"

    db.session.delete(booking)
    db.session.commit()

    return redirect('/my-bookings')

# ======================
# RUN APP
# ======================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # auto create tables if not exist

    app.run(debug=True)