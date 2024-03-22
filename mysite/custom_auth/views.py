from django.shortcuts import render
import pyrebase
import firebase_admin
from firebase_admin import auth


config={
	"apiKey": "AIzaSyCrslVdbfTH4-6DKlda7qdKCrAsen9QK_Y",
	"authDomain": "test-14c86.firebaseapp.com",
	"databaseURL": "https://test-14c86-default-rtdb.firebaseio.com",
	"projectId": "test-14c86",
	"storageBucket": "test-14c86.appspot.com",
	"messagingSenderId": "673067347547",
	"appId": "1:673067347547:web:1a4de9b6e90c7458f7197e"
}
# Initialising database,auth and firebase for further use 
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def signIn(request):
	return render(request,"Login.html")
def home(request):
	return render(request,"Home.html")

def postsignIn(request):
	email=request.POST.get('email')
	pasw=request.POST.get('pass')
	try:
		# if there is no error then signin the user with given email and password
		user=authe.sign_in_with_email_and_password(email,pasw)
	except:
		message="Invalid Credentials!!Please ChecK your Data"
		return render(request,"Login.html",{"message":message})
	session_id=user['idToken']
	request.session['uid']=str(session_id)

	context = {
		'email': email,
		'user':user
	}

	return render(request,"Home.html", context)

def logout(request):
	try:
		del request.session['uid']
	except:
		pass
	return render(request,"Login.html")

def signUp(request):
	return render(request,"Registration.html")

def postsignUp(request):
	email = request.POST.get('email')
	passs = request.POST.get('pass')
	name = request.POST.get('name')
	try:
		# creating a user with the given email and password
		user=authe.create_user_with_email_and_password(email,passs)
		uid = user['localId']
		idtoken = request.session['uid']
		print(uid)
	except:
		return render(request, "Registration.html")
	return render(request,"Login.html")


# ----------------------------------------------------------------------------------------------

def reset(request):
	return render(request, "Reset.html")

def postReset(request):
	email = request.POST.get('email')
	try:
		authe.send_password_reset_email(email)
		message = "A email to reset password is successfully sent"
		return render(request, "Reset.html", {"msg":message})
	except:
		message = "Something went wrong, Please check the email you provided is registered or not"
		return render(request, "Reset.html", {"msg":message})

# -------------------------------------------------------------------------
	
# def profile(request,uid):
# 	user = auth.get_user(uid)

# 	context = {
# 		'user':user
# 	}
# 	return render(request, 'Profile.html', context)