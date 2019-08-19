var conn = require('../config/database-connection')

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
  var sql = 'SELECT markets.id,markets.name,market_crop_rel.crop_name,market_crop_rel.crop_price, ( 3959 * acos( cos( radians(' + lat + ') ) * cos( radians( market_lat ) ) \
* cos( radians( market_long ) - radians(' + long + ') ) + sin( radians(' + lat + ') ) * sin(radians(market_lat)) ) ) AS distance \
FROM markets , market_crop_rel where markets.id = market_crop_rel.market_id and market_crop_rel.crop_name = "' + crop_name + '"\
 ORDER BY distance desc'
  conn.query(sql, function (err, markets) {
    cb(err, markets)
  })
}

module.exports = { getUser, newUser, getMarkets }
