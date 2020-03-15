#pragma once
#define _CRT_SECURE_NO_WARNINGS

#include "ItemService.h"
#include <stdio.h>
#include <crtdbg.h>

typedef struct _UI
{
	ItemService* itemService;
} UI;

UI* createUI(ItemService* itemService);

void freeAllMemory(UI* ui);

void launch(UI* ui);

void parseCommand(UI* ui, char* command);

void print(Item** items, unsigned int count);

void display(UI* ui, char** arguments, unsigned int argumentCount);

void handleAdd(UI* ui, char** arguments, unsigned int argumentCount);

void handleRemove(UI* ui, char** arguments, unsigned int argumentCount);

void handleUpdate(UI* ui, char** arguments, unsigned int argumentCount);