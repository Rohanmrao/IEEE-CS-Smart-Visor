// C++ code
//
#include <Servo.h>

int check_light = 0;

Servo servo_9;

void setup()
{
  pinMode(A0, INPUT);
  Serial.begin(9600);
  servo_9.attach(9, 500, 2500);
}

void loop()
{
  check_light = analogRead(A0);
  Serial.println(check_light);
  if (check_light < 550) 
  {
    servo_9.write(0);
  } 
  else 
  {
    servo_9.write(90);
  }
}