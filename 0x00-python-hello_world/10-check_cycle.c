#include "lists.h"
/**
 * check_cycle - Checks if a linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 0 if no cycle is found, 1 if a cycle is found.
 */
int check_cycle(listint_t *list)
{
	listint_t *turtoise = list;
	listint_t *hare = list;

	if (!list)
		return (0);

	while (hare!= NULL && hare->next != NULL)
	{
		if (turtoise == hare)
			return (1);
		else if(turtoise != hare)
		{
			turtoise = list->next;
			hare = list->next->next;
		}
	}
	return (0);
}


