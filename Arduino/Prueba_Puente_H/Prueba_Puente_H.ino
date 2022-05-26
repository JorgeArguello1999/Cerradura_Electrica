/* Prueba del Puente H (L293D) 
Dibujo de las conexiones en www.elprofegarcia.com

ARDUINO   L293D(Puente H)        
  5          10
  6          15
  9          7
  10         2
  5V         1, 9, 16
  GND        4, 5, 12, 13
  
  El motor 1 se conecta a los pines 3 y 6 del Puente H
  El motor 2 se conecta a los pines 11 y 14 del Puente H
  
  La fuente de alimentacion de los Motores se conecta a tierra y
  el positivo al pin 8 del puennte H.  

*/
int izqA = 5; 
int izqB = 6; 
int derA = 9; 
int derB = 10; 
int vel = 255; // Velocidad de los motores (0-255)
int led_S= 13; // Pines de conexion para led's
int led_N= 15; // Pin de conexion led
int salida;

void setup()  { 
  Serial.begin(9600);
  pinMode(derA, OUTPUT);
  pinMode(derB, OUTPUT);
  pinMode(izqA, OUTPUT);
  pinMode(izqB, OUTPUT);
 } 
 
void loop()  { 
  /*
    Serial.println("Detenido");
    analogWrite(derB, 0);  // Detiene los Motores
    analogWrite(izqB, 0); 
    delay (500);
    
    Serial.println("Frente");
    analogWrite(derA, vel);  // Frente 2 segundos
    analogWrite(izqA, vel); 
    delay (2000);
    
    Serial.println("Derecha");
    analogWrite(derA, vel);  // Derecha 0,5 segundos
    analogWrite(izqA, 0); 
    delay (500);

    Serial.print("Izquierda")
    analogWrite(derA, 0);    // Izquierda 0,5 segundos
    analogWrite(izqA, vel); 
    delay (500);
    
    Serial.println("Detenido");
    analogWrite(derA, 0);    // Detiene los Motores
    analogWrite(izqA, 0);
    delay (500);

    Serial.println("Reversa");
    analogWrite(derB, vel);  // Reversa 2 segundos
    analogWrite(izqB, vel); 
    delay (2000);                      
    */
    if(Serial.available()>0){
        salida=Serial.read();
        Serial.println(salida);
        if(salida=='S'){
          digitalWrite(led_S, HIGH);

          Serial.println("Derecha");
          analogWrite(derA, vel);   // Los mueve a la derecha
          delay(5000);

          Serial.println("Detenido");
          analogWrite(derA, 0);    // Detiene los Motores
          delay(2000);

          /*Serial.println("Reversa");
          analogWrite(derB, vel);  // Reversa 2 segundos
          // analogWrite(izqB, vel);
          delay(5000);

          Serial.println("Detenido");
          analogWrite(derA, 0);    // Detiene los Motores
          analogWrite(izqA, 0);
          */
                   
        }
        if(salida=='N'){
          digitalWrite(led_N, HIGH);
          delay(2000);

          Serial.println("Detenido");
          analogWrite(derA, 0);    // Detiene los Motores
          analogWrite(izqA, 0);
        }
      
    }
}
