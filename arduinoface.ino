/*
 * Liquid cristal faces
 */

// include the library code:
#include <LiquidCrystal.h>


// initialize the library with the numbers of the interface pins
//LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int  sleepyFace[2][16]={
 {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
 {0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0}
};

int  happyFace[2][16]={
 {0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0},
 {0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0}
};

int  angryFace[2][16]={
 {0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0},
 {0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0}
};

int  sadFace[2][16]={
 {0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0},
 {0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0}
};

int  normalFace[2][16]={
 {0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0},
 {0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0}
};

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);// set up the LCD's number of columns and rows: 
  analogWrite(8,15);
}

void loop() {

  neutral();
  delay(2000);
  
  happy();
  delay(2000);
  
  sleepy();
  delay(2000);  

  angry();
  delay(2000);  

  sad();
  delay(2000); 

  lcd.clear();
}

void neutral(){
  printFace(normalFace);
}
void happy(){
  printFace(happyFace);
}

void angry(){
  printFace(angryFace);
}

void sad(){
  printFace(sadFace);
}

void sleepy(){
  printFace(sleepyFace);
}

void printFace(int emo[][16]){
  lcd.clear();
  for(int i=0;i<2;i++){
    for(int j=0; j<16;j++){
      lcd.setCursor(j, i);    
      if(emo[i][j]==1){
        lcd.write(255);
      }
    }
  }
}
