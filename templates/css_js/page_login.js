let username = document.querySelector('#username');
let password = document.querySelector('#password');
       function UserAction() {
         const usename = username.value;
         const pssword = password.value;

         var xhttp = new XMLHttpRequest();
         xhttp.open("POST", `http://127.0.0.1:8000/auth/login?username=${usename}&password=${pssword}`);
         xhttp.send(null);

         xhttp.onreadystatechange = function() {
             if (xhttp.readyState == XMLHttpRequest.DONE ) {
                if(xhttp.status == 200){
                    window.open ('http://127.0.0.1:8000/warehouse/get_html/page_main_window','_self',false);
                    console.log("sdsd")
                }
                else {
                    if(xhttp.status == 401){

                    alert("Not register user");

                    }

                    else {

                    alert("Something went wrong(");

                    }
                }

             }

         }

     }

function pageRegistration() {
    window.open ('http://127.0.0.1:8000/warehouse/get_html/page_registration','_self',false);
}


