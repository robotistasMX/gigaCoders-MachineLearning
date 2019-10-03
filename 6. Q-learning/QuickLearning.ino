/*
Robotistas
 _______________________________________
|    6    |    5    |    3    |    1    |
|Recepcion    May   |  Golem      Bano  |
|_________|___   ___|___   ___|_________|
|    7    |         4         |    2    |
| Entrada        chaBots        Cocina  |
|_________|___________________|_________|
*/
int currentRoom;
int target = 6;
int action = 0;
int num_random = 0;
int num_max = 0;
int n = 0; //epochs
int in = 0; //index
int sound = 10;

//cuartos del 1-7
int cuartos[7] = {7, 11, 8, 12, 9, 10, 13};

//Acciones-recompensas
//Posible: 0, No posible: -1 Target: 100
int rewards[7][7] =
{
  
  {-1, -1, 0, -1, -1, -1, -1},  //0
  {-1, -1, -1, 0, -1, -1, -1},  //1
  {0, -1, -1, 0, -1, -1, -1},   //2
  {-1, 0, 0, -1, 0, -1, 100},   //3
  {-1, -1, -1, 0, -1, 0, -1},   //4
  {-1, -1, -1, -1, 0, -1, 100}, //5
  {-1, -1, -1, -1, -1, 0, 100}  //6
   
};

int weights[7][7];

void turnOn(int n)
{

  digitalWrite(cuartos[n], HIGH);
  
}

void turnOff()
{
  
  for(int i = 0; i < 7; i++)
    digitalWrite(cuartos[i], LOW);   
  
}

void room(int n)
{

  turnOff();
  turnOn(n);
  
}

void celebrate()
{
  
  for(int j = 0; j < 3; j++)
  {

    for(int i = 0; i < 7; i++)
      turnOn(i);

    delay(100);
    turnOff();
    delay(100);
    
  }
  
}

void setup()
{

  for(int i = 0; i < 7; i++)
  {

    for(int j = 0; j < 7; j++)
      weights[i][j] = 0;
    
  }

  for(int i = 0; i < 7; i++)
  {

    pinMode(cuartos[i], OUTPUT);
    digitalWrite(cuartos[i], LOW);
    
  }
  
}

void loop()
{

  //test();
  
  //Entrenamiento  
  while(n < 6)
  {
    
    while(currentRoom != target)
    {
      
      room(currentRoom);
      num_random = random(0, 7);

      while(rewards[currentRoom][num_random] < 0)
        num_random = random(0, 7);

      action = num_random;
      num_max = weights[action][0];

      for(int i = 1; i < 7; i++)
      {

        if(weights[action][i] > num_max)
          num_max = weights[action][i];
        
      }

      weights[currentRoom][action] = rewards[currentRoom][action] + 0.8 * num_max;
      currentRoom = action;
      delay(400);
            
    }

    room(target);
    delay(400);
    n++;
    currentRoom = 0;

    celebrate();
    delay(500);
    
  }

  //Evaluacion
  currentRoom = 0;

  while(currentRoom != target)
  {

    room(currentRoom);
    num_max = weights[currentRoom][0];
    in = 0;

    for(int i = 1; i < 7; i++)
    {

      if(weights[currentRoom][i] > num_max)
      {
        
        num_max = weights[currentRoom][i];
        in = i;  
        
      }
      
    }

    currentRoom = in;
    delay(1000);
    
  }
    
  room(target);
  delay(1000);
  celebrate();
  room(0);
  delay(1000);

}
