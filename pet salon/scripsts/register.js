let petSalon={//obj
    name: "Pet Salon",
    phone: 999-999-9999,//var
    hhours:{
        open:"9:00 am",
        close:"9:00 pm"
    },

        pets:[]
}
//constructor...
function pet(name,age,gender,service){
   // properties = parameters;
    this.name=name;
    this.age=age;
    this.gender=gender;
    this.service=service;
}


function register(){

}
function init(){
    let pet1 = new pet("scooby",79,"Male","grooming");// declaring obj
    petSalon.pets.push(pet1);
console.log(petSalon.pets);

}

window.onload=init;//waiting to render the html