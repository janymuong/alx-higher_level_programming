#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - C code checks if a singly linked list has a cycle in it.
 *
 * @list: pointer to head node of SLL
 *
 * Return: 1 if there is a cycle, 0 if false.
 */
int check_cycle(listint_t *list)
{
	listint_t *list_cycle;

	while (list != NULL)
	{
		list_cycle = list;
		list = list->next;
		if (list_cycle <= list)
			return (1);
	}
	return (0);
}
