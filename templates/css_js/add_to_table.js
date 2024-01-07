let password = document.querySelector('#Tbody');
let dashboard = document.querySelector('#Table_dashboard');
function Reload() {

for (var i = dashboard.rows.length-1; i>0; i--){
    dashboard.deleteRow(i);
}

var xhttp = new XMLHttpRequest();
xhttp.open("GET", `http://127.0.0.1:8000/warehouse/get_shelfs`);
xhttp.send(null);

xhttp.onreadystatechange = function() {
   if (xhttp.readyState == XMLHttpRequest.DONE ) {
      if(xhttp.status == 200){
          //var s2 = xhttp.responseText.substring(1);
          var s3 = xhttp.responseText.slice(3,-3);
          const array = s3.split('], [');

          for (const element of array){

            const array_1 = element.split(', ');
            var newRow=password.insertRow(0);
            var i = 0;
            console.log(element)

            for (const element of array_1){

                var newCell = newRow.insertCell(0);
                yacheyka = array_1[array_1.length - 1 - i];

                if (yacheyka.indexOf('\'') > -1){
                    newCell.innerHTML = yacheyka.slice(1,-1);
                }
                else{
                    newCell.innerHTML = yacheyka;
                }
                i = i + 1;
            }
            password.appendChild(newRow);
          }
      }
      else {
          console.log("Something went wrong with get from db");
      }

   }

}

}

function funcDashboard() {

    window.open ('http://127.0.0.1:8000/warehouse/get_html/page_main_window','_self',false);

}


function funcProducers() {


var xhttp = new XMLHttpRequest();
window.open ('http://127.0.0.1:8000/warehouse/get_html/page_producers_window','_self',false);
xhttp.send(null);

}

function ReloadProducers() {


let password = document.querySelector('#Tbody');
let dashboard = document.querySelector('#Table_dashboard');

for (var i = dashboard.rows.length-1; i>0; i--){
    dashboard.deleteRow(i);
}

var xhttp = new XMLHttpRequest();
xhttp.open("GET", `http://127.0.0.1:8000/warehouse/get_producers`);
xhttp.send(null);


xhttp.onreadystatechange = function() {
   if (xhttp.readyState == XMLHttpRequest.DONE ) {
      if(xhttp.status == 200){
          //var s2 = xhttp.responseText.substring(1);
          var s3 = xhttp.responseText.slice(3,-3);

          const array = s3.split('), (');

          for (const element of array){

            const array_1 = element.split(', ');
            var newRow=password.insertRow(0);
            var i = 0;
            console.log(element)

            for (const element of array_1){

                var newCell = newRow.insertCell(0);
                yacheyka = array_1[array_1.length - 1 - i];

                if (yacheyka.indexOf('\'') > -1){
                    newCell.innerHTML = yacheyka.slice(1,-1);
                }
                else{
                    newCell.innerHTML = yacheyka;
                }
                i = i + 1;
            }
            password.appendChild(newRow);
          }
      }
      else {
          console.log("Something went wrong with get from db");
      }

   }

}

}


function funcStaff() {

var xhttp = new XMLHttpRequest();
window.open ('http://127.0.0.1:8000/warehouse/get_html/page_staff_window','_self',false);
xhttp.send(null);

}


function ReloadStaff() {


let password = document.querySelector('#Tbody');
let dashboard = document.querySelector('#Table_dashboard');

for (var i = dashboard.rows.length-1; i>0; i--){
    dashboard.deleteRow(i);
}

var xhttp = new XMLHttpRequest();
xhttp.open("GET", `http://127.0.0.1:8000/warehouse/get_staff`);
xhttp.send(null);


xhttp.onreadystatechange = function() {
   if (xhttp.readyState == XMLHttpRequest.DONE ) {
      if(xhttp.status == 200){
          //var s2 = xhttp.responseText.substring(1);
          var s3 = xhttp.responseText.slice(3,-3);
          const array = s3.split('), (');

          for (const element of array){

            const array_1 = element.split(', ');
            var newRow=password.insertRow(0);
            var i = 0;
            console.log(element)

            for (const element of array_1){

                var newCell = newRow.insertCell(0);
                yacheyka = array_1[array_1.length - 1 - i];

                if (yacheyka.indexOf('\'') > -1){
                    newCell.innerHTML = yacheyka.slice(1,-1);
                }
                else{
                    newCell.innerHTML = yacheyka;
                }
                i = i + 1;
            }
            password.appendChild(newRow);
          }
      }
      else {
          console.log("Something went wrong with get from db");
      }

   }

}

}


function funcSignOut() {

var xhttp = new XMLHttpRequest();
window.open ('http://127.0.0.1:8000/warehouse/get_html/page_login','_self',false);
xhttp.send(null);

}



