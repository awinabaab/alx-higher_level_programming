#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head node of the singly linked list
 *
 * Return: 0 if it is not palidrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr = *head;
	listint_t *slow_ptr = *head;
	listint_t *head_node = *head;
	listint_t *mid_ptr = NULL;
	listint_t *reverse_head = NULL;
	listint_t *reverse_head_cpy = NULL;

	if (!*head)
		return (1);

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		if (fast_ptr == NULL)
			break;
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}

	mid_ptr = slow_ptr;
	reverse_head = reverse_list(&mid_ptr);
	reverse_head_cpy = reverse_head;

	while (reverse_head->next && head_node->next)
	{
		if (reverse_head->n != head_node->n)
		{
			reverse_head = reverse_list(&reverse_head_cpy);
			return (0);
		}
		reverse_head = reverse_head->next;
		head_node = head_node->next;
	}
	reverse_head = reverse_list(&reverse_head_cpy);
	return (1);
}

/**
 * reverse_list - Reverses a singly linked list
 * @head: Singly linked list to reverse
 *
 * Return: Pointer to the head node of the reversed list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *head_node = *head;
	listint_t *next_node = NULL;
	listint_t *current_node = NULL;

	while (head_node)
	{
		next_node = head_node->next;
		head_node->next = current_node;
		current_node = head_node;
		head_node = next_node;
	}
	head_node = current_node;
	
	return (head_node);
}
