'use strict';

var express = require('express');
var http = require('http');
var path = require('path');
var url4 = require('url4');

process.env.NODE_ENV = 'production';
var app = express();

app.set('port', 8000);
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(app.router);

url4.urls = {
  'hello': '/hello/',
  'table': '/table/:row?/:col?'
};
app.locals.url4 = url4;

var ROWS = (function () {
  var rows = [], cols, row, col;
  for (row = 0; row < 10; row += 1) {
    cols = [];
    for (col = 0; col < 10; col += 1) {
      cols.push({row: row, col: col});
    }
    rows.push(cols);
  }
  return rows;
}());

app.get(url4.urls.hello, function (req, res) {
  res.send('Hello, World!');
});

app.get(url4.urls.table, function (req, res) {
  res.render('table', {rows: ROWS});
});

http.createServer(app).listen(app.get('port'), function () {
  console.log('Express server listening on port ' + app.get('port'));
});
