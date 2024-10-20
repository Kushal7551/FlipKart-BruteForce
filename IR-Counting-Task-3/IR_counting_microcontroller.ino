#include <LiquidCrystal.h>

// Initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
const int IRSensorPin = 9;  // Pin connected to the IR sensor
int counter = 0;  // Variable to store the count
bool objectDetected = false;  

void setup() {
  // Set up the LCD's number of columns and rows (16x2 in this case)
  lcd.begin(16, 2);

  // Print "Hello, World!" to the LCD
  lcd.setCursor(0, 0);   // Set the cursor to the first column, first row
  // lcd.print(1);
}

void loop() {
  int sensorValue = digitalRead(IRSensorPin);  // Read IR sensor value

    // Check if the IR sensor detects an object
    if (sensorValue == LOW && !objectDetected) {  
        // Increment the counter when an object is detected
        objectDetected = true; 
        lcd.clear();
        lcd.print("The count is: ");
        lcd.print(counter);
        counter++;
         // Set the flag to prevent multiple counts
    } else if (sensorValue == HIGH) {
        // Reset the flag when the object moves away
        objectDetected = false;

    }

    // Display the counter on the seven-segment display
    
     
     delay(50);

  // No need to put anything in loop for this task
}
