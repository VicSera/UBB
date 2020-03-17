#include "Item.h"

Item* createItem(unsigned int catalogueNumber, char* state, char* type, unsigned int value)
{
	Item* item = (Item*)malloc(sizeof(Item));

	if (!item)
		return NULL;

	item->state = (char*)malloc((strlen(state) + 1) * sizeof(char));
	item->type = (char*)malloc((strlen(type) + 1) * sizeof(char));

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

unsigned int getItemId(Item* item)
{
	return item->catalogueNumber;
}

Item* copyItem(Item* item)
{
	return createItem(
		item->catalogueNumber,
		item->state,
		item->type,
		item->value
	);
}

int orderedByName(Item* firstItem, Item* secondItem)
{
	if (strcmp(firstItem->type, secondItem->type) <= 0)
		return TRUE;
	return FALSE;
}

int orderedByNameReverse(Item* firstItem, Item* secondItem)
{
	if (strcmp(firstItem->type, secondItem->type) > 0)
		return TRUE;
	return FALSE;
}