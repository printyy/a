void setup() {
  pinMode(8, OUTPUT);  // Green LED
  pinMode(9, OUTPUT); // Red LED
  pinMode(10, OUTPUT); // Yellow LED
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char color = Serial.read();
    if(color == 'G')
    {
      digitalWrite(8, HIGH);
      digitalWrite(9, LOW);
      digitalWrite(10, LOW);
    }
    else if(color == 'R')
    {
      digitalWrite(9, HIGH);
      digitalWrite(8, LOW);
      digitalWrite(10, LOW);
    }
    else if(color == 'Y')
    {
      digitalWrite(10, HIGH);
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
    }
    /*
    digitalWrite(8, color == 'G');
    digitalWrite(9, color == 'R');
    digitalWrite(10, color == 'Y');
    */
  }
}
