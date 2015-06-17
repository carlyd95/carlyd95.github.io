#include "include/stdio.h"
#include "include/stdlib.h"
#include "theos/include/readline/readline.h"
#include "string.h"
int main(int argc, char **argv, char **envp) {
    printf("Meters2Feet\n\n");
    char *input = readline("How many meters would you like to convert?\n");
	float meter = atoi(input);
	if (meter > 1) {
	    char* string[] = "s";
	}else {
	    char* string[] = "";
}
	float feet = meter * 3.28;
	float inches = feet * 12.0;
	float remainder = fmodf(inches, 12);
	int total = (inches - remainder)/12;
	printf("%.2f meter%s =\n%.2f feet\n%.2f inches\n%i feet and %.2f inches.\n", meter, s, feet, inches, total,  remainder);
	return 0;
}

// vim:ft=objc
