# Stack
A queue is a structure popularly know for the way you access its data
which is last in first out (LIFO). In theory you can only access
information from the top of the stack.

Stacks are usually taught at the same time as stacks. So go check out
my [queue article](../Queue).

## Basic Structuring
Stacks are usually built the same way that Linked Lists are. We have a
node that has a pointer to the next element in the structure. Then Inside the
Stack we want to have a head variable which will be the top element on
our stack.

## Push
The add an element to a stack, you are going to push it to the top of
the stack. We would do this by creating a node, assigning it's next
value to the current stack head, then setting our node to the new head.

## Pop Pop Pop Georgy
To remove an element from the stack, we pop it off the top of our stack.
All we need to do is set the head of our stack to be the current heads
next value. But we don't want to totally get rid of the old head, we
actually want to return back the data it holds.

## Peak
If we want to check top element on the stack, we peak it. Just return
back the data within the head node.

## Popular Usage
Stacks are popularly used for things like undo functions and back
tracking. Also some people use it for reversing a word.

