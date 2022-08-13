#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "dog.h"

int main(){
  Dog* my_dog = dog_init("Frodo", "Jack Russel", 4);
  dog_bark(my_dog);
  return 0;
}
