#include <Servo.h> 
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *motor_a = AFMS.getMotor(1);
Adafruit_DCMotor *motor_b = AFMS.getMotor(2);
Adafruit_DCMotor *motor_c = AFMS.getMotor(3);
Adafruit_DCMotor *motor_d = AFMS.getMotor(4);
String reading = "";
int comma_index;
String first_values;
String second_values;
int right_values;
int left_values;

void setup() {
  AFMS.begin(); 
  Serial.begin(9600);
  motor_a->setSpeed(0);
  motor_b->setSpeed(0);
  motor_c->setSpeed(0);
  motor_d->setSpeed(0);
}

void loop() {
  if (Serial.available() > 0) {
    reading = Serial.readStringUntil('\n'); // read from buffer until newline
    comma_index = reading.indexOf(',');
    first_values = reading.substring(0, comma_index);
    second_values = reading.substring(comma_index+1,reading.length());
    left_values = first_values.toInt();
    right_values = second_values.toInt();
   }
   right();
   left();
}

void right(){
  //make right turn
  if (right_values > 0){
    motor_a->run(FORWARD);
    motor_b->run(FORWARD);
    motor_a->setSpeed(right_values);
    motor_b->setSpeed(right_values);
  }
  //make left turn
  if (right_values < 0){
    motor_a->run(BACKWARD);
    motor_b->run(BACKWARD);
    motor_a->setSpeed(abs(right_values));
    motor_b->setSpeed(abs(right_values));
  }
  if (right_values == 0){
    motor_a->run(FORWARD);
    motor_b->run(FORWARD);
    motor_a->setSpeed(0);
    motor_b->setSpeed(0);
  }
}

void left(){
  //make right turn
  if (left_values > 0){
    motor_c->run(FORWARD);
    motor_d->run(FORWARD);
    motor_c->setSpeed(left_values);
    motor_d->setSpeed(left_values);
  }
  //make left turn
  if (left_values < 0){
    motor_c->run(BACKWARD);
    motor_d->run(BACKWARD);
    motor_c->setSpeed(abs(left_values));
    motor_d->setSpeed(abs(left_values));
  }
    if (left_values == 0){
    motor_c->run(FORWARD);
    motor_d->run(FORWARD);
    motor_c->setSpeed(0);
    motor_d->setSpeed(0);
  }
}
  
