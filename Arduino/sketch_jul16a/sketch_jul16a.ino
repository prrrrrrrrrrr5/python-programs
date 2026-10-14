void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int luce=analogRead(A0);
  Serial.println(luce);
  if (luce<750){
      digitalWrite(13,HIGH);
  } else {
      digitalWrite(13,LOW);
    }
  delay(100);
}
