#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include "UI.h"

#include "Tests.h"

#define RUN_TESTS 0

int main()
{

#if RUN_TESTS
	runVectorTests();
	runRepositoryTests();
	runServiceTests();

	exit(0);
#endif

	ItemRepository* repository = createRepository();
	ItemService* service = createService(repository);
	UI* ui = createUI(service);

	launch(ui);

	return 0;
}