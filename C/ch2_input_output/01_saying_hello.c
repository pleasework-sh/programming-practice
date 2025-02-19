#include <stdio.h>

// A program that takes a user's name and greets them

int main() {
	char name[30];

	printf("Hi there! What is your name? ");
	scanf("%s", name);

	printf("Hello %s, it is nice to meet you!", name);

	return 0;
}
