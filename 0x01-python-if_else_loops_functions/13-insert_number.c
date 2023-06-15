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
	listint_t *new_node;
	listint_t *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next && number > current->next->n)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
