const apm = require('elastic-apm-node').start();

const express = require('express');
const app = express();

app.get('/', function (req, res) {
  try {
    throw new Error('Ups, something broke!')
  } catch (err) {
    apm.captureError(err)
  }
})

app.listen(3000)
