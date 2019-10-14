var express = require('express')
var app = express()
var bodyParser = require('body-parser')
var logger = require('morgan');
var path = require('path');

// routes
var user = require('./routes/user.js')

app.use(logger('dev'));
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(express.static(path.join(__dirname, 'public')));

app.use('/user', user)

app.listen(5656 || process.env.port)
console.log('Listening at 5656')
