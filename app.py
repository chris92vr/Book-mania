import os
import math 
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from form import LoginForm, AddBookForm
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
def index():
    """ Returns the home page """
    
    # initializes page title
    page_title = "Home"
    # determines last 5 books books added 
    books = mongo.db.book.find().sort("_id", -1).limit(5)
    # renders the home page
    return render_template("index.html", books = books, page_title =
    page_title)

@app.route("/listing")
def listing():
    """ Returns the the added books """
    
    # initializes page title
    page_title = "Our Book Review"
    # determines books books added in descending order
    books = mongo.db.book.find().sort("_id", -1)
    # Pagination
    books_pagination = books.count()
    books_per_page = 6
    current_page = int(request.args.get("current_page", 1))
    num_pages = range(
    1, int(math.ceil(books_pagination / books_per_page)) + 1
    )
    books = books.skip((current_page - 1) * books_per_page).limit(books_per_page)
    # renders the the page with the added books
    return render_template("listing.html", books = books,
    current_page = current_page,
    pages = num_pages, page_title = page_title)

@app.route("/myreviews")
def myreviews():
    """ Returns the page with the books added by the logged in user profile """
    
    # initializes page title
    page_title = "My Reviews"
    # logged in user
    username = session["user"]
    #determines books added by the logged in user
    books = mongo.db.book.find({
        'created_by': username
    }).sort("_id", -1)
    n_books = mongo.db.book.find({'created_by': username}).count()
    # Pagination
    books_pagination = books.count()
    books_per_page = 6
    current_page = int(request.args.get("current_page", 1))
    num_pages = range(
        1, int(math.ceil(books_pagination / books_per_page)) + 1
    )
    books = books.skip((current_page - 1) * books_per_page).limit(
        books_per_page)
    # renders the the page with the books added by the logged in user
    return render_template("my_reviews.html", books = books, current_page = current_page, pages = num_pages, page_title = page_title,n_books=n_books)

@app.route("/browse/<book_id>")
def browse(book_id):
    """ Returns the page of a book  """

    book = mongo.db.book.find_one_or_404({
        '_id': ObjectId(book_id)
    })
    comments = mongo.db.comment.find({
    'book_id': ObjectId(book_id)
    })
    # initializes page title
    page_title = "View Book"
    book = mongo.db.book.find_one_or_404({'_id': ObjectId(book_id)})
    #increment books counter displayed by the connected user profile
    mongo.db.users.update({"username": session["user"]}, {"$inc": {"review_viewed": 1}})
    # renders the the page of corresponding book
    return render_template("browse.html", book = book, comments =
    comments, page_title = page_title)

@app.route('/search', methods=['GET', 'POST'])
def search():
    """ Search books by name and author  """

    # initializes page title
    page_title="Search book"
    search_input = request.form.get("search")
    #convert search input to string
    search_string = str(search_input)
    books = mongo.db.book.find().sort("_id", -1)
     # Pagination
    books_pagination = books.count()
    books_per_page = 6
    current_page = int(request.args.get("current_page", 1))
    num_pages = range(
        1, int(math.ceil(books_pagination / books_per_page)) + 1
    )
    books = books.skip((current_page - 1) * books_per_page).limit(
        books_per_page
    ) 
    # Previous index on all fields removed to narrow down the results
    # mongo.db.reviews.drop_index([('$**', 'text')])
    mongo.db.book.create_index([('book_author', 'text'), 
    ('book_name', 'text')])
    
    # Search results and sort by id
    search_results = mongo.db.book.find(
        {"$text": {"$search": search_string}}).sort([("_id", -1)])
    
    results_count = mongo.db.book.count_documents(
        {"$text": {"$search": search_string}})
    if request.method == 'POST':
        
        if results_count == 0:
            
            flash(f'No matching results found for "{search_input}". Please try a different search or browse through our collection', 'info')
            
            return redirect('/listing')
            
        # Display search result
        elif results_count == 1:
            flash(f'Result for "{search_input}". We found one item')
            search_results
        else:
            flash(f'Result for "{search_input}". We found {results_count} items')
            search_results
    # renders the the page with the search result                
    return render_template('listing.html', books=search_results, current_page=current_page,page_title=page_title)

@app.route("/register", methods=["GET", "POST"])
def register():
    """ Returns a form for user registration  """

    # initializes page title
    page_title ="Register"
    form = LoginForm()
    if form.validate_on_submit():
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": form.username.data.lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": form.username.data.lower(),
            "password": generate_password_hash(form.password.data),
            "review_viewed": 0
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = form.username.data.lower()
        flash("Registration Successful!")
        return redirect(url_for("profile"))

    return render_template("register.html", form=form, page_title=page_title)

@app.route("/login", methods=["GET", "POST"])
def login():
    """ Returns a form for for user login  """

    # initializes page title
    page_title="Log in"
    form = LoginForm()
    if form.validate_on_submit():
        # check if username exists in db
        existing_user = mongo.db.users.find_one_or_404(
            {"username": form.username.data.lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], form.password.data):
                        session["user"] = form.username.data.lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html", form=form,page_title=page_title)


@app.route("/profile/", methods=["GET", "POST"])
def profile():
    """ Returns the user profile page  """

    # grab the session user's username from db
    if "user" in session:
        # initializes page title    
        page_title="Profile"
        username = mongo.db.users.find_one_or_404(
            {"username": session["user"]})["username"]
        #reviews created by the current user
        myreview = mongo.db.book.find( {"created_by": session["user"]}).count()
        #comments created by the current user
        mycomment =mongo.db.comment.find( {"created_by": session["user"]}).count()
        #count of reviews viewed by the current user 
        review_viewed= mongo.db.users.find_one_or_404({'username': session["user"]})
        # renders the the page of the user profile
        return render_template("profile.html", username=username,page_title=page_title,myreview=myreview,mycomment=mycomment,review_viewed=review_viewed)
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    """ log out current user profile  """

    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    """ returns form for add a book  """

    form = AddBookForm()
    # initializes page title
    page_title = "Add a Book"   
    if form.validate_on_submit():
        book = {
            "category_name": request.form.get("category_name"),
            "book_name": form.name.data,
            "book_description": form.bookdescription.data,
            "publication_date": request.form.get("publication_date"),
            "cover_image_url": form.coverimageurl.data,
            "number_pages": form.npages.data,
            "book_review": form.bookreview.data,
            "book_author": form.author.data,
            "book_publisher": form.publisher.data,
            "rating": request.form.get("rating"),
            "created_by": session["user"]
        }
        mongo.db.book.insert_one(book)
        flash("Book successfully added!")
        return redirect(url_for("index"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    # renders the the page of the form for add a book
    return render_template("add_book.html", categories=categories, form=form,page_title=page_title)

@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    """ Returns a form for edit a book  """

    form = AddBookForm()
    # initializes page title
    page_title="Edit Book"
    book = mongo.db.book.find_one_or_404({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
     # renders the the page of the form for edit a book
    return render_template('edit_book.html',
     book=book, categories=categories, form=form,page_title=page_title)
 
@app.route("/update_book/<book_id>", methods=["GET", "POST"])
def update_book(book_id):
    """ Inserts book changes updates  """

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "book_name": request.form.get("book_name"),
            "book_description": request.form.get("book_description"),
            "publication_date": request.form.get("publication_date"),
            "cover_image_url": request.form.get("cover_image_url"),
            "number_pages": request.form.get("number_pages"),
            "book_review": request.form.get("book_review"),
            "book_author": request.form.get("book_author"),
            "book_publisher": request.form.get("book_publisher"),
            "rating": request.form.get("rating"),
            "created_by": session["user"]
        }
        mongo.db.book.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Successfully Updated")
    book = mongo.db.book.find_one_or_404({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("browse.html", book=book, categories=categories)

@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    """ Delete a book  """
    #remove book from database
    mongo.db.book.remove({"_id": ObjectId(book_id)})
    #remove comments of the book
    mongo.db.comment.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("listing"))

@app.route("/add_comment/<book_id>", methods=["GET", "POST"])
def add_comment(book_id):
    """ Add a comment to a book review  """

    if request.method == "POST":
        comment = mongo.db.comment
        #insert comment
        comment.insert_one({
                "comment": request.form.get("comment"),
                'book_id': ObjectId(book_id),
                "created_by": session["user"]   
        })
        flash("Comment successfully added!")
        return redirect(url_for('browse', book_id=book_id))

@app.route('/delete_comment/<comment_id>/<book_id>')
def delete_comment(comment_id, book_id):
    """ Delete a comment  """
    
    mongo.db.comment.remove({'_id': ObjectId(comment_id)})
    flash("Comment successfully deleted!")
    return redirect(url_for('browse', book_id=book_id))

@app.route('/delete_account/')
def delete_account():
    """ Delete a user profile """

    #remove current user profile from database
    mongo.db.users.remove({"username": session["user"]})
    #remove books created by current user
    mongo.db.book.remove({"created_by": session["user"]})
    #remove comments created by current user
    mongo.db.comment.remove({"created_by": session["user"]})
    # remove user from session cookie
    session.pop("user")
    flash("Profile successfully deleted!")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)