#include "lists.h"

/**
 * check_cycle - check if list have cycle
 *
 * @list: linked list
 * Return: 0 if no cycle, 1 if is cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
