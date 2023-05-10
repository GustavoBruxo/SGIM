var coordenadasinciais = [-19.681701563909616, -44.89016025751918];
var zoominicial = [15];

// Crie uma instância do mapa Leaflet
var map = L.map('map').setView(coordenadasinciais, zoominicial);
// Remova o controle de zoom padrão do Leaflet
map.removeControl(map.zoomControl);

L.control.zoom({
    position: 'topright'
}).addTo(map);

var streetLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {});

// Adicione a camada base que você deseja que seja exibida por padrão
streetLayer.addTo(map);