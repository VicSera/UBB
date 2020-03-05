#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include "UI.h"

int main()
{
	ItemRepository* repository = createRepository(25);
	ItemService* service = createService(repository);
	UI* ui = createUI(service);

	char* command = (char*)malloc(60 * sizeof(char));

	while (1)
	{
		gets_s(command, 60);
		
		parseCommand(ui, command);
	}

	return 0;
}