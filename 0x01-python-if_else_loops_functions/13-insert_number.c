#include "lists.h"

/**
 * insert_node - insert an element into a sorted node
 * @head: pointer to the first node
 * @number: element to be inserted
 *
 * Return: on success, pointer to the new node. On failure, null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *new_node = NULL;
	listint_t *temp_node = NULL;

	if (!head)
		return (NULL);

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new_node->next = *head;
		return (*head = new_node);
	}
	else
	{
		while (current_node && (current_node->n) < number)
		{
			temp_node = current_node;
			current_node = current_node->next;
		}

		temp_node->next = new_node;
		new_node->next = current_node;
	}
	return (new_node);
}
