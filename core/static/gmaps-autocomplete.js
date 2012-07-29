function initialize() {
    var input = document.getElementById('id_search');
    var autocomplete = new google.maps.places.Autocomplete(input);

    google.maps.event.addListener(autocomplete, 'place_changed', function() {
        var place = autocomplete.getPlace();
        console.log(place.address_components);
        if (place) {
            var objects = place.address_components;
            for (var i = 0; i < objects.length; i ++) {
                var short_name = objects[i].short_name;
                var loc_type = objects[i].types[0];
                var field = document.getElementById("id_" + loc_type);
                field.value = short_name;

                // UF Long Name
                var long_name = objects[i].long_name;
                var uf_long_name = document.getElementById("id_administrative_area_level_1_long_name");
                uf_long_name.value = long_name;
            }
        }
    });
}
google.maps.event.addDomListener(window, 'load', initialize);