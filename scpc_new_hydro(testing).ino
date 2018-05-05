#include <Wire.h>

#define SLAVE_ADDRESS 0x04
#define DIR1_PIN 2
#define STEP1_PIN 3
#define DIR2_PIN 4
#define STEP2_PIN 5
#define DIR3_PIN 6
#define STEP3_PIN 7

//int numstep=520; // 90 Degree
/*int numstep_x = 1100;
int numstep_z = 2200;
int numstep_plate = 25;*/

int state = 0;
int flr,slt;
char fr;

int sleep = 1;
int wait = 1000;
int numstep_x = 4000 ;
int numstep_z ;
int numstep_plate = 25;
int microstep = 200;

char ch;
int i,j;


void z_slot(char ch);


void setup(){
    pinMode(DIR1_PIN, OUTPUT);
    pinMode(STEP1_PIN, OUTPUT);
    pinMode(DIR2_PIN, OUTPUT);
    pinMode(STEP2_PIN, OUTPUT);
    pinMode(DIR3_PIN, OUTPUT);
    pinMode(STEP3_PIN, OUTPUT);
    
    Serial.begin(9600);
    Wire.begin(SLAVE_ADDRESS);
    Wire.onReceive(receiveData);
    
}

void loop(){
   delay(100);   
}

void z_slot(char x, char y){
  
      fslide();
      delay(sleep);
      pickup();
      delay(wait);
      bslide();
      delay(sleep);
      plateround();
      delay(wait);
      
      //up
       digitalWrite(DIR1_PIN,HIGH);
       for(int i=0;i<numstep_z;i++){
          //if(digitalRead(SW)==1){
           digitalWrite(STEP1_PIN,LOW);
           delay(sleep);
           digitalWrite(STEP1_PIN,HIGH);
           delay(sleep);  
         // }
       }

       fslide();
       delay(sleep);
       pickdown();
       delay(wait);
       bslide();

       //down
       digitalWrite(DIR1_PIN,LOW);
       for(int i=0;i<numstep_z;i++){
          //if(digitalRead(SW)==1){
           digitalWrite(STEP1_PIN,HIGH);
           delay(sleep);
           digitalWrite(STEP1_PIN,LOW);
           delay(sleep);
    }
    
       plateround_back();


}


void res_slot(char x, char y){
  
      plateround();
      delay(wait);

      //up
       digitalWrite(DIR1_PIN,HIGH);
       for(int i=0;i<numstep_z;i++){
          //if(digitalRead(SW)==1){
           digitalWrite(STEP1_PIN,LOW);
           delay(sleep);
           digitalWrite(STEP1_PIN,HIGH);
           delay(sleep);  
         // }
       }
      
      fslide();
      delay(sleep);
      pickup();
      delay(wait);
      bslide();
      delay(sleep);
      
      plateround_back();
      delay(wait);

      //down
       digitalWrite(DIR1_PIN,LOW);
       for(int i=0;i<numstep_z;i++){
          //if(digitalRead(SW)==1){
           digitalWrite(STEP1_PIN,HIGH);
           delay(sleep);
           digitalWrite(STEP1_PIN,LOW);
           delay(sleep);
    }
      

       fslide();
       delay(sleep);
       pickdown();
       delay(wait);
       bslide();
       delay(wait);

}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void plateround(){
      //if(ch == 'z'){
        digitalWrite(DIR3_PIN,HIGH);
        for(int i=0;i<numstep_plate;i++){
           digitalWrite(STEP3_PIN,LOW);
           delay(sleep);
           digitalWrite(STEP3_PIN,HIGH);
           delay(sleep);  
       }     
//}
  
  }
  
  void plateround_back(){
      //if(ch == 'z'){
        digitalWrite(DIR3_PIN,LOW);
        for(int i=0;i<numstep_plate;i++){
           digitalWrite(STEP3_PIN,HIGH);
           delay(sleep);
           digitalWrite(STEP3_PIN,LOW);
           delay(sleep);  
       }     
//}
  
  }

  void fslide(){
        digitalWrite(DIR2_PIN,HIGH);
        for(int i=0;i<numstep_x;i++){
           digitalWrite(STEP2_PIN,LOW);
           delay(sleep);
           digitalWrite(STEP2_PIN,HIGH);
           delay(sleep);  
       }    
  }

    void bslide(){
       digitalWrite(DIR2_PIN,LOW);
       for(int i=0;i<numstep_x;i++){
           digitalWrite(STEP2_PIN,HIGH);
           delay(sleep);
           digitalWrite(STEP2_PIN,LOW);
           delay(sleep);
       }   
  }

      void pickup(){
        digitalWrite(DIR1_PIN,HIGH);
        for(int i=0;i<microstep;i++){
           digitalWrite(STEP1_PIN,LOW);
           delay(sleep);
           digitalWrite(STEP1_PIN,HIGH);
           delay(sleep);  
       }    
  }

        void pickdown(){
       digitalWrite(DIR1_PIN,LOW);
       for(int i=0;i<microstep;i++){
           digitalWrite(STEP1_PIN,HIGH);
           delay(sleep);
           digitalWrite(STEP1_PIN,LOW);
           delay(sleep);
       }   
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

void receiveData(int byteCount) { 
    fr = Wire.read();

    flr = fr/10;
    slt = fr%10;

   Serial.print("FLOOR :");
   Serial.print(flr);
   Serial.print("\n");
   Serial.print("SLOT :");
   Serial.print(slt);
   Serial.print("\n");

   if(flr == 1)
     numstep_z = 0;
   if(flr == 2)
     numstep_z = 2200;
   if(flr == 3)
     numstep_z = 4400;
   if(flr == 4)
     numstep_z = 6600;

   numstep_plate = numstep_plate*slt ;

   Serial.print("numstep_z :");
   Serial.print(numstep_z);
   Serial.print("\n\n");

   if(flr < 4)
    res_slot(flr,slt);
   else
    z_slot(flr,slt);
}  

void sendData() {
  Wire.write(fr);
}

