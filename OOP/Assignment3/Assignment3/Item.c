#include "Item.h"

Item* createItem(unsigned int catalogueNumber, char* state, char* type, unsigned int value)
{
	Item* item = (Item*)malloc(sizeof(Item));
	item->state = (char*)malloc(30 * sizeof(char));
	item->type = (char*)malloc(30 * sizeof(char));

	item->catalogueNumber = catalogueNumber;
	strcpy(item->state, state);
	strcpy(item->type, type);
	item->value = value;

	return item;
}

void freeItem(Item* item)
{
	free(item->state);
	free(item->type);
	free(item);
}