//
// location.js
// @Author Brian
//

version = L.version;
console.log("Leafletjs: "+version)
alert("Profile maps cool1..."+version);

var geojsonFeature = {
    "type": "Feature",
    "properties": {
        "username": "cool",
        "profile_number": "20230508112345213",
        "popupContent": "Cool, Profile info..."
    },
    "geometry": {
        "type": "Point",
        "coordinate": [-104.99404, 39.75621]
    }
  }

var users = [];
var profiles = [geojsonFeature,{},]
var i = 0;
var j = 0;

function locationInfo(userX){
  var info = userX.trim();
  var username = info;
  var latitude = document.getElementById("latp"+info).innerHTML;
  var longitude = document.getElementById("lngp"+info).innerHTML;
  var profile = document.getElementById("p"+info).innerHTML;
  console.log(j+" username: ", username);
  console.log(j+" profileInfo: ", profile);
  var geojsonProfile = {
      "type": "Feature",
      "properties": {
          "username": username,
          "popupContent": profile
      },
      "geometry": {
          "type": "Point",
          "coordinate": [latitude.trim(), longitude.trim()]
      }
    }
  console.log(j+"username: "+username);
  console.log(j+"profile: "+geojsonProfile);
  profiles[j] = geojsonProfile;
  j++;
  return username;
}

function profileInfo(table){
  var tableName = document.getElementById(table);
  var username = table.trim();
  //var profile = tableName.value;
  var profile = tableName.innerHTML;
  console.log(i+" Username: ", username);
  console.log(i+" ProfileInfo: ", profile);
  alert(i+"Username: "+username);
  alert(i+"Profile: "+profile);
  users[i] = username;
  i++;
  return username;
}

function onEachFeature(feature, layer){
  if(feature.properties && feature.properties.popupContent){
    layer.bindPopup(feature.properties.popupContent);
  }
}

///////////////////////
//ref:
//https://leafletjs.com/index.html
//https://leafletjs.com/examples/quick-start/
//https://leafletjs.com/examples/geojson/example.html
//https://leafletjs.com/reference.html
///////////////////////////

//var map = L.Map('map').setView([51.505, -0.09], 13);
var map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributers'
}).addTo(map);

var marker = L.marker([51.5, -0.09]).addTo(map);
marker.bindPopup("Profile: Location(51.5,-0.09)<br>UserName: Cool").openPopup();

/*/
//var profileLayer = L.geoJSON().addTo(map);
//profileLayer.addData(geojsonFeature);

//var profileLayer = L.geoJSON(geojsonFeature, {
//    onEachFeature: onEachFeature
//  }).addTo(map);

//var profileLayer = L.geoJSON({
//    onEachFeature: onEachFeature
//  }).addTo(map);
//profileLayer.addData(geojsonFeature);
//var popup = L.popup()
//    .setLatLng([51.513, -0.09])
//    .setContent("I am a standalone popup.")
//    .openOn(map);


/*/

/*/
L.geoJSON(profiles, {
  onEachFeature: onEachFeature
}).addTo(map);
*/

var popup = L.popup();

function onMapClick(e){
  popup
       .setLatLng(e.latlng)
       .setContent("Profile at: "+e.latlng.toString())
       .openOn(map);
}

map.on('click', onMapClick);

//version = L.version;
console.log("Leafletjs: "+version);
alert("Done cool2...enjoy..."+version);
