

var firebaseConfig = {
    apiKey: "AIzaSyDWbM3XKnTy5uiqiA9ZnbxmbxJ8SUjYuGI",
    authDomain: "fir-webapp-9012a.firebaseapp.com",
    databaseURL: "https://fir-webapp-9012a.firebaseio.com",
    projectId: "fir-webapp-9012a",
    storageBucket: "fir-webapp-9012a.appspot.com",
    messagingSenderId: "983763752961",
    appId: "1:983763752961:web:ef66cc63ecf45f1ba90800",
    measurementId: "G-RKFV9F6ZG4"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  

  firebase.auth.Auth.Persistence.LOCAL;


  $("#btn-login").click(function()
  {
    
     var email =  $("#email").val();
     var password =  $("#password").val(); 


     if(email !="" && password != "")
     {

            var result = firebase.auth().signInWithEmailAndPassword(email, password);

            result.catch(function(error)
            {
                  var errorCode = error.code;
                  var errorMessage = error.message;
  
  
                  console.log(errorCode);
                  console.log(errorMessage);
                  window.alert("Message : " + errorMessage);
            });

     }
     else{
         window.alert("Form is incomplete. Please fill out the fields.");
     }
  });



  
  $("#btn-signup").click(function()
  {
    
     var email =  $("#email").val();
     var password =  $("#password").val(); 
     var cPassword =  $("#confirmPassword").val(); 

     if(email !="" && password != "" && cPassword != "")
     {
          if(password == cPassword)
          {
            var result = firebase.auth().createUserWithEmailAndPassword(email, password);

            result.catch(function(error)
            {
                  var errorCode = error.code;
                  var errorMessage = error.message;
  
  
                  console.log(errorCode);
                  console.log(errorMessage);
                  window.alert("Message : " + errorMessage);
            });
          }
          else{
              window.alert("Password does not match with confirm password");
          }
     }
     else{
         window.alert("Form is incomplete. Please fill out the fields.");
     }
  });


  $("#btn-resetPassword").click(function()
  {
    var auth = firebase.auth();
    var email = $("#email").val();

    if(email != "")
    {
        auth.sendPasswordResetEmail(email).then(function(){
            window.alert("Email has bee sent to you please check and verify it");

        })
        .catch(function(error){
            var errorCode = error.code;
            var errorMessage = error.message;


            console.log(errorCode);
            console.log(errorMessage);
            window.alert("Message : " + errorMessage);
        });
    }
    else{
        window.alert("Please write your email first.");
    }

 });
  

  $("#btn-logout").click(function()
  {
    firebase.auth().signOut();

 });

 $("#btn-update").click(function()
 {
    var phone =  $("#phone").val();
    var address =  $("#address").val(); 
    var bio =  $("#bio").val(); 
    var fName =  $("#firstName").val();
    var sName =  $("#secondName").val(); 
    var country =  $("#country").val(); 
    var gender =  $("#gender").val(); 

    var rootRef = firebase.database().ref().child("Users");
    var userID = firebase.auth().currentUser.uid;
    var usersRef = rootRef.child(userID);

    if(fName!="" && sName!="" && phone!="" && country!="" && gender!="" && bio!="" && address!="")
    {
            var userData = {
                "phone": phone,
                "address": address,
                "bio": bio,
                "firstName": fName,
                "secondName": sName,
                "country": country,
                "gender": gender,
            };

            usersRef.set(userData, function(error){
                if(error)
                {
                    var errorCode = error.code;
                    var errorMessage = error.message;
        
        
                    console.log(errorCode);
                    console.log(errorMessage);
                    window.alert("Message : " + errorMessage);
                }
                else{
                    window.location.href = "MainPage.html";
                }
            });
    }

    else{
        window.alert("Form is incomplete. Please fill out the fields.");
    }


});

function switchView(view)
{
    $.get({
        url:view,
        cache:false,
    })
    .then(function(data){
        $("#container").html(data);
    });
}
  