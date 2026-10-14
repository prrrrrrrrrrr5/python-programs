int key[3]={LOW,LOW,LOW};
int pin[3]={7,8,9};
int i;

void setup() {
  for (i=0; i<3; i++){
    pinMode(pin[i],INPUT);
  }
}

void loop() {
  for (i=0; i<3; i++){
    if (digitalRead(pin[i])==HIGH){
      key[i]=!key[i];
      delay(200);
    }
  }
  for (i=0; i<3; i++){
    if (key[i]==HIGH){
      digitalWrite(13,HIGH);
    } else {
        digitalWrite(13,LOW);
      }
  }
}
