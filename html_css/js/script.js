function read(){

    var name= document.getElementById("get_name").value;
    var rollNumber= document.getElementById("get_rollno").value;
    var addNumber =document.getElementById("get_addno").value;
    var addAge =document.getElementById("get_age").value;
    if(addAge<18){
        window.alert("You are Not Eligible");
    }else{
        window.alert("You are  Eligible");
        console.log(addAge);
    }
    
    console.log(name);
    console.log(rollNumber);
    console.log(addNumber);
    
    
    
    
    
    
    }