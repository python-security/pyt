import datetime

import httplib2
from flask import Flask, render_template, request, redirect, url_for, session
from flask.ext.login import login_user, logout_user, current_user, login_required, LoginManager
from googleapiclient import discovery
from oauth2client import client
import os

import mysql_manager as mm
import ranker
import yelp_data_source
from models.UserModel import User

# static strings
connect_to_goog_cal = "Connect with Google Calendar to see your next event's location!"


# app configuration
DEBUG = False
SECRET_KEY = 'development_key'
USERNAME = 'admin'
PASSWORD = 'uci'
CLIENT_ID = "113602676382-vom8i9393ldj0vcuk32emk3c4elf20vo.apps.googleusercontent.com"
CLIENT_SECRET = "xdXnSkdHanL361tPp4AZU2HU"

# App Init
app = Flask(__name__)
app.config.from_object(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


# Helper Functions
@login_manager.user_loader
def user_loader(user_name):
    temp_user = mm.get_user(user_name)
    if temp_user is not None:
        return User(temp_user)
    return None


def is_google_auth():
    """
    Function that returns true if the user has autheticated Google Calender Read Only Access
    :return: Boolean
    """
    return False
    # if 'credentials' not in session.keys():
    #     return False
    # # print(session['credentials'])  # DEBUG
    # return True


# HOME PAGE
@app.route('/')
def index():
    return render_template("index.html")
# TODO: fix the front end get location and its scenarios where it doesnt have the location
# todo: on login, degenerate the user weights
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        # getting user_name and password form data
        user_name = request.form['user_name']
        form_password = request.form['user_password']
        print(user_name, form_password)
        if request.form['submit'] == 'Sign In':  # if the user is trying to sign in
            user = mm.get_user(user_name)  # get the user from Database, will return Null if no user_name
            if user:  # if not None
                muser = User(user)  # make a new user_model User
                if muser.password == form_password:  # if correct password
                    login_user(muser)  # Save user in context as "logged_in"
                    lat = request.form['current_location_latitude']
                    long = request.form['current_location_longitude']
                    print(lat,long)
                    session['lat'] = lat
                    session['long'] = long
                    mm.degenerate_categories(user_name)
                    return redirect(url_for('index'))  # return client to index page
                    # redirect(request.args.get('next') or url_for('index')) #allows login page to act as in between
                else:
                    # print("ERROR in logging in") #DEBUG
                    return render_template("login.html", error_msg="You entered a wrong password, please try again")
            else:
                return render_template("login.html", error_msg="Unknown username, please try again")
        elif request.form['submit'] == 'Sign Up':  # if trying to sign up new user
            # print("Trying to sign user up") #DEBUG
            if user_name is "" or form_password is "":
                return render_template("login.html", error_msg="Empty Username or Password Fields, please try again")
            mm.insert_new_user_profile(user_name, form_password)
            new_user = User((user_name, form_password))
            mm.init_category_weight_vector_for_user(user_name, .015)
            login_user(new_user)
            lat = request.form['current_location_latitude']
            long = request.form['current_location_longitude']
            print(lat,long)
            session['lat'] = lat
            session['long'] = long
            return redirect(url_for('index'))
    return render_template("login.html")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    logout_user()
    session.clear()
    return render_template("logout.html")


@app.route('/auth_google')
def auth_google():
    if 'credentials' not in session:
        return redirect(url_for('oauth2callback'))
    credentials = client.OAuth2Credentials.from_json(session['credentials'])
    if credentials.access_token_expired:
        return redirect(url_for('oauth2callback'))
    return redirect(url_for('index'))


def get_location(http_auth):
    service = discovery.build('calendar', 'v3', http=http_auth)
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    # note: events_result['items'][0] is a Event resource object
    # see: https://developers.google.com/google-apps/calendar/v3/reference/events
    index_of_valid_event = 0
    # need to handle when user has no more events in events_result
    for i in range(len(events_result['items'])):
        example = events_result['items'][i]['start']
        # check if event is all day event, if not, continue
        if 'dateTime' in example.keys():
            index_of_valid_event = i
            # print(index_of_valid_event) #DEBUG
            break
    if 'location' in events_result['items'][index_of_valid_event].keys():
        location = events_result['items'][index_of_valid_event]['location']
    else:
        location = 'unspecified'
    return location


@app.route('/oauth2callback')
def oauth2callback():
    flow = client.flow_from_clientsecrets(
        'resources/google_calendar_client_secret.json',
        scope='https://www.googleapis.com/auth/calendar.readonly',
        redirect_uri=url_for('oauth2callback', _external=True))
    print('google auth flow was established')  # DEBUG
    if 'code' not in request.args:
        auth_uri = flow.step1_get_authorize_url()
        return redirect(auth_uri)
    else:
        auth_code = request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        session['credentials'] = credentials.to_json()
        global http_auth
        http_auth = credentials.authorize(httplib2.Http())
        # print(http_auth)
        return redirect(url_for('index'))


# TODO: fix the front end location buttons
@app.route('/recommended', methods=["GET", "POST"])
def recommended():
    username = current_user.get_id()
    if request.method == "POST":
        print('hi post')
        # for i in request.form.items():
        #     print(i)
        print(request.form['whatOk'])
        if request.form['whatOk'] == "coords":
            long = request.form.get("current_location_longitude")
            lat = request.form.get("current_location_latitude")
            print(long, lat)
            # location = get_location(http_auth) if is_google_auth() else connect_to_goog_cal
            # TODO: PASS IN LONGITUDE AND LATITUDE IN YELP RETURN STATEMENT BELOW.................
            # print('LOCATION FROM GOOGLE CAL' + lat + "," + long)  # DEBUG


            return render_template("recommended.html",
                                   list_results=ranker.get_ranking_by_probabilistic_cosine(current_user.get_id(),
                                                                                  coords=[(lat, long)]))


        elif request.form['whatOk'] == "manual":
            a1 = request.form['addressline1']
            city = request.form['addresscity']
            state = request.form['addressstate']
            address = a1 + ' ' + city + ' ' + state
            return render_template("recommended.html",
                                   list_results=ranker.get_ranking_by_probabilistic_cosine_by_address(current_user.get_id(),address=address))

    else:

        print('Trying to get restaurant results using GET method')
        print((session['lat'], session['long']))
        if is_google_auth():
            location = get_location(http_auth)
        else:
            location = "Connect with Google Calendar to see your next event's location!"
        return render_template("recommended.html",
                               list_results=ranker.get_ranking_by_probabilistic_cosine(current_user.get_id(), coords=[(session['lat'], session['long'])]),
                               next_location=location)

# Visited Restaurants
@app.route('/visited')
@login_required
def visit_restaurants():
    username = current_user.get_id()
    list_of_tuples_business_id = mm.get_visited_businesses_by_username(username)
    list_yelp_data = []
    print(list_of_tuples_business_id)
    for tup in list_of_tuples_business_id:
        list_yelp_data.append(yelp_data_source.YelpData(yelp_data_source.get_business_by_id(tup[0])))
    empty_list = True
    if len(list_yelp_data) > 0:
        empty_list = False
    return render_template("visited.html", list_results=list_yelp_data, empty_list=empty_list)



# Single Restaurant View
@app.route('/restaurant/<restaurant_id>')
def restaurant(restaurant_id):
    business = yelp_data_source.get_business_by_id(restaurant_id)  # this is a dictionary
    rating = mm.get_rating_by_business_id(current_user.get_id(), business.id)
    return render_template("restaurant.html", business=business, rating=rating)


# Deprecating this method and page
@app.route('/profile/<username>')
@login_required
def profile(username):
    # print(current_user.get_id())  # EXAMPLE TO GET USER
    username = current_user.get_id()
    cat_names = mm.get_list_categories_for_profile_edit(username)
    return render_template("profile.html", category_names=cat_names)


# Deprecating this method and page
@app.route('/upload', methods=['POST', 'GET'])
@login_required
def upload():
    username = current_user.get_id()
    if request.method == 'GET':
        return redirect("/", code=302)
    # print("Trying to upload categories for user profile")
    selected_categories = request.form.getlist('checkbox')
    # print(selected_categories) #DEBUG
    for cat_name in selected_categories:
        mm.init_category_weight_if_not_present(username, cat_name, 1.0)
    return render_template("index.html", logged_in=True, username=username, code=302)


@app.route('/rate_listing')
@login_required
def get_nearby_locations():
    empty_list = True
    list_results = ranker.get_nearby_restaurants(current_user.get_id(), coords=[(session['lat'], session['long'])])
    if len(list_results)>0:
        empty_list = False
    return render_template("rate_listing.html", list_results=list_results, empty_list=empty_list)

@app.route('/rating', methods=['POST'])
@login_required
def update_user_weights():
    username = current_user.get_id()
    business_id = request.form['business-id']
    # opt_param = request.form.get('blacklist', None)
    # if opt_param is None:
    #     is_blacklisted = 0
    rating = request.form['my_rating_slider']
    business = yelp_data_source.get_business_by_id(business_id);
    list_categories = yelp_data_source.YelpData(business).list_categories
    print('Rating')
    print(rating)
    print(list_categories)
    mm.insert_visit_and_update_categories_for_business(business_id, list_categories, username, rating)
    return redirect(url_for('index'))


# app run
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(host='localhost')
    # to make app run public
    # app.run(host='0.0.0.0')