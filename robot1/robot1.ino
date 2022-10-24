#include<Servo.h>
#include <AFMotor.h>

Servo myservo;

// received data
byte val = "";

// setting up motor pins
AF_DCMotor motor1(1, MOTOR12_1KHZ);
AF_DCMotor motor2(2, MOTOR12_1KHZ);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // for communicating via serial port with Python
  myservo.attach(10);
  myservo.write(90);
}

void forward() {
  motor1.setSpeed(255);
  motor1.run(FORWARD);
  motor2.setSpeed(255);
  motor2.run(FORWARD);
  delay(4000);
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}

void backward() {
  myservo.write(360);
  motor1.setSpeed(255);
  motor1.run(BACKWARD);
  motor2.setSpeed(255);
  motor2.run(BACKWARD);
  delay(4000);
  myservo.write(90);
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}

void right() {
  myservo.write(0);
  delay(500);
  myservo.write(90);
  delay(500);
  motor1.setSpeed(255);
  motor1.run(FORWARD);
  motor2.setSpeed(255);
  motor2.run(BACKWARD);
  delay(2500);
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}

void left() {
  myservo.write(180);
  delay(500);
  myservo.write(90);
  delay(500);
  motor1.setSpeed(255);
  motor1.run(BACKWARD);
  motor2.setSpeed(255);
  motor2.run(FORWARD);
  delay(2500);
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}

void loop() {

  while(Serial.available() > 0)  //look for serial data available or not
  {
    val = Serial.read();        //read the serial value
  }
    if(val == 'f'){
      forward();
      }
    if(val == 'b'){
      backward();
      }
    if(val == 'l'){
      left();
      }
    if(val == 'r'){
      right();
      }
    val = "";
}
