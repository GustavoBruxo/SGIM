var properties = [
    {
        name: "Casa 1",
        location: [-19.680375423965334, -44.8893864946182],
        price: 500000
    },
    {
        name: "Casa 2",
        location: [-19.68180851208734, -44.888269745480905],
        price: 600000
    },
    {
        name: "Casa 3",
        location: [-19.67983128985573, -44.901269188937405],
        price: 700000
    }
];

var coordenadasinciais = [-19.681701563909616, -44.89016025751918];
var zoominicial = [15];

var map = L.map('map').setView(coordenadasinciais, zoominicial);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZ3VzdGF2b3NnaW0iLCJhIjoiY2xkYWZhNG5qMDlpYjNwcDZkbzMzdHRlbSJ9.1f1FocVPKq1ajqPRSPxUrg'
}).addTo(map);

properties.forEach(function(property) {
    var marker = L.marker(property.location).addTo(map);
    marker.bindPopup("<b>" + property.name + "</b><br>Preço: " + property.price);
});