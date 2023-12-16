fetch("jsondata.json")
.then(response=>response.js)
.then(data=> showInfo(data));

function showInfo(data){
    console.table(data);
}