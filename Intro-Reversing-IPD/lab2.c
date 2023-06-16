#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[]){
  if (argc==2) {
    printf("Checking License: %s\n", argv[1]);
    if (strcmp(argv[1], "Netacad-License-Key")==0) {
      printf("Access Granted\n");  
    } else {
      printf("Wrong!\n");
    }
  } else {
    printf("Useage: ./lab2 <key>\n");
  }
  return 0;
}
