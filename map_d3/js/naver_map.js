
var oPoint = new nhn.api.map.LatLng(37.5667, 126.9781);		//create start position on the map(original point)

var map = new nhn.api.map.Map('map' ,{
    point : new nhn.api.map.LatLng(37.5667, 126.9781),		//create naver map class
    zoom : 7,
    enableWheelZoom : true,
    enableDragPan : true,	
    enableDblClickZoom : false,
    mapMode : 0,
    activateTrafficMap : false,
    activateBicycleMap : false,
    minMaxLevel : [ 1, 14 ],
    size : new nhn.api.map.Size(1300, 600)
});

var color = d3.scale.category10();
var radius = d3.scale.linear().domain([0, 3000]).range([10, 50]);

var layer = d3.select('.nmap_overlay_pane').append("div").attr("class", "library");			//where d3 objects overlay
var padding = 50,
	pluspadding = 1;
                 




var marker = layer.selectAll("svg")			//point marker object
    .data(d3.entries(data))
    .each(transform)
    .enter().append("svg:svg")
    .each(transform)
    .attr("class", "marker");
                     
marker.append("svg:circle")
    .attr("r", function(d){return radius(d.value.AR) >= 50 ? 50 : radius(d.value.AR);})
    .attr("cx", function(d){return padding;})
    .attr("cy", function(d){return padding;})
    .style("fill", function(d,i){return color(d.value.GU_NM);})
    .attr("fill-opacity", "0.7")
    .on("click",function(d){ alert(d.value.FCLTY_NM); map.setCenter(new nhn.api.map.LatLng(d.value.LAT, d.value.LNG)); });
                     
marker.append("svg:text")
    .attr("x", function(d){return padding;})
    .attr("y", function(d){return padding;})
    .attr("dy", ".31em").style("text-anchor", "middle")
    .text(function(d) { return d.value.LNG > 0 ? d.value.HNR_NAM : ""; });


function transform(d) {
    var r = radius(d.value.AR) >= 50 ? 50 : radius(d.value.AR);
    LatLng = new nhn.api.map.LatLng(d.value.LAT, d.value.LNG);
                         
    var oSize  = new nhn.api.map.Size(28, 37); 
    var oOffset = new nhn.api.map.Size(28, 37); 
    var oIcon  = new nhn.api.map.Icon('http://static.naver.com/maps2/icons/pin_spot2.png', oSize, oOffset); 
                         
    var oMarker = new nhn.api.map.Marker(oIcon, { title : d.value.FCLTY_NM }); 
    oMarker.setPoint(LatLng);

    
    
    map.addOverlay(oMarker);
    oMarker.setVisible(true);
                         
    return d3.select(this)
        .style("left", (parseInt(d3.select(oMarker)[0][0]["_elEl"].style.left)-padding) + "px")		//extract d3 circle position from map marker	
        .style("top", (parseInt(d3.select(oMarker)[0][0]["_elEl"].style.top)-padding) + "px")
        .style("width", (r+padding+pluspadding) + "px")
        .style("height", (r+padding+pluspadding) + "px");
}







function goPanning() {
    var tempZoomOptions = { useEffect : true, centerMark : true }; // set zoom options
    map.setCenterBy(20, -10, tempZoomOptions); // move 20 pixel to right 
}

function revertPanning() {
    map.setCenter(oPoint); 
}


var zoomEvent = function(zoom){
    var defaultBounds = map.getBound();
    var defaultCenter = map.getCenter();
    var defaultLevel = map.getLevel();
    var defaultMapMode = map.getMapMode();
}
                     

var mapZoom = new nhn.api.map.ZoomControl(); // zoom control declaration
mapZoom.setPosition({right:40, top:20}); // set position of zoom control
map.addControl(mapZoom); // add zoom control object








var mapInfoTestWindow = new nhn.api.map.InfoWindow(); // create info window
mapInfoTestWindow.setVisible(false); // display infowindow or not
map.addOverlay(mapInfoTestWindow);     // add to map  

var oLabel = new nhn.api.map.MarkerLabel(); // declaration marker label
map.addOverlay(oLabel); // add marker label to map(default: hidden)

mapInfoTestWindow.attach('changeVisible', function(oCustomEvent) {
        if (oCustomEvent.visible) {
                oLabel.setVisible(false);
        }
});


map.attach('mouseenter', function(oCustomEvent) {
        var oTarget = oCustomEvent.target;
        // when mouseover
        if (oTarget instanceof nhn.api.map.Marker) {
                var oMarker = oTarget;
                oLabel.setVisible(true, oMarker); // display marker title
        }
});

map.attach('mouseleave', function(oCustomEvent) {
        var oTarget = oCustomEvent.target;
        // when mouse leave
        if (oTarget instanceof nhn.api.map.Marker) {
                oLabel.setVisible(false);
        }
});

map.attach('click', function(oCustomEvent) {
        var oPoint = oCustomEvent.point;
        var oTarget = oCustomEvent.target;
        mapInfoTestWindow.setVisible(false);
        // when click marker
        if (oTarget instanceof nhn.api.map.Marker) {
                // when click overlapped marker
                if (oCustomEvent.clickCoveredMarker) {
                        return;
                }
                // - InfoWindow 에 들어갈 내용은 setContent 로 자유롭게 넣을 수 있습니다. 외부 css를 이용할 수 있으며, 
                // - 외부 css에 선언된 class를 이용하면 해당 class의 스타일을 바로 적용할 수 있습니다.
                // - 단, DIV 의 position style 은 absolute 가 되면 안되며, 
                // - absolute 의 경우 autoPosition 이 동작하지 않습니다. 
                mapInfoTestWindow.setContent('<DIV style="border-top:1px solid; border-bottom:2px groove black; border-left:1px solid; border-right:2px groove black;margin-bottom:1px;color:black;background-color:white; width:auto; height:auto;">'+
                '<span style="color: #000000 !important;display: inline-block;font-size: 12px !important;font-weight: bold !important;letter-spacing: -1px !important;white-space: nowrap !important; padding: 2px 2px 2px 2px !important">' + 
                'Location info: <br /> ' + oTarget.getPoint()
                +'<span></div>');
                mapInfoTestWindow.setPoint(oTarget.getPoint());
                mapInfoTestWindow.setVisible(true);
                mapInfoTestWindow.setPosition({right : 15, top : 30});
                mapInfoTestWindow.autoPosition();
                return;
        }
});


