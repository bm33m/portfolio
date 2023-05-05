//
// app.js
// @author: Brian
//

var locations = [];
var users = [];
var info = [];
var i = 0;
var j = 0;
var x = 0;

function userLocation(userLatLng){
  console.log("userLocation: "+userLatLng)
  var users = userLatLng.trim();
  var userLoc = users.split(',');
  var username = userLoc[0];
  var latitude = userLoc[1];
  var longitude = userLoc[2];
  var location = latitude+","+longitude;
  var infox = username+","+location;
  location[j] = location;
  info[x] = infox;
  console.log("username: "+username+", lat: "+latitude+", lng: "+longitude);
  console.log(j+" location: ", info[x]);
  j++;
  x++
  return infox;
}

function userLocationXYZ(userx, lat, lng){
  console.log("userLocation: "+userx+", "+lat+", "+", "+lng)
  var latitude = lat.trim();
  var longitude = lng.trim();
  var username = userx.trim();
  var location = latitude+","+longitude;
  var infox = username+","+location;
  location[j] = location;
  info[x] = infox;
  console.log(j+" location: ", info[x]);
  j++;
  x++
  return infox;
}

function profileInfo(table){
  var tableName = document.getElementById(table);
  var username = table.trim();
  //var profile = tableName.value;
  var profile = tableName.innerHTML;
  console.log(i+" username: ", username);
  console.log(i+" profileInfo: ", profile);
  alert("username:"+username);
  alert("profile:"+profile);
  users[i] = username;
  i++;
  return username;
}
