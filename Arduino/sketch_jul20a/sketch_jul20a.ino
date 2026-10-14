void setup() {
  pinMode(7,INPUT);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(7)){
      Serial.println("Ok");
      delay(200);
    }
}
