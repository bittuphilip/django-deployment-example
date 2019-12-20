// alert("Welcome to your bank...");
// var deposit=prompt("Enter the number in pounds...");
// var convert=deposit*0.454;

// alert("Total wieght in kg:"+convert);

// console.log("Conversion Completed....");


// if (3>5) {
// 	console.log(true)
	
// } else {
// 	console.log(false)
	
// }

// for(var i=0;i<5;i++)
// {
// 	console.log("Number is:"+i)
// }

var arr = ['A','B','C']
// Don't do this!
// for (letter in arr) {
//   alert(letter);
// }

// // Because of this you will want to use a for/of loop. For example:
// for (letter of arr) {
//   alert(letter);
// }

arr.forEach(alert);


function awesomeAdder(name){
  console.log(name+" is awesome")
}

var topics = ["python",'django','science']

topics.forEach(awesomeAdder);
