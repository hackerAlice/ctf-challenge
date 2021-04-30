#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *chunk;
	chunk = malloc(24);
	puts("Get input:");
	gets(chunk);
	return 0;
}
