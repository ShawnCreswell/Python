

// const str1 = "object oriented programming";
// const expexted1 = "OOP"

function create_acronym() {
    var acronym = [];
    let text = "object oriented programming"
    text = text.toUpperCase()
    const myArray = text.split(" ");

    for(let i = 0; i < myArray.length; i++) {
        // let myArray = str.split(" ")
        acronym.push(myArray[i][0]);
    }
    console.log(acronym)
}

create_acronym()