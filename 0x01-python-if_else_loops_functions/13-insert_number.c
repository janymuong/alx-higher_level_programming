#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to head of list
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;

	current_node = *head;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	if (!current_node || current_node->n >= number)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}
	return (new_node);
}
