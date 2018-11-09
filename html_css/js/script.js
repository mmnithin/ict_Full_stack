 function read(){

    var name= document.getElementById("get_name").value;
    var rollNumber= document.getElementById("get_rollno").value;
    var addNumber =document.getElementById("get_addno").value;
    var addAge =document.getElementById("get_age").value;

    var option =document.getElementById("get_district");
    var dist=option.options[option.selectedIndex].value;
   


    
    
    console.log(name);
    console.log(rollNumber);
    console.log(addNumber);
    console.log(dist);
    if(addAge<18){
        window.alert("You are Not Eligible");
    }else{
        window.alert("You are  Eligible");
        console.log(addAge);
    }
 }

    function oper(){

        var firstNo=document.getElementById("get_first_no").value;
        var secondNo=document.getElementById("get_second_no").value;
    
        var x= parseInt(firstNo);
        var y =parseInt(secondNo);

        var op=document.getElementById("operation");
        var select=op.options[op.selectedIndex].value;

        if(select== "add"){

            var result=x+y;
        }else if(select =="sub"){
            var result=x-y;
        }else if(select=="mul"){
            var result=x*y;
        }else{
            

                var result=x/y;
            
            
        }
        
        
        console.log(result);
        window.alert(result);
    }

    function big(){

        var n1= document.getElementById("first_num").value;
        var n2=document.getElementById("second_num").value;
        var n3=document.getElementById("third_num").value;

        var num1= parseInt(n1);
        var num2= parseInt(n2);
        var num3= parseInt(n3);

         if (num1>num2){
             if(num1>num3){
                console.log("Largest number is" + num1);
               window.alert("Largest number is" +num1);
             }else{
                console.log("Largest number is" + num3);
               window.alert("Largest number is" +num3);

             }
           
         }else{
             if(num2>num3){

                console.log("Largest number is" + num2);
          window.alert("Largest number is" +num2);
             }else{

                console.log( "Largest number is" +num3);
               window.alert("Largest number is" +num3);
             }
            
         }
        
    }
    function small(){

        var n1= document.getElementById("first_num").value;
        var n2=document.getElementById("second_num").value;
        var n3=document.getElementById("third_num").value;

        var num1= parseInt(n1);
        var num2= parseInt(n2);
        var num3= parseInt(n3);

         if (num1<num2){
             if(num1<num3){
                console.log("Largest number is" + num1);
               window.alert("Largest number is" +num1);
             }else{
                console.log("Largest number is" + num3);
               window.alert("Largest number is" +num3);

             }
           
         }else{
             if(num2<num3){

                console.log("Largest number is" + num2);
          window.alert("Largest number is" +num2);
             }else{

                console.log( "Largest number is" +num3);
               window.alert("Largest number is" +num3);
             }
            
         }
        
    }