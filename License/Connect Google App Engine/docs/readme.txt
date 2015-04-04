This package shows you how to connect a game to a server running on Google App Engine® (GAE). The server scripts for this package was written in Python and uses the GAE API, jinja2, wtforms, ndb and webapp2. The client side scripts are all done in C#.

Google App Engine® enables you to build and host web apps on the same systems that power Google® applications. App engine offers fast development and deployment; simple administration, with no need to worry about hardware, patches or backups; and effortless scalability. Depending on your game's load you could host the server side for free or for a very low monthly fee. See http://code.google.com/appengine/ for more information on Google App Engine® and http://code.google.com/appengine/docs/quotas.html for the free quotas that apply.


You will find documentation on how to use this package in the “docs” directory.
Visit http://plyoung.com/forums/ or http://plyoung.wordpress.com/ for support.

Check out http://www.battlemass.com/ for a sample of a full game making use of code from this package.

Visit this link http://unitygae.appspot.com/sample.htm for a webplayer demo of the included sample scene.

This package features the following systems:

* Account system:
Players can Register, Login, and Initiate Password Recovery from within the game client.
There is also a sample of how to save a player's settings to the server and load it when the player login; this could even be adapted for a system that saves game state in the “cloud”.

* Friends system:
Friends list. List, Add and remove friends.

* Chat system:
Public channel for all players and private chat channels between 2 players. Also List online players.

* Simple News and Advert system:
Sample game admin section to add news and adverts and how to show them client side.

* Payment system:
Check in-game if player purchased game. Use of keys to unlock game. Admin side to manage ownership and generate game keys. Sample of handling PayPal and auto-generating keys and sending via e-mail when payment confirmed.
