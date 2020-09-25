console.log("Ajax tutorial in one video by harry puttar.")

let fetchBtn = document.getElementById("fetchBtn")
fetchBtn.addEventListener('click', buttonClickHandler)

function buttonClickHandler() {
  console.log("hello")
  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();

  //Open the object
  xhr.open('GET', 'harry.txt', true);

  // What to do on progress (optional)
  xhr.onprogress = function() {
    console.log('On progress');
  }

  // What to do when response is ready
  xhr.onload = function() {
    console.log(this.responseText)
  }

  //send the request
  xhr.send();
}
