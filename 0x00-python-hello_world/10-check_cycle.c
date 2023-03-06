#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle
* @list: points to a struct
*
* Return: 0 if no cycle, 1 if there is cycle
*/
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *swift = list;
if(!list)
return (0);
while(swift && swift->next)
{
slow = slow->next;
swift = swift->next->next;
if(swift == slow)
return (1);
}
return (0);
}
