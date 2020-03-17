#include "UI.h"

UI* createUI(ItemService* itemService)
{
	UI* ui = (UI*)malloc(sizeof(UI));

	if (!ui)
		return ALLOCATION_ERROR;

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
	char commandBuffer[MAX_COMMAND_LENGTH];

	while (TRUE)
	{
		gets_s(commandBuffer, MAX_COMMAND_LENGTH);

		parseCommand(ui, commandBuffer);
	}
}

void parseCommand(UI* ui, char* command)
{
	char* arguments[MAX_ARGUMENTS];
	unsigned int argumentCount = 0;

	arguments[argumentCount] = strtok(command, ", ");
	while (arguments[argumentCount])
	{
		arguments[++argumentCount] = strtok(NULL, ", ");
	}

	commandHandler handler = getCommandHandler(arguments[0]);
	if (!handler)
	{
		if (strcmp(arguments[0], "exit") == 0)
		{
			freeAllMemory(ui);
			_CrtDumpMemoryLeaks();
			exit(0);
		}

		printf("Invalid command!\n");
		return;
	}

	handler(ui, arguments, argumentCount);
}

commandHandler getCommandHandler(char* command)
{
	static unsigned int numberOfCommands = 6;
	static commandHandler handlers[] = {
		handleAdd, handleUpdate, handleRemove, handleDisplay, handleUndo, handleRedo
	};
	static const char* commands[] = {
		"add", "update", "delete", "list", "undo", "redo"
	};

	for (unsigned int i = 0; i < numberOfCommands; ++i)
		if (strcmp(command, commands[i]) == 0)
			return handlers[i];

	return NULL;
}

static void print(Vector* itemVector)
{
	static char* printFormat = "%u - %s - %s - %u\n";
	Item** items = getItems(itemVector);

	for (unsigned int index = 0; index < itemVector->count; ++index)
	{
		Item* item = items[index];
		printf(printFormat, item->catalogueNumber, item->state, item->type, item->value);
	}
}

void handleDisplay(UI* ui, char** arguments, unsigned int argumentCount)
{
	Vector* itemVector;

	if (argumentCount == 1)
		itemVector = serviceGetItems(ui->itemService);
	else
	{
		// There are two cases here - filter by type or by max value
		if (isNumber(arguments[1]))
		{
			unsigned int maxValue = strtoul(arguments[1], NULL, NUMERATION_BASE);
			itemVector = serviceGetFilteredItems(ui->itemService, filterByMaxValue, &maxValue);

			if (argumentCount == 3 && strcmp(arguments[2], "descending") == 0)
				sort(itemVector, orderedByNameReverse);
			else
				sort(itemVector, orderedByName);
		}
		else
		{
			if (argumentCount == 3 && strcmp(arguments[1], "toomuch") == 0)
			{
				// Filter by the length of the type - the old merchant can't remember long names!
				unsigned int maxLength = strtoul(arguments[2], NULL, NUMERATION_BASE);
				itemVector = serviceGetFilteredItems(ui->itemService, filterByTypeLength, maxLength);
			}
			else
			{
				// Filter by type
				char* type = arguments[1];
				itemVector = serviceGetFilteredItems(ui->itemService, filterByType, type);
			}
		}
	}

	if (itemVector)
	{
		print(itemVector);
		freeVector(itemVector);
	}
}

void handleAdd(UI* ui, char** arguments, unsigned int argumentCount)
{
	// Read the object data
	unsigned int catalogueNumber = strtoul(arguments[1], NULL, NUMERATION_BASE);
	unsigned int value = strtoul(arguments[4], NULL, NUMERATION_BASE);
	char* type = arguments[3];
	char* state = arguments[2];

	int errorCode = serviceAddItem(ui->itemService, catalogueNumber, state, type, value);

	if (errorCode != DONE)
		printf("No! (%d)\n", errorCode);
}

void handleRemove(UI* ui, char** arguments, unsigned int argumentCount)
{
	unsigned int catalogueNumber = strtoul(arguments[1], NULL, NUMERATION_BASE);

	int errorCode = serviceDeleteItem(ui->itemService, catalogueNumber);

	if (errorCode != DONE)
		printf("No!\n");
}

void handleUpdate(UI* ui, char** arguments, unsigned int argumentCount)
{
	// Read the object data
	unsigned int catalogueNumber = strtoul(arguments[1], NULL, NUMERATION_BASE);
	unsigned int value = strtoul(arguments[4], NULL, NUMERATION_BASE);
	char* type = arguments[3];
	char* state = arguments[2];

	int errorCode = serviceUpdateItem(ui->itemService, catalogueNumber, state, type, value);

	if (errorCode != DONE)
		printf("No!\n");
}

void handleUndo(UI* ui, char** arguments, unsigned int argumentCount)
{
	int errorCode = serviceUndo(ui->itemService);

	if (errorCode != DONE)
		printf("No!\n");
}

void handleRedo(UI* ui, char** arguments, unsigned int argumentCount)
{
	int errorCode = serviceRedo(ui->itemService);

	if (errorCode != DONE)
		printf("No!\n");
}

static int isNumber(char* string)
{
	for (int i = 0; i < strlen(string); ++i)
		if (string[i] < '0' || string[i] > '9')
			return FALSE;
	return TRUE;
}