const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello W";

function rotatestr(str,amt){
    var newstring =""
    for (let i=str.length-amt; i<str.length;i++) {
        newstring +=(str[i])
    }
    for (let i=0;i<str.length-amt;i++){
        newstring += (str[i]);
    }
    return newstring
}
console.log(rotatestr("Hello World",6))