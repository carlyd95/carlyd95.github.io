#include "include/stdio.h"
#include "include/stdlib.h"
#include "include/string.h"
#include "theos/include/readline/readline.h"

int main(int argc, char **argv, char **envp) {
	printf("Jakes Motto\n\n");
	char *anal = readline("Yes or No?\n");
	if (strcmp(anal, "yes") == 0) {
	printf("yes means rape\n");
	}else if (strcmp(anal, "no") == 0) {
	printf("no means yes, yes means rape\n");
	}else {
	printf("whatever you said means yes, yes means rape\n");}
return 0;
}

// vim:ft=objc
