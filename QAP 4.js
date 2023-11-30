// MotelCustomer object definition
function MotelCustomer(name, birthDate, gender, roomPreferences, paymentMethod, mailingAddress, phoneNumber, checkInDate, checkOutDate) {
    this.name = name;
    this.birthDate = birthDate;
    this.gender = gender;
    this.roomPreferences = roomPreferences || [];
    this.paymentMethod = paymentMethod;
    this.mailingAddress = mailingAddress || {};
    this.phoneNumber = phoneNumber;
    this.checkInDate = checkInDate || {};
    this.checkOutDate = checkOutDate || {};

    // Method to calculate age
    this.calculateAge = function () {
        const today = new Date();
        const birthDate = new Date(this.birthDate);
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();

        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }

        return age;
    };

    // Method to calculate duration of stay in days
    this.calculateDurationOfStay = function () {
        const checkIn = new Date(this.checkInDate.year, this.checkInDate.month - 1, this.checkInDate.day);
        const checkOut = new Date(this.checkOutDate.year, this.checkOutDate.month - 1, this.checkOutDate.day);
        const millisecondsPerDay = 24 * 60 * 60 * 1000;
        const durationInDays = Math.round(Math.abs((checkOut - checkIn) / millisecondsPerDay));

        return durationInDays;
    };

    // Method to generate a description of the customer
    this.generateCustomerDescription = function () {
        const age = this.calculateAge();
        const durationOfStay = this.calculateDurationOfStay();

        return `Customer Name: ${this.name}\nAge: ${age} years\nGender: ${this.gender}\nRoom Preferences: ${this.roomPreferences.join(', ')}\nPayment Method: ${this.paymentMethod}\nMailing Address: ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.state}, ${this.mailingAddress.zip}\nPhone Number: ${this.phoneNumber}\nCheck-in Date: ${this.checkInDate.month}/${this.checkInDate.day}/${this.checkInDate.year}\nCheck-out Date: ${this.checkOutDate.month}/${this.checkOutDate.day}/${this.checkOutDate.year}\nDuration of Stay: ${durationOfStay} days`;
    };
}

// Example usage
const customer1 = new MotelCustomer(
    "Lucas Keats",
    "2002-05-15",
    "Male",
    ["Non-smoking", "King bed"],
    "Credit Card",
    { street: "123 Main St", city: "San francisco", state: "CA", zip: "12345" },
    "555-1234",
    { month: 11, day: 20, year: 2023 },
    { month: 11, day: 27, year: 2023 }
);

// Generate and log customer description
console.log(customer1.generateCustomerDescription());