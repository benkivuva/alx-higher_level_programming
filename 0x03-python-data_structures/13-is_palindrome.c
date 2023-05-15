#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

int list_len(listint_t *);

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: address of pointer to the head of the list
 *
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	int list_length = list_len(*head);
	int array[4096];
	int half_length = list_length / 2;
	int i;
	listint_t *current_node = NULL;

	/* Check if head pointer is NULL */
	if (!head)
		exit(-1);

	/* If the list has more than one element */
	if (list_length > 1)
	{
		/* Store the first half of the list in an array */
		for (i = 0, current_node = *head;
		     i < half_length;
		     i++, current_node = current_node->next)
		{
			array[i] = current_node->n;
		}

		/* If the list has odd length, move to the next node */
		if (list_length % 2)
			current_node = current_node->next;

		/* Compare the second half of the list with the reversed 1st h*/
		for (i = 0; i < half_length; i++, current_node = current_node->next)
		{
			if (array[half_length - i - 1] != current_node->n)
				return (0); /* Not a palindrome */
		}
	}

	return (1); /* Palindrome */
}

/**
 * list_len - count the number of nodes in a linked list
 * @head: pointer to the head of the list
 *
 * Return: number of nodes
 */
int list_len(listint_t *head)
{
	if (head)
		return (1 + list_len(head->next));
	return (0);
}
