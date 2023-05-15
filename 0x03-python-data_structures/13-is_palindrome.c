#include"lists.h"

/**
  * listint_len - Counts the number of elements in a linked list
  * @head: linked list to count
  *
  * Return: Number of elements in the linked list
  */
size_t listint_len(const listint_t *head)
{
	size_t length = 0;

	while (head != NULL)
	{
		++length;
		head = head->next;
	}
	return (length);
}


/**
  * get_nodeint_at_index - Gets a node from a linked list
  * @head: Head of the linked list
  * @index: Index to find in the linked list
  *
  * Return: The specific node
 */

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int iter_times = 0;

	while (current != NULL)
	{
		if (iter_times == index)
			return (current);
		current = current->next;
		++iter_times;
	}
	return (NULL);
}

/**
 * is_palindrome - checks if linked list is palindrome
 *
 * @head: head of linked list
 *
 * Return: 1 if palindrome and 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *start = NULL, *end = NULL;
	unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	start = *head;
	len = listint_len(start);
	len_cyc = len * 2;
	len_list = len_cyc - 2;
	end = *head;
	for (; i < len_cyc; i = i + 2)
	{
		if (start[i].n != end[len_list].n)
			return (0);
		len_list = len_list - 2;
	}
	return (1);
}
