#include <stdio.h>

// Create a program that prompts for an input string and displays
// output that shows the input string and the number of characters
// the string contains. 

int main() {
	char buffer[1000];
	
	printf("buffer %s", buffer);
	printf("Enter your string. ");
	fgets(buffer, sizeof(buffer), stdin);
	printf("You entered: %s with size %d", buffer, sizeof(buffer));
	
	for(int i = 0; i < sizeof(buffer); i++) {
		putchar(buffer[i]);
	}
}
