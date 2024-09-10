#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a number into a sorted linked list
 * @head: pointer to head node of linked list
 * @number: number to be inserted
 *
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *head_node = *head;
	listint_t *new_node = NULL;

	if (!head || !*head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;

	while (head_node != NULL && head_node->next != NULL)
	{
		if (head_node->n <= number &&
				head_node->next->n >= number)
		{
			new_node->next = head_node->next;
			head_node->next = new_node;
			return (new_node);
		}
		head_node = head_node->next;
	}

	return (new_node);
}
