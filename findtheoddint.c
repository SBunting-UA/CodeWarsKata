#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

struct Num{
  int value;
  int numOccurrences;
} Num;

int cmpfunc(const void * a, const void * b){
   return ( *(int*)a - *(int*)b );
}

int find_odd (size_t length, const int array[length]){
  size_t i;
  size_t k;
  char a = 'b';
  int j = 0;
  struct Num numbs[100];
  
  qsort(array, length, sizeof(int), cmpfunc);
  
  for(i = 0; i < length; i++){
    
    if(a == 'b'){
      numbs[j].value = array[i];
      numbs[j].numOccurrences = 1;
      a = 'c';
      continue;
      //goto endpoint;
    }
    
    if(numbs[j].value == array[i]){
      numbs[j].numOccurrences++;
    } else {
      ++j;
      numbs[j].value = array[i];
      numbs[j].numOccurrences = 1;
    }
    
    //endpoint:
  } 
  
  for (k = 0; k < sizeof(numbs); k++){
    if ((numbs[k].numOccurrences % 2) == 1){
      return numbs[k].value;
    }
  }
  
  return 0;
}
