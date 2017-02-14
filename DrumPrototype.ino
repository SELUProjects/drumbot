/*
  Jazzberry Pi Prototype (Built with Arduino)
  Team: 3Ten
  Members: Matthew Allemand, James Ostarly, William Williamson
*/

int actuator1 = 13;
int actuator2 = 12;
int button2 = 2;
int button7 = 7;
int striketime = 100;
int resttime = 1000;
  
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(actuator1, OUTPUT);
  pinMode(actuator2, OUTPUT);
  pinMode(button2, INPUT);
  pinMode(button7, INPUT);  
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(actuator1, LOW);
  digitalWrite(actuator2, LOW);
  delay(striketime);

  int button2_state = digitalRead(button2);
  int button7_state = digitalRead(button7);
  
  if (button2_state == HIGH) {
      digitalWrite(actuator1, HIGH);
      delay(striketime);
  } else if (button7_state == HIGH) {
      digitalWrite(actuator2, HIGH);
      delay(striketime);
  }  
  
}

