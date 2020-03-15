#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include "UI.h"

int main()
{
	ItemRepository* repository = createRepository(25);
	ItemService* service = createService(repository);
	UI* ui = createUI(service);

	launch(ui);

	return 0;
}