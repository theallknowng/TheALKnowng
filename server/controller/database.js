var conn = require('../config/database-connection')
var request = require('request-promise');

const url='http://dataservice.accuweather.com/forecasts/v1/daily/1day/204842'
var propertiesObject = { apikey:'hXdBW69CiAiCMNWJ5sddRGGZIfjoCthe' ,metric:'true' };

function getUser (email_id, password, cb) {
  var sql = 'select * from users where email_id ="' + email_id + '" and password ="' + password + '"'
  conn.query(sql, function (err, user) {
    cb(err, user[0])
  })
}

function newUser (values, cb) {
  var sql = 'INSERT INTO `users`(`email_id`, `password`, `home_location_lat`, `home_location_long`, `name`) VALUES(?)'
  conn.query(sql, [values], function (err, result) {
    cb(err, result)
  })
}

function getMarkets (lat, long, crop_name, cb) {
  var sql = 'SELECT markets.id,markets.name,markets.market_lat, markets.market_long, market_crop_rel.crop_name,market_crop_rel.crop_price, ( 3959 * acos( cos( radians(' + lat + ') ) * cos( radians( market_lat ) ) \
* cos( radians( market_long ) - radians(' + long + ') ) + sin( radians(' + lat + ') ) * sin(radians(market_lat)) ) ) AS distance \
FROM markets , market_crop_rel where markets.id = market_crop_rel.market_id and market_crop_rel.crop_name = "' + crop_name + '"\
 ORDER BY distance asc'
  conn.query(sql, function (err, markets) {
    cb(err, markets)
  })
}

function newMarket (values, cb) {
  var sql = 'INSERT INTO `markets` (`name`, `market_lat`, `market_long`) VALUES(?)'
  conn.query(sql, [values], function (err, result) {
    cb(err, result)
  })
}

function irrigationDetails (values, cb) {
  var sql = 'INSERT INTO `userCrops` (`email_id`, `cropName`, `Irrigation`) VALUES(?)'
  conn.query(sql, [values], function (err, result) {
    cb(err, result)
  })
}


function weather(req,res){
  var data=1;
  request({url:url, qs:propertiesObject}, function(err, response, body) {
    
    // var data=[]
    if(err) { console.log(err); return; }
    console.log("Get response: " + response.statusCode);
    // data=[{"body":body}]
    // console.log("data")
    data=JSON.parse(body);
  })
  .then(()=>{
  // console.log(data)
  // res.send(data)
  res.send({'minTemp':data.DailyForecasts[0].Temperature.Minimum.Value,'maxTemp':data.DailyForecasts[0].Temperature.Maximum.Value, 'text':data.Headline.Text })
  })
}


module.exports = { getUser, newUser, getMarkets, newMarket, weather, irrigationDetails }
