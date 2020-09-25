 // console.log('Hello World');
 // document.write("This is document write");
 // console.warn("this is a warning");
 // console.error("this is an error");

 // 3. JavaScript variables
 //What are variables? Containers to store data values
 // var number1 = 34;
 // var number2 = 56;
 // console.log(number1 + number2);

 // 4. Data types in JavaScript
 // var str1 = "This is a string";
 // var str2 = "This is another string";

 //Objects
 // var marks = {
 //   ravi: 34,
 //   shubham: 78,
 //   harry: 99.977
 // }
 // console.log(marks);

 // Booleans
 // var a = true;
 // var b = false;
 // console.log(a)

 // var und;
 // console.log(und);

 // var n = null;
 // console.log(n)

 // At a very high level, there are two types of
 // data in Javascript
 // 1. Primitive data types: undefined, null, number, string, boolean, symbol
 // 1. Reference data types: Arrays and Objects

 // var arr = [1, 2, "string", 4, 5]
 // console.log(arr)

 //Operrators in Javascript
 // Arithmetic operators
 // var a = 34;
 // var b = 56;
 // console.log("The value of a + b is ", a+b);

 //Assignment operators
 // var c = b;
 // c += 2;
 // console.log("The value of c is ", c);

 // comparision operators
 // var x = 34;
 // var y = 56;
 // console.log(x == y);

 //logical operators
 // console.log(true && true);
 // console.log(true && false);
 // console.log(true || true);
 // console.log(true || false);
 // console.log(!true);

 // Function in JavaScript

 // function avg(a, b){
 //   c = (a + b)/2;
 //   return c;
 // }
 //
 // c1 = avg(4, 6);
 // c2 = avg(14, 16);
 // console.log(c1, c2);

 //Coditionals in JavaScript
 // var age = 34;
 // if (age > 8){
 //   console.log('You are not a kid.')
 // } else {
 //   console.log('You are a kid.')
 // }
 //
 // console.log(arr);
 // for(var i=0; i<arr.length; i++){
 //   console.log(arr[i])
 // }
 //
 // arr.forEach(function(element){
 //   console.log(element);
 // })

 // var arr = [1, 2, 3, 4, 5, 6, 7];
 // let j = 0; //temporary variable
 // const ac = 0;

 // while(j<arr.length){
 //   console.log(arr[j])
 //   j++;
 // }
 //
 // do {
 //   console.log(arr[j]);
 //   j++;
 // } while (j<arr.length);


 // var arr = [1, 2, 3, 4, 5, 6, 7];
 // for(var i=0; i<arr.length; i++){
 //   if(i==2){
 //     // break;
 //     continue;
 //   }
 //   console.log(arr[i])
 // }

 // let myArr = ["Fan", "Camera", 34, null, true];
 // Array Methods
 // myArr.pop() // pops last element
 // myArr.push("ganesh");
 // myArr.shift() // pops first element
 // myArr.unshift()
 // const newLen = myArr.unshift("ganesh")
 // console.log(newLen)
 // console.log(myArr);


 // String methods in Javascript
 // let myString = "good boy."
 // console.log(myString.length)
 // console.log(myString.indexOf("boy"))
 //
 // let myDate = new Date();
 // console.log(myDate.getFullYear());

 //DOM Manipulation
 // let elem = document.getElementById('click');
 // console.log(elem);

 // let elemClass = document.getElementsByClassName("container");
 // console.log(elemClass);

 // elemClass[0].style.background = "yellow";
 // elemClass[0].classList.add("bg-primary");
 // elemClass[0].classList.add("text-success");

 // function clicked(){
 //   console.log("The button was clicked.")
 // }
 // window.onload = function(){
 //   console.log("The document was loaded.")
 // }
 //Events in Javascript
 // firstContainer.addEventListener('click', function(){
 //   document.querySelectorAll(".container")[1].innerHTML = "<b> We have clicked."
 //   console.log("Clicked!")
 // })        //firstContainer is ID so we can directly access it.
 //
 // firstContainer.addEventListener('mouseover', function(){
 //   console.log("Mouse on container")
 // })        //firstContainer is ID so we can directly access it.
 //
 //
 // let prevHTML = document.querySelectorAll(".container")[1].innerHTML;
 // firstContainer.addEventListener('mouseup', function(){
 //   document.querySelectorAll(".container")[1].innerHTML = prevHTML;
 //   console.log("Mouse up when clicked on container");
 // })        //firstContainer is ID so we can directly access it.

 // firstContainer.addEventListener('mousedown', function(){
 //   document.querySelectorAll(".container")[1].innerHTML = "<b> We have clicked.</b>"
 //   console.log("Mouse down when clicked on container");
 // })        //firstContainer is ID so we can directly access it.


 // function summm(a,b){
 //   return a+b;
 // }

 // Arrow Functions
 // summm = (a, b)=>{
 //   return a+b;
 // }
 //
 // logIt = ()=>{
 //   document.querySelectorAll(".container")[1].innerHTML = "<b>Set timeout fired</b>"
 //   console.log("I am your log.");
 // }
 //SetTimeOut and setinterval
 // clr = setTimeout(logIt, 5000);
 // clr = setInterval(logIt, 2000)

 // JavaScript localStorage
 // localStorage.setItem('name', 'ganesh')
 // localStorage.getItem('name')
 // localStorage.removeItem('name')
 // localStorage.clear()

 // json
 // onj = {name: "Ganesh", length: 1, a: {this: 'tha"t'}}
 // jso = JSON.stringify(onj);
 // console.log(jso)
 console.log(typeof onj)
 parsed = JSON.parse('{"name":"Ganesh","length":1,"a":{"this":"that"}}')
 console.log(parsed)
