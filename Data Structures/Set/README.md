# Set
A set is a popular data structure used for storing a list of elements
that are unique. A set doesn't have any particular ordering so the order
you input elements and fetch them could be different. 

## Basic Structuring 
Sets can be implemented in different ways depending on what speed and
capacity you need. The most popular implementation is creating a set 
with just a list. List's are not the fastest implementation of sets
but it's the least amount of code involved. 

Other popular set implementations are trees and hash maps. They both
will have lightning add, has, and delete speeds but you will need to 
have the other data structures created to implement them. 

## Add
The most basic function for sets is add. It will take one parameter and
all it will do is check if the element isn't already in the set, and if 
it's not then the function will add the element to the set. We normally 
dont return anything back this method.

## Has
We need to check what is in our set and we use has to do that. It's just
as simple as set and all we need to do is just return back if the 
element is in our data structure. 

## Delete
This is the inverse of the add function. We want to check if the set
has a certain value and if it does we delete it. We want to return a 
boolean of if the element was deleted from the set. 

## Union
Sets are popular to do calculations based on what's inside them. Union 
is basically just combining two sets together and returning a brand new
set. 

For example if you have a set that has [1, 2] and a set that has [2, 3]
a union of the two sets will return [1, 2, 3]. 

Getting a union is quite simple, all you need to do is clone the first 
set then call the add function on all the elements in the second set.

## Intersection
While union will return all the data from two sets, intersection will
just return the elements that overlap. 

Simple just look through the data in the first set and check if the 
second set has the current element, if it does add it to a return set
then return that set once all the elements in the first set has been
looked at. 

If you use a HashMap to implement this you can get it down to O(n) while
a list will get you up to O(n^2)

## Difference
Difference is what it sounds like, calling it on a function will return 
the difference between two sets. 

It's very similar to intersection but instead of adding the element to a
return set if both sets have the element. You add the element to the 
return set if set b doesn't have (or has) it. 

You will get the same speed from the intersection function.

## Subset
This function will return if all the elements in the current set are in 
a separate set. All you need to do is loop through all the elements
in the current set and check if the target set has the current element.

Speed will be O(n). 

## Iterator 
We want this set to be iterable. So if you are in a language that you 
can make a class iterable this would be pretty smart. Check the code to 
see a python implementation.

# When to use Sets
Sets are very helpful in many ways. They are extremely helpful in 
machine learning and math based algorithms because of the union, 
intersection, difference, and subset functions. But they are also very
helpful in your day to day application. 

It's good to use sets whenever you want to store elements that are 
unique and the ordering doesn't matter. They will typically be faster
then lists so using them instead of lists in the situation stated is
normally more efficient. 

Some of the implementations of set's I've used today are:
- Storing member ids that I was to find in a database from all orders
from a certain restaurant. 
- Storing ids that will never overlap and don't need to retain order.