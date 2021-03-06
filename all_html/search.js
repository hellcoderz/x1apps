
function add_result_to_list(response){
    var res = response;
    var items = res["items"];
    //console.log(items);

    for(i=0;i<items.length;i++){
      item = items[i]
      if(item["id"]["kind"] == "youtube#video"){
        var id = item["id"]["videoId"]
        var url = "//www.youtube.com/embed/" + id + "?autoplay=1&fs=1&autohide=1&controls=0&rel=0";
        var title = item["snippet"]["title"]
        var desc = item["snippet"]["description"]
        var image_url = item["snippet"]["thumbnails"]["high"]["url"]


        var tag_str = "<div class='area'> <a href='"+url+"' id='"+i+"'><div class='bubble'><img src='"+image_url+"' width='100px' height='100px' style='float:left'></img><div><div class='title'><strong>"+title+"</strong></div><div class='desc'>"+desc+"</div></div></div></a></div>";

        $("#maintabs").append(tag_str);
      }
      
    }
  }



// Once the api loads call enable the search box.
function handleAPILoaded() {
  $('#search-button').attr('disabled', false);
}

// This callback is invoked by the Google APIs JS client automatically when it is loaded.
googleApiClientReady = function() {
  
  gapi.auth.init(function() {
    //window.setTimeout(checkAuth, 1);
   loadAPIClientInterfaces()
  });
  
}


function getQueryVariable(variable) {
    var query = document.URL;
    var arr = query.split('?');
    if(arr.length > 1){
      var vars = arr[1];
      var maps = vars.split("&");
      for (var i = 0; i < maps.length; i++) {
          var pair = maps[i].split('=');
          if (decodeURIComponent(pair[0]) == variable) {
            console.log("query= "+ decodeURIComponent(pair[1]));
              return decodeURIComponent(pair[1]);
          }
      }
    }else{
      return "cats";
    }
    console.log('Query variable %s not found', variable);
}

function loadAPIClientInterfaces() {
      
      gapi.client.load('youtube', 'v3', function() {
        res = search(getQueryVariable("q"));
      });
  }

// Search for a given string.
function search(query) {
  // var q = $('#query').val();

  var q = query;
  var request = gapi.client.youtube.search.list({
    q: q,
    part: 'snippet',
    key:"AIzaSyDdUOGutOhweA_X4qU5jhsAQvBMfMVmxAA",
    maxResults:15
  });

  var res = null;
  request.execute(function(response) {
    res = response.result
    //console.log(res["items"]);
    var str = JSON.stringify(response.result);
    add_result_to_list(res)
    var currentZone = $("#maintabs");
    var firstChild = currentZone.children()[0]
    //console.log(firstChild)
    $(firstChild).addClass("nav-current-item");
    //$('#search-container').html('<pre>' + str + '</pre>');
  });
  
}