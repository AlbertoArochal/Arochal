class Car {
    motor = true;
    color = "red";
    wheels = 4;
    brand;

    constructor(color, brand, wheels) {
        this.color = color;
        this.brand = brand;
        this.wheels = wheels;
        this.run = () => alert("brun brun")
        this.dropMotor = () => this.motor = false
    }
}

let myCar = new Car("white", "seat", 6)
let javicar = new Car("green", "seat", 3)

console.log(javicar)
javicar.dropMotor()
console.log(javicar)

/////////////////////////////////////////////

