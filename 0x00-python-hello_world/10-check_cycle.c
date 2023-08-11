/**
* check_cycle - Checks if a cycle exists in a linked list
* list: Pointer to the list
* Return: 1 if cycle exists, otherwise 0
*/

#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while(fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1); /* Cycle exist */
	}
	return (0); /* Cycle not exist */
}
