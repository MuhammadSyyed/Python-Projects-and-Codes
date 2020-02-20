//Setting pins
const int vcc = 13; 
const int trigPin1 = 11; // trigger o/p sensr 1 
const int echoPin1 = 10; // Echo i/p sensr 1     
const int trigPin2 = 6;  // trigger o/p sensr 2
const int echoPin2 = 5;  // echo i/p sensr 2

// Considering Variables 

long duration;                               
int distance1, distance2; 
float r;
unsigned long temp=0;
int temp1=0;
int l=0; // for special purpose of identification

//Defining function for distance

void find_distance (void);
//  main function of distance
void find_distance (void)                   
{ 
  // left sensor 
  digitalWrite(trigPin1, LOW);  // low for 0 // high for 1 // delay in ms
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  
  // time calcultion of receiving signal
  
  duration = pulseIn(echoPin1, HIGH, 5000);
  
  r = 3.4 * duration / 2;                  // calculation in cm because cm mein hoti hai 340/100 
  distance1 = r / 100.00;
  
  // Working of right sensor
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);

  duration = pulseIn(echoPin2, HIGH, 5000);
  r = 3.4 * duration / 2;     
  distance2 = r / 100.00;
  delay(100);
}
// those things which should be run at once 
void setup() 
{
  Serial.begin(9600); //serial for instance of specific port timings
  pinMode(trigPin1, OUTPUT); // defining behaviour of every pin
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(vcc,OUTPUT);
  delay (1000);
    
}
// for continuous loop
void loop()
{
  digitalWrite(vcc, HIGH); // We asssumed this pin for getting an extra vcc pin always high
  
  find_distance(); // for getting distance continuously
  
  if(distance2<=30 && distance2>=15) // checking range from 15 to 30 cm
  { 
    temp=millis();                   // store current time for comaparing in ms
    while(millis()<=(temp+300))      // Futher checking for 300 ms to identify gesture
    find_distance();
    if(distance2<=30 && distance2>=15) // if statement for identificaion
    {
     temp=distance2;                         // store Position of hand for comparing
     while(distance2<=50 || distance2==0)    // loop to check whether hand is still there
     {
       find_distance();                      // call to get latest distance
       if((temp+6)<distance2)                // checking movement away from sensor    // +- 6 calibration k lie kia hai
       {
       Serial.println("down");               // send "down" serially.
       }
       else if((temp-6)>distance2)           // checking movement closer to the sensor
       {
        Serial.println("up");                // send "up" serially.
       }
     }
    }
    else                                     // this condition becomes true, if we only swipe in front of the right sensor . 
    {
      Serial.println("next");                // send "next" serially.
    }
  }

  else if(distance1<=30 && distance1>=15)   // calculation for left sensor
  { 
  
    temp=millis();                           
  
    while(millis()<=(temp+300))             
    {
       find_distance();
       if(distance2<=30 && distance2>=15)  // checking movement of hand in from os both sensors left + right
       {
         Serial.println("change");         // send "change" serially.
         l=1;                              // store 1 in variable l for flagging usage
         break;                            // breaking loop
       }
    }
    
    if(l==0)                               // if only movement in left sensor
    {
    Serial.println("previous");            // send "previous" serially.
    while(distance1<=30 && distance1>=15) // loop to check stability of hand in left sensor
    find_distance();                      
    }
    l=0;                                  // make l=0 for the next round.
   }
   
}
