#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head node of the singly linked list
 *
 * Return: 0 if it is not palidrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *head_node = *head;
	listint_t *duplicate_head = NULL;
	listint_t *reverse_head = NULL;
	listint_t *reverse_node = NULL;

	if (!*head)
		return (1);
	duplicate_head = duplicate_list(&head_node);
	reverse_head = reverse_list(&duplicate_head);

	reverse_node = reverse_head;

	while (reverse_node->next && head_node->next)
	{
		if (reverse_node->n != head_node->n)
		{
			free_listint(reverse_head);
			return (0);
		}
		reverse_node = reverse_node->next;
		head_node = head_node->next;
	}

	free_listint(reverse_head);
	return (1);
}

/**
 * duplicate_list - Duplicates a singly linked list
 * @head: Pointer to the head node of the singly linked list
 *
 * Return: Pointer to head of duplicate @head
 */

listint_t *duplicate_list(listint_t **head)
{
	listint_t *head_node = *head;
	listint_t *duplicate = NULL;

	if (!*head)
		return (NULL);

	while (head_node != NULL)
	{
		add_nodeint_end(&duplicate, head_node->n);
		head_node = head_node->next;
	}

	return (duplicate);
}

/**
 * reverse_list - Reverses a singly linked list
 * @head: Pointer to the head node of the singly linked list
 *
 * Return: Pointer to head node of reversed list else NULL
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *head_node = *head;
	listint_t *current_node = NULL;
	listint_t *next_node = NULL;

	if (!*head)
		return (NULL);

	while (head_node != NULL)
	{
		next_node = head_node->next;
		head_node->next = current_node;
		current_node = head_node;
		head_node = next_node;
	}
	head_node = current_node;

	return (head_node);
}
