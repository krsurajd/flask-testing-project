from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '-ako18bhoox0i*2)o%o6aqn1iw_!$2zue-z-jjx#lwl!vmwjdp'

posts = [
    {
        'author': 'Suraj Kumar',
        'title': 'Blog Post 1',
        'content': 'This is First blog created by me',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Mansi Dhingra',
        'title': 'Blog Post 2',
        'content': 'This blog created by mansi',
        'date_posted': 'April 21, 2020'
    }
]

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)

