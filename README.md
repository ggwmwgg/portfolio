### **GGwM**
## My Portfolio Website
#### Video Demo:  https://youtu.be/BZb9_QM6oQg
#### Description:
LIST OF USED Technologies:
*Flask
*Flask Sessions
*Telegramm API
*sqlite
*Python

A portfolio website with some functionality I've learned so far
This is a Flask Web Application, which uses SQL, Telegram API requests
You will need your API token from (t.me/)[@botfather](https://t.me/botfather) in order to run this application.
Simply use this command to execute it (in app.py directory):
```
export tokentg=XXXXXXXXXX:YYYYYYYYYYYYYYYYYYYYYYYYY
```
where XXXXXXXXXX:YYYYYYYYYYYYYYYYYYYYYYYYY is your API Token (like 123456789:jbd78sadvbdy63d37gda37bd8)

Front:

I've used premade template changed it, added some functionality (preload etc), converted for Flask (added loops in hello.html(made it from another template) and also connected buttons to use contact form which was also created on "/contact" and "contactru" routes)

Technologies:
*Bootstrap
*HTML
*JS (creates a nice index page)\
*Fontawesome


Functions:
```
insend(lang, name, email, subject, message, date)
```
Uses a Telegram API to send messages through a telegram channel (now @yumplay)
Your token saved in token variable (line 48)
If user submits a message via route "/" (english) version of this site the message
sent to @yumplay will be in english, else - in russian.
You can change messages sent to telegram group on lines 50(english) and 52(russian)
Method used to send messages is HTML , but you can change it (in the URL on line 53)
to Markdown or MarkdownV2 (be sure to format messages)

And also insert data into (now is) ggwm.db
Database defined on line 38 and 97. Database structure:
```
CREATE TABLE 'news' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
'name' TEXT, 'email' TEXT, 'subject' TEXT, 'message' TEXT, 'date' DATETIME);
```

To summarize - function insend opens the sqlite3 connection, execute INSERT all the data and closes the connection, then with help of API token this function generates a get request to the telegram to send the message into my channel
There's also a page implemented to review all of the messages at route "/hello"

This site is bilingual, RUSSIAN button redirects the User to route "/ru" and uses translated templates and layout template too.

Contact page:
Uses ```"name"```, ```"email"```, ```"subject"```, ```"message"``` from id in c.html, cru.html and ```date``` from ```datetime``` library to parse them to the ```insend``` function.

To run this programm execute:
```
flask run
```
in the app.py directory

Other functions:
index() and indexru() are generating the main page.
contact() and contactru() generating contact page with submission form to parse it to insend()
port() and portru() functions are generating portfolio page
about() and aboutru() are generating About me page

