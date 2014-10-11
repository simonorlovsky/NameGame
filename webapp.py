#!/usr/bin/python
''' tinywebapp.py
    Simon Orlovsky, Hami Abdi, Caleb Braun 2012

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
output = '''<!DOCTYPE HTML>
<html>
    
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script> 

<head>
    <title>#NameGame</title>
</head>

<body>
    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">#NameGame</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li class="active">
                        <a href="#">Home</a>
                    </li>
                    <li>
                        <a href="#">Questions</a>
                    </li>
                    <li>
                        <a href="#">Contact</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <br>
    <br>
    <br>
    <br>
    <div class="container">
        <div class="row">
            <div class="col-lg-12 text-center">
                <div class="jumbotron">
                  <h1>#NameGame</h1>
                  <body>
                    <p>I like %s.</p>
                    <p>Also, %s is a cool ethnicity.</p>
                    <p>Hmm, %s good question.</p>
                </body>
                  
                </div>
                <br>
                <br>

            
            </html>''' % (lastname, ethnicity, question)

# Send the output page back to the client.
print "Content-type: text/html\r\n\r\n"
print output
