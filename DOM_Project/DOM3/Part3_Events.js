// //Let's explore some events samples!

// var headOne = document.querySelector('#one')
// var headTwo = document.querySelector('#two')
// var headThree = document.querySelector('#three')

// // Hover (mouseover and mouseout)
// headOne.addEventListener('mouseover',function(){
//   headOne.textContent = "Mouse currently Over";
//   headOne.style.color = 'red';
// })

// headOne.addEventListener('mouseout',function(){
//   headOne.textContent = "Mouse Not On me."
//   headOne.style.color = 'blue';
// })


// // On Click
// headTwo.addEventListener("click",function(){
//   headTwo.textContent = "Clicked On";
//   headTwo.style.color = 'blue';
// })

// // Double Click
// headThree.addEventListener("dblclick",function(){
//   headThree.textContent = "Double Clicked!";
//   headThree.style.color = 'red';
// })

var headone= document.querySelector("#one");
var headtwo= document.querySelector("#two");
var headthree= document.querySelector("#three");


headone.addEventListener('mouseover',function(){
  headone.textcontent = "Mouse currently over";
  headone.style.color="red";
})

headone.addEventListener('mouseout',function(){
  headone.textcontent = "Mouse over me";
  headone.style.color="green";
})

headtwo.addEventListener("click",function(){
  headtwo.textContent = "Clicked";
  headtwo.style.color = "red";
})

headtwo.addEventListener("mouseout",function(){
  headtwo.textContent = "Click Over Me again..";
  headtwo.style.color = "purple";
})

headthree.addEventListener("dblclick",function(){
  headthree.textContent = "I was Double Clicked.";
  headthree.style.color = "blue";
})