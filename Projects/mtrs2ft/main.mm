#include "include/stdio.h"
#include "include/stdlib.h"
#include "theos/include/readline/readline.h"

int main(int argc, char **argv, char **envp) {

    //
	printf("Meters2Feet\n\n");
	char *input = readline("How many meters would you like to convert?\n");
	double feet = atoi(input) * 3.28;
	double ft;
	double in = modf(feet, &ft) * 12;
	printf("%s meters is %.0f feet and %.2f inches.\n", input, ft, in);
	return 0;
}

// vim:ft=objc
