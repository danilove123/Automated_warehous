let username = document.querySelector('#username');
let age = document.querySelector('#age');
let email = document.querySelector('#email');
let password = document.querySelector('#password');
let phone = document.querySelector('#phone');

function UserAction() {
     const username_ = username.value;
     const age_ = age.value;
     const email_ = email.value;
     const password_ = password.value;
     const phone_ = phone.value;

     var obj = new Object();
     obj.username = username_;
     obj.age  = parseInt(age_);
     obj.email = email_;
     obj.password = password_;
     obj.phone = phone_;
     var jsonString= JSON.stringify(obj);
     console.log(jsonString)
     const url = "http://127.0.0.1:8000/auth/create_user"
     const Http = new XMLHttpRequest();
     Http.open("POST", url);
     Http.setRequestHeader("Content-Type", "application/json");
     Http.send(jsonString);
     Http.onreadystatechange = function() {
         if (Http.readyState == XMLHttpRequest.DONE ) {
            if(Http.status == 201){
                alert("Successfully created");
                window.open ('http://127.0.0.1:8000/warehouse/get_html/page_login','_self',false);
            }
            else {

                alert("Cant create user!");

            }
         }
    }
}
