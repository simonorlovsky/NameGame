#!/usr/bin/python
''' tinywebapp.py
    Jeff Ondich, 2012

    This is the server-side script of a very simple web application
    that involves an HTML form with two <input type="text"> elements
    (one named "lastname" and the other named "ethnicity").
'''

import cgi

# Get the user input from the client's request.
form = cgi.FieldStorage()
lastname = form['lastname'].value
ethnicity = form['ethnicity'].value
question = form['question'].value

# Sanitize the user input. You can't trust users not to mess with
# your scripts. In this case, we allow only letters in our lastname
# names. Otherwise, you're stuck with the default lastname.
if not lastname.isalpha():
    lastname = 'DEFAULT lastname'
if not ethnicity.isalpha():
    ethnicity = 'DEFAULT ethnicity'
if not ethnicity.isalpha():
    question = 'DEFAULT question'

# Construct the output page.
output = '''<DOCTYPE HTML>
<html>
<head>
    <title>#NameGame Results</title>
</head>

<body>
    <p>I like %s.</p>
    <p>Also, %s is a cool ethnicity.</p>
    <p>Hmm, %s good question.</p>
</body>
</html>''' % (lastname, ethnicity, question)

# Send the output page back to the client.
print "Content-type: text/html\r\n\r\n"
print output
