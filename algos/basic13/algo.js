

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



function makeFrequencyTable2(arr){
    var newObject = {};
    var numA = 0;
    var numb = 0;
    var numC = 0;
    var numD = 0;
    var numB = 0;


    for(var i = 0; i < arr.length; i++){
        if(arr[i] == "a"){
            newObject[arr[i]] = (numA += 1)
        }else if(arr[i] == "b"){
            newObject[arr[i]] = (numb += 1)
        } else if(arr[i] == "c"){
            newObject[arr[i]] = (numC += 1)
        }else if(arr[i] == "d"){
            newObject[arr[i]] = (numD += 1)
        }else 
        newObject[arr[i]] = (numB += 1)
    }return newObject;
}

console.log(makeFrequencyTable2(["a", "b", "a", "c", "B", "c", "c", "d"]));



// const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"]
// const expexted2 = {
//     a: 2,
//     b: 1,
//     c: 3,
//     B: 1,
//     d: 1,
// };