//Richard Deodutt
//09/15/2022
//This script is meant to gather data from a API specifically a flaskapp
//Issues

//API root for now should be assumed to be the ip address this is running on
var APIRoot=window.location.href;

//Last JSON data stored locally
var JSONData=""

//Log to console
function Log(Msg){
	console.log(Msg);
}

//Get the bored api
function GetBored(){
	var Request = new XMLHttpRequest();
	Request.open('GET', APIRoot+'/bored', true);
	Request.setRequestHeader("accept", "application/json");
	Request.setRequestHeader("Content-Type", "application/json");
	try{
		Request.send();
		Request.onload = function(){
			if(Request.status === 200){
                ;
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
	Request.open('GET', APIRoot+'/name/'+Name, true);
	Request.setRequestHeader("accept", "application/json");
	Request.setRequestHeader("Content-Type", "application/json");
	try{
		Request.send();
		Request.onload = function(){
			if(Request.status === 200){
                ;
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
	Request.open('POST', APIRoot+'/jsontocsv', true);
	Request.setRequestHeader("accept", "application/json");
	Request.setRequestHeader("Content-Type", "application/json");
	try{
		Request.send(PayLoad);
		Request.onload = function(){
			if(Request.status === 200){
                ;
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

function ClickedBored(){
    GetBored();
}

function ClickedName(){
    var InputName = document.getElementById(nameinput);
    //Implement a Check If it's valid then do below
    GetName(InputName.value);
}

function ClickedDownloadJSON(){
    ;//Download the local JSON
}

function ClickedDownloadCSV(){
    GetCSV(JSONData);
}