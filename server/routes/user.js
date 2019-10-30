var express = require('express')
var router = express.Router()
var database = require('../controller/database')
var fs = require('fs')

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

router.post('/marketRegister', function(req,res){
  var values=[ req.body.name,req.body.lat, req.body.long ]
  database.newMarket(values, (err, result)=> {
    if (err) {
      res.json({ success: 'false' })
    } else {
      res.json({ success: 'true' })
    }

  })
})

router.post('/irrigationData', function(req, res){
  var values=[ req.body.email,req.body.cropName,req.body.irrigation ]
  database.irrigationDetails(values, (err, result)=>{
    if (err) {
      res.json({ success: 'false' })
    } else {
      res.json({ success: 'true' })
    }
    
  })

})

router.post('/image', function(req,res){
  fs.readdir('./public/images/',(err,files)=>{
    if(err )throw err
    // console.log(err)
    resp={'success':'true','imageURL': files}
    res.json(resp)
  })
})

router.post('/weather',function(req,res){
  database.weather(req,res)

})

module.exports = router
