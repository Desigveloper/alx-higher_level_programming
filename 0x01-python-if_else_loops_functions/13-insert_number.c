#include "lists.h"

/**
* insert_node - Inserts a node in a linked list
* head: pointer to pointer to the head of the list
* number: The number to be inserted or as a node
* Return: The address of the node, otherwise  NULL if failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *curr_node = *head;
	listint_t *prev_node = NULL;

	if (!new_node)
		return (NULL);
	
	new_node->n = number;
	new_node->next = NULL;

	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}

	while (curr_node && number > curr_node->n)
	{
		prev_node = curr_node;
		curr_node = curr_node->next;
	}

	if (!prev_node)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev_node->next = new_node;
		new_node->next = curr_node;
	}
	
	return (new_node);
}
