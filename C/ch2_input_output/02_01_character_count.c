#include <stdio.h>

// Create a program that prompts for an input string and displays
// output that shows the input string and the number of characters
// the string contains. 

// From K & R book
int main() {
	long nc;
	nc = 0;

	while(getchar() != EOF) {
		++nc;
	}

	printf("%d\n", nc);
}
