# Queue
A queue is a structure popularly know for the way you access its data
which is first in, first out.

Queues are usually taught at the same time as stacks. So go check out
my [stack article](../Stack).

## Basic Structuring
Queues are structured the same way that
[Linked Lists](../Linked%20Lists) are structured. We have a node that
has a next and data variable, then inside our Queue we have a head and
tail for adding and removing elements. The head is the first element
added while the tail is the last element added. In a real world example
the head would be the first person in a line, and the tail would be the
last person in line.

## Enqueue
If we enqueue an element, we are adding it to the back of the line.
Enqueue is the same as append an element to a Linked List. We first
create a new node. If our Queue is empty then we set the head and tail
to our new node. If it's not empty, we set our current tail reference
our new node, and set our new node to the tail of our Queue.

## Dequeue
If we dequeue an element, we are removing and getting the first person
in line. We return the current head of our Queue, then set the head to
the old heads next value.

Be sure that if our queue only has one element left, to self the tail to
None.

## Peak
If we want to peak and see the first person in line, we will just return
the head of our Queue.

## Deque
A deque is where you can enqueue and dequeue elements from either the
head and tail.

## Circular Queue
Our heads next value is set to the tail of our queue. Quite simple
actually.

## Popular Usage
A  popular usage for queues is with arithmetic expression evaluation.