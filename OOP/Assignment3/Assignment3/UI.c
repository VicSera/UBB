#include "UI.h"

UI* createUI(ItemService* itemService)
{
	UI* ui = (UI*)malloc(sizeof(UI));
	ui->itemService = itemService;

	return ui;
}

void freeAllMemory(UI* ui)
{
	freeService(ui->itemService);
	free(ui);
}

void launch(UI* ui)
{
	char* command = (char*)malloc(60 * sizeof(char));

	while (1)
	{
		gets_s(command, 60);

		parseCommand(ui, command);
	}
}

void parseCommand(UI* ui, char* command)
{
	char* arguments[10];
	unsigned int argumentCount = 0;

	arguments[argumentCount] = strtok(command, ", ");
	while (arguments[argumentCount])
	{
		arguments[++argumentCount] = strtok(NULL, ", ");
	}

	// Depending on the command, the right handling function has to be called
	if (strcmp(arguments[0], "add") == 0)
		handleAdd(ui, arguments, argumentCount);
	else if (strcmp(arguments[0], "update") == 0)
		handleUpdate(ui, arguments, argumentCount);
	else if (strcmp(arguments[0], "delete") == 0)
		handleRemove(ui, arguments, argumentCount);
	else if (strcmp(arguments[0], "list") == 0)
		display(ui, arguments, argumentCount);
	else if (strcmp(arguments[0], "exit") == 0)
	{
		free(command);
		freeAllMemory(ui);
		_CrtDumpMemoryLeaks();
		exit(0);
	}
}

void print(Item** items, unsigned int count)
{
	char* printFormat = "%u - %s - %s - %u\n";

	for (unsigned int index = 0; index < count; ++index)
	{
		Item* item = items[index];
		printf(printFormat, item->catalogueNumber, item->state, item->type, item->value);
	}
}

void display(UI* ui, char** arguments, unsigned int argumentCount)
{
	unsigned int count = 0;
	Item** items;

	if (argumentCount == 1)
		items = getItems(ui->itemService, &count);
	else
		items = getItemsByType(ui->itemService, arguments[1], &count);

	print(items, count);
}

void handleAdd(UI* ui, char** arguments, unsigned int argumentCount)
{
	// Read the object data
	unsigned int catalogueNumber = strtoul(arguments[1], NULL, 10);
	unsigned int value = strtoul(arguments[4], NULL, 10);
	char* type = arguments[3];
	char* state = arguments[2];

	int errorCode = addItem(ui->itemService, catalogueNumber, state, type, value);

	if (errorCode == -1)
		printf("No!\n");
}

void handleRemove(UI* ui, char** arguments, unsigned int argumentCount)
{
	unsigned int catalogueNumber = strtoul(arguments[1], NULL, 10);

	int errorCode = deleteItem(ui->itemService, catalogueNumber);

	if (errorCode == -1)
		printf("No!\n");
}

void handleUpdate(UI* ui, char** arguments, unsigned int argumentCount)
{
	// Read the object data
	unsigned int catalogueNumber = strtoul(arguments[1], NULL, 10);
	unsigned int value = strtoul(arguments[4], NULL, 10);
	char* type = arguments[3];
	char* state = arguments[2];

	int errorCode = updateItem(ui->itemService, catalogueNumber, state, type, value);

	if (errorCode == -1)
		printf("No!\n");
}