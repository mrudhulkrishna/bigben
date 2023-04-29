// odd or even
// **************************************

// var a=5

// if(a % 2 == 0){
//    console.log(a +' is even') 
// }
// else{
//     console.log(a + ' is odd')
// }

// **************************************
//    armstrong numbers Or not
// **************************************

var  num=153;
var  sum=0

while(num > 0){
    // console.log(num)
    remainder = num % 10
    sum += remainder * remainder * remainder
    // console.log(sum)
    num = num/10
}
if(num == sum){
    console.log('armstrong number')

}
else{
    console.log(' not armstrong number') 
}


