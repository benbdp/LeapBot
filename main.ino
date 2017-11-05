#include <Servo.h> 
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *motor_a = AFMS.getMotor(1);
Adafruit_DCMotor *motor_b = AFMS.getMotor(2);
Adafruit_DCMotor *motor_c = AFMS.getMotor(3);
Adafruit_DCMotor *motor_d = AFMS.getMotor(4);
String inString = "";
int set_speed;

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
    inString = Serial.readStringUntil('\n'); // read from buffer until newline
    set_speed = inString.toInt();
  }
  if (set_speed < 0) {
    reverse();
  }
  else if (set_speed > 0) {
    forward();
  }
  else if (set_speed == 0) {
    off();
  }
}


void reverse(){
  motor_a->run(FORWARD);
  motor_b->run(FORWARD);
  motor_c->run(BACKWARD);
  motor_d->run(BACKWARD);
  motor_a->setSpeed(abs(set_speed));
  motor_b->setSpeed(abs(set_speed));
  motor_c->setSpeed(abs(set_speed));
  motor_d->setSpeed(abs(set_speed));
}
void forward(){
  motor_a->run(BACKWARD);
  motor_b->run(BACKWARD);
  motor_c->run(FORWARD);
  motor_d->run(FORWARD);
  motor_a->setSpeed(set_speed);
  motor_b->setSpeed(set_speed);
  motor_c->setSpeed(set_speed);
  motor_d->setSpeed(set_speed);
}
void off(){
  motor_a->setSpeed(set_speed);
  motor_b->setSpeed(set_speed);
  motor_c->setSpeed(set_speed);
  motor_d->setSpeed(set_speed);
}

