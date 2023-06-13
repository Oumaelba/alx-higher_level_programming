#include "lists.h"
/**
 * insert_node - Inserts a new node into a sorted linked list
 * @head: Pointer to a pointer to the head of the linked list
 * @number: Value to be inserted in the new node
 *
 * Return: Pointer to the newly inserted node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *inserted;
	listint_t *current;
	listint_t *previous;

	current = *head;

	inserted = malloc(sizeof(listint_t));
	if (inserted == NULL)
		return (NULL);

	inserted->n = number;

	while (current->n < number && current != NULL)
	{
		previous = current;
		current = current->next;
	}
	if (previous == NULL)
	{
		inserted->next = *head;
		*head = inserted;
	}
	else
	{
		previous->next = inserted;
		inserted->next = current;
	}

	return (inserted);

}
