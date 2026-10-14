char comando;

void setup() {
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  comando=Serial.read();
  if (comando== 'i'){
      digitalWrite(13,HIGH);
      Serial.println("ON 13");
    }
  if (comando== 'o'){
      digitalWrite(13,LOW);
      Serial.println("OFF 13");
    }
  
}
