var express = require('express')
var router = express.Router()
var database = require('../controller/database')

router.post('/login', function (req, res) {
  database.getUser(req.body.email_id, req.body.password, (err, user) => {
    if (user) {
      res.json({ success: 'true', user: user })
    } else {
      res.json({ success: 'false' })
    }
  })
})

router.post('/register', (req, res) => {
  var values = [req.body.email_id, req.body.password, req.body.home_lat, req.body.home_long, req.body.name]
  database.newUser(values, (err, result) => {
    if (err) {
      res.json({ success: 'false' })
    } else {
      res.json({ success: 'true' })
    }
  })
})

router.post('/markets', function (req, res) {
  database.getMarkets(req.body.lat, req.body.long, req.body.name, (err, markets) => {
    if (markets) {
      res.json({ success: 'true', markets: markets })
    } else {
      res.json({ success: 'false' })
    }
  })
})

module.exports = router
