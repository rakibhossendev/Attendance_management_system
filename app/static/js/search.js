document.addEventListener("DOMContentLoaded", function(){

let input = document.getElementById("teacherSearch");

input.addEventListener("keyup", function(){

let filter = input.value.toLowerCase();

let rows = document.querySelectorAll("#teacherTable tbody tr");

rows.forEach(function(row){

let text = row.textContent.toLowerCase();

if(text.includes(filter)){
row.style.display = "";
}
else{
row.style.display = "none";
}

});

});

});