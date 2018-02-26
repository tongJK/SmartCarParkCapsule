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

int sleep = 1;
int wait = 1000;
int numstep_x = 4000 ;
int numstep_z ;
int numstep_plate ;
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
    
}

void loop(){
   ch = Serial.read();   
   z_slot(ch);   
}

void z_slot(char ch){
    if(ch == 'a'){
    numstep_z = 2200;
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

    if(ch == 'b'){
    numstep_z = 4400;
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

    if(ch == 'c'){
    numstep_z = 6600;
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

    if(ch == 'd'){
    numstep_z = 8800;
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

}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void plateround(){
      //if(ch == 'z'){
       numstep_plate = 500;
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
       numstep_plate = 500;
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
  



