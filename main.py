#By Yun Chen
import kivy
kivy.require("1.7.2")
from kivy.app import App
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty

class onlyScreen(FloatLayout):
  Config.setdefaults("account", {"user": "","password": ""})
  saveuser = Config.get("account", "user")
  savepassword = Config.get("account", "password")
  user = ObjectProperty()
  password = ObjectProperty()
  check = ObjectProperty()

  def sendwifi(self):
    if self.check.active == True:
      Config.set("account", "user", self.user.text)
      Config.set("account", "password", self.password.text)
      Config.write()

    url1 = "http://fju1.auth.fju.edu.tw/auth/index.html/u"
    url2 = "http://fju2.auth.fju.edu.tw/auth/index.html/u"
    url3 = "http://fju3.auth.fju.edu.tw/auth/index.html/u"
    url4 = "http://fju4.auth.fju.edu.tw/auth/index.html/u"
    url5 = "http://fju5.auth.fju.edu.tw/auth/index.html/u"
    url6 = "http://fju6.auth.fju.edu.tw/auth/index.html/u"
    senddata = "?user="+self.user.text+"&password="+self.password.text

    popup = Popup(title="FJU Wi-Fine :)", content=Label(text="FJU Wi-Fi Data Send Success!!"),size_hint=(None, None), size=(450,300))

    for i in range(0,2):
      UrlRequest(url1+senddata)
      UrlRequest(url2+senddata)
      UrlRequest(url3+senddata)
      UrlRequest(url4+senddata)
      UrlRequest(url5+senddata)
      UrlRequest(url6+senddata)

    popup.open()

class MyApp(App):
  def build(self):
    return onlyScreen()

if __name__ == '__main__':
  MyApp().run()
