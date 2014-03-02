#FJU-login-WiFi-APP

## For Fu Jen Catholic Student

An APP for smart phone to login school's wifi.

## Requirement

'''
Python 2.7.5
Kivy 1.7.2 at least
Python for Android/Kivy
Android-sdk 14 at lease 
Android-ndk
Buildozer/Kivy
'''

I use buildozer to pack my project to apk file
You can pack it and install it on your phone.
Watch more detail on [buildozer](https://github.com/kivy/buildozer)

'''
buildozer android debug deploy
'''

## Kivy

### Popup

Popup can provide you a pop window when you use it.
You can use on message box or some warning.
popup.close(),popup.dismiss() to control your pop window open or close.

'''python
popup = Popup(title="FJU Wi-Fine :)", 
content=Label(text="FJU Wi-Fi Data Send Success!!"),
size_hint=(None, None), size=(450,300))
'''

### Config

This provide you a config set that can memory something without database.
In here, I use config to save the user's account.
It will create .ini file atomatically with the data in your devices.

### UrlRequest

You can use urlrequest to instead requests in python.
It provide you more convenient way to use.

'''python
UrlRequest(url, on_success, on_error, req_body, req_headers)
'''

To see more detail you can find it on: 
[UrlRequest](http://kivy.org/docs/api-kivy.network.urlrequest.html)
'''

### Get Data In Python and Kivy

In .kv file ,if you want to get some varible in .py,
Kivy provide you root method to use
saveuser is a varible on main.py.
You can find this on class onlyScreen.

'''
text: root.saveuser
'''

In .py file,if you want to get some varible in .kv,
First you have to get the .kv object

.kv
'''
<onlyScreen>
    user(object name for python): user
    TextInput:
        id: user
'''

.py
'''python
class onlyScreen(FloatLayout):
    user = ObjectProperty()
    user.text,user.value
'''

Now,you can get the element from .kv
But please notice that the varible must in the same class.
like: Both .kv and .py varible are all in onlyScreen class.
Then you can get the value easily.
