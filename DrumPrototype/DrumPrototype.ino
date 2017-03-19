/*
  Jazzberry Pi Prototype (Built with Arduino)
  Team: 3Ten
  Members: Matthew Allemand, James Ostarly, William Williamson
*/

int actuator1 = 13;
int actuator2 = 12;
int actuator3 = 8;
int button2 = 2;
int button7 = 7;
int striketime = 100;
int resttime = 1000;
int counter = 1;
boolean stateB1;
boolean stateB2;
  
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(actuator1, OUTPUT);
  pinMode(actuator2, OUTPUT);
  pinMode(actuator3, OUTPUT);
  pinMode(button2, INPUT);
  pinMode(button7, INPUT);  
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(actuator1, LOW);
  digitalWrite(actuator2, LOW);
  digitalWrite(actuator3, LOW);
  delay(striketime);

  int button2_state = digitalRead(button2);
  int button7_state = digitalRead(button7);
  
  if(button2_state == HIGH) {
    if (stateB1) {
      stateB1 = false;
    } else {
      stateB1 = true;    
    }
    delay(resttime);
  }
  
  if(button7_state == HIGH) {
    if (stateB2) {
      stateB2 = false;
    } else {
      stateB2 = true;    
    }
    delay(resttime);
  }
  
  if (stateB1) {
     digitalWrite(actuator1, HIGH);
     delay(striketime);
     digitalWrite(actuator1, LOW);
     delay(500); 
     digitalWrite(actuator3, HIGH);
     delay(striketime);
     digitalWrite(actuator3, LOW);
     delay(500); 
     digitalWrite(actuator1, HIGH);
     delay(striketime);
     digitalWrite(actuator1, LOW);
     delay(500); 
     digitalWrite(actuator2, HIGH);
     delay(striketime);
     digitalWrite(actuator2, LOW);
     delay(500); 
     
  }
  
  if (stateB2) {
     digitalWrite(actuator1, HIGH);
     delay(striketime);
     digitalWrite(actuator1, LOW);
     delay(500); 
     digitalWrite(actuator3, HIGH);
     delay(striketime);
     digitalWrite(actuator3, LOW);
     delay(500);  
     digitalWrite(actuator2, HIGH);
     delay(striketime);
     digitalWrite(actuator2, LOW);
     delay(500); 
     digitalWrite(actuator3, HIGH);
     delay(striketime);
     digitalWrite(actuator3, LOW);
     delay(500);  
  }
  
  
  
//  if (button2_state == HIGH) {
//      digitalWrite(actuator1, HIGH);
//      delay(striketime);
//  } else if (button7_state == HIGH) {
//      digitalWrite(actuator2, HIGH);
//      delay(striketime);
//  }  
  
}

