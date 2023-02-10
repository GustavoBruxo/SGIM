var coordenadasinciais = [-19.681701563909616, -44.89016025751918];
var zoominicial = [15];

// Crie uma instância do mapa Leaflet
var map = L.map('map').setView(coordenadasinciais, zoominicial);

var streetLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {});
var satelliteLayer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    maxZoom: 18,
    id: 'mapbox/satellite-v9',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZ3VzdGF2b3NnaW0iLCJhIjoiY2xkYWZhNG5qMDlpYjNwcDZkbzMzdHRlbSJ9.1f1FocVPKq1ajqPRSPxUrg'
});

// Adicione a camada base que você deseja que seja exibida por padrão
streetLayer.addTo(map);

// Crie um objeto de controle de camadas como descrito acima
var baseLayers = {
    "Mapa": streetLayer,
    "Satélite": satelliteLayer
};

// Adicione o objeto de controle de camadas ao mapa
L.control.layers(baseLayers).addTo(map);