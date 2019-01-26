var url = "http://127.0.0.1:5000/audio";

function handle_input(input,dataType) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", url, true);
  var data = new FormData();
  data.append("dataType", dataType)
  data.append("files", input);
  xhr.send(data);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        console.log(xhr.responseText);
        analyze_response(json);
    }
  };
}

/*
function analyze_response(json) {
  for (let sequence of json.main) {
    if (sequence.dataType == "gif") {}
*/