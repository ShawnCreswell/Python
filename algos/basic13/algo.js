

// const str1 = "object oriented programming";
// const expexted1 = "OOP"

// function create_acronym() {
//     var acronym = [];
//     let text = "object oriented programming"
//     text = text.toUpperCase()
//     const myArray = text.split(" ");

//     for(let i = 0; i < myArray.length; i++) {
//         // let myArray = str.split(" ")
//         acronym.push(myArray[i][0]);
//     }
//     console.log(acronym)
// }

// create_acronym()


/* 
Zip Arrays into Map
Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

// const keys1 = ["abc", 3, "yo"];
// const vals1 = [42, "wassup", true];
// const expected1 = {
//     abc: 42,
//     3: "wassup",
//     yo: true,
// };

// const keys2 = [];
// const vals2 = [];
// const expected2 = {};



/*
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
// function zipArraysIntoMap(keys, values) { }


// const keys1 = ["abc", 3, "yo"];
// const vals1 = [42, "wassup", true];

// function newobj (arr1, arr2) {
//     var expected = {};
//     for(let i = 0; i < arr1.length; i++) {
//         expected[arr1[i]] = arr2[i];
//     }
//     return expected;
// }

// console.log(newobj(keys1, vals1));

// const arr1 = ["a", "a", "a",]
// const expected1 = {
//     a: 3,
// };

// function makeFrequencyTable(arr){
//     var newObject = {};
//     var num = 0;
//     for (var i = 0; i < arr.length; i++){
//         if(arr[i] == "a"){
//             newObject[arr[i]] = (num += 1);
//         }
//     }return newObject;
// }

// console.log(makeFrequencyTable(["a", "a", "a"]));



// function makeFrequencyTable2(arr){
//     var newObject = {};
//     var numA = 0;
//     var numb = 0;
//     var numC = 0;
//     var numD = 0;
//     var numB = 0;


//     for(var i = 0; i < arr.length; i++){
//         if(arr[i] == "a"){
//             newObject[arr[i]] = (numA += 1)
//         }else if(arr[i] == "b"){
//             newObject[arr[i]] = (numb += 1)
//         } else if(arr[i] == "c"){
//             newObject[arr[i]] = (numC += 1)
//         }else if(arr[i] == "d"){
//             newObject[arr[i]] = (numD += 1)
//         }else 
//         newObject[arr[i]] = (numB += 1)
//     }return newObject;
// }

// console.log(makeFrequencyTable2(["a", "b", "a", "c", "B", "c", "c", "d"]));


// function makeFrequencyTable2(arr){
//     var newObj = {};
//     for(var i = 0; i < arr.length; i++){
//         if(newObj[arr[i]]){
//             newObj[arr[i]] =+ 1;
//         }
//         else{
//             newObj[arr[i]] = 1
//         }
//         return newObj;
//     }
// }


// function makeFrequencyTable2(arr) { 
//     obj = {};
//     for(let i = 0; i < arr.length; i++) {
//         if(obj[arr[i]]) {
//             obj[arr[i]] ++;
//         }
//         else {
//             obj[arr[i]] = 1;
//         }
//     }
//     return obj;
//     }

//     console.log(makeFrequencyTable2(["a", "b", "a", "c", "B", "c", "c", "d"]));


// const str1 = "abcABC";
// const expected1 = abcABC;

// const str2 = "helloo";
// const expected2 = "helo";


// function stringDeDupe(str){
//     let expected2 = " ";
//     obj = {};
//     for(let i = 0; i < str.length; i++){
//         if(obj[str[i]]){
//             obj[str[i]] ++;
//         }
//         else{
//             obj[str[i]] = 1;
//             expected2 += str[i];
            
//         }
//     } return expected2
// }
// console.log(stringDeDupe("helloo"))

// const str3 = "";
// const expected3 = "";

// const str4 = "aa";
// const expected4 = "a";


// function reverseWords(str){
//     var newString = " ";
//     const myArr = str.split(" ");
//     var firstWord = myArr[0];
//     var secondWord = myArr[1];

//     for(let i = 0; i < Math.floor(myArr.length / 2); i++){
//         var temp = myArr[i];
//         myArr[i] = myArr[myArr.length - 1 - i];
//         myArr[myArr.length - 1 - i] = temp;
//         newString = myArr[i];
//     }
//     return newString;
// }

// console.log(reverseWords("hello world"));

function reverseWords(str){
    var newArr = [];
    var myArr = str.split(" ");
    for(let i = 0; i < myArr.length; i++){
        var temp = " "
        for(let j = myArr[i].length - 1; j >= 0; j--){
            temp += myArr[i][j] 
        }
        newArr.push(temp)
    }  
    
    console.log(newArr.join(' '));
}

reverseWords("hello world");