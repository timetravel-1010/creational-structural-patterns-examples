/**
 * Clase que clona un objecto
 */
class appointmentPrototype {
    constructor(proto){
        this.proto = proto;
        return this.clone();
    }

    clone(){
        let appointment_ = new appointment();
        appointment_.doctor = this.proto.doctor;
        appointment_.patient = this.proto.patient;
        appointment_.price = this.proto.price;
        appointment_.appointmentType = this.proto.appointmentType;

        return appointment_;
    }
}

/**
 * Clase de objecto inicial
 */
class appointment{

    constructor(doctor, patient, price, appointmentType){
        this.doctor = doctor;
        this.patient = patient;
        this.price = price;
        this.appointmentType = appointmentType;

        this.status = 0;
    }

    startAppointment(){
        this.status=1;
    }

}

/* Prototipo de cita de psicologia */
let appointmentPrototypePsychology = 
    new appointment("Juan","Manuel","8.000","psychology");
//appointmentPrototypePsychology.startAppointment();
/* Prototipo de cita de oncologia */
let appointmentPrototypeOncology = 
    new appointment("Juan","Manuel","7.000","oncology");
/* Clone de cita de psicologia*/
let Clone1 = 
    new appointmentPrototype(appointmentPrototypePsychology);

//Clone1.patient= "Daniel";

/* Clone de cita de Oncologia*/
let Clone2 = 
    new appointmentPrototype(appointmentPrototypeOncology);

console.log(appointmentPrototypePsychology);
//console.log(appointmentPrototypeOncology);
console.log(Clone1);
//console.log(Clone2);
