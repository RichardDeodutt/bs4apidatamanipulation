//Richard Deodutt
//09/15/2022
//This script is meant to gather data from a API specifically a flaskapp
//Issues

//API root for now should be assumed to be the ip address this is running on
var APIRoot=window.location.href;

var API=""

//Last JSON data stored locally
var JSONData=""

//Log to console
function Log(Msg){
	console.log(Msg);
}

//Get the bored api
function GetBored(){
	var Request = new XMLHttpRequest();
	Request.open('GET', APIRoot+'bored', true);
	Request.setRequestHeader("accept", "application/json");
	Request.setRequestHeader("Content-Type", "application/json");
	try{
		Request.send();
		Request.onload = function(){
			if(Request.status === 200){
				var JsonDataElement = document.getElementById('jsondata');
				JSONData = Request.responseText;
				API = "Bored";
                JsonDataElement.textContent = JSONData;
				var DataDiv = document.getElementById('data');
				DataDiv.style.display = 'block';
			}
			else{
				Log('Failed to use Bored API, Request Error. Non 200 Status Code');
			}
		};
		Request.onerror = function() {
			Log('Failed to use Bored API, Request Error');
		};
	}
	catch(err){
		Log('Failed to use Bored API');
	}
}

//Get the name api
function GetName(Name){
	var Request = new XMLHttpRequest();
	Request.open('GET', APIRoot+'name/'+Name, true);
	Request.setRequestHeader("accept", "application/json");
	Request.setRequestHeader("Content-Type", "application/json");
	try{
		Request.send();
		Request.onload = function(){
			if(Request.status === 200){
				var JsonDataElement = document.getElementById('jsondata');
				JSONData = Request.responseText;
				API = "Name";
                JsonDataElement.textContent = JSONData;
				var DataDiv = document.getElementById('data');
				DataDiv.style.display = 'block';
			}
			else{
				Log('Failed to use Name API, Request Error. Non 200 Status Code');
			}
		};
		Request.onerror = function() {
			Log('Failed to use Name API, Request Error');
		};
	}
	catch(err){
		Log('Failed to use Name API');
	}
}

//Get the jsontocsv api
function GetCSV(JSONData){
	var Request = new XMLHttpRequest();
    var PayLoad = JSON.stringify(JSONData);
	Request.open('POST', APIRoot+'jsontocsv', true);
	Request.setRequestHeader("accept", "application/json");
	Request.setRequestHeader("Content-Type", "application/json");
	try{
		Request.send(PayLoad);
		Request.onload = function(){
			if(Request.status === 200){
				var Data = "data:text/json;charset=utf-8," + encodeURIComponent(Request.responseText);
				var DL = document.createElement('a');
				DL.setAttribute("href", Data);
				if("Key" in JSON.parse(JSONData)){
					DL.setAttribute("download", API+'-'+JSON.parse(JSONData)["Key"]+".csv");
				}
				else if("Name" in JSON.parse(JSONData)){
					DL.setAttribute("download", API+'-'+JSON.parse(JSONData)["Name"]+".csv");
				}
				DL.click();
			}
			else{
				Log('Failed to use JSONtoCSV API, Request Error. Non 200 Status Code');
			}
		};
		Request.onerror = function() {
			Log('Failed to use JSONtoCSV API, Request Error');
		};
	}
	catch(err){
		Log('Failed to use JSONtoCSV API');
	}
}

//When the user clicks the bored button
function ClickedBored(){
    GetBored();
}

//When the user clicks the name button
function ClickedName(){
    var InputName = document.getElementById('nameinput');
	Origin = InputName.value
	InputName.value = InputName.value.replace(/[^A-Za-z]/ig, '')
	if(Origin != InputName.value || InputName.value == ""){
		InputName.placeholder = "Only Letters"
		InputName.value = ""
	}
	else{
		GetName(InputName.value);
		InputName.placeholder = "Enter Name Here"
	}
}

//When the user clicks the download json
function ClickedDownloadJSON(){
    var Data = "data:text/json;charset=utf-8," + encodeURIComponent(JSONData);
	var DL = document.createElement('a');
	DL.setAttribute("href", Data);
	if("Key" in JSON.parse(JSONData)){
		DL.setAttribute("download", API+'-'+JSON.parse(JSONData)["Key"]+".json");
	}
	else if("Name" in JSON.parse(JSONData)){
		DL.setAttribute("download", API+'-'+JSON.parse(JSONData)["Name"]+".json");
	}
	DL.click();
}

//When the user clicks the download csv
function ClickedDownloadCSV(){
    GetCSV(JSONData)
}