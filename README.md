# Finding-the-Size-Ez-

CompSci #2

What did I learned from this lesson?

By coding this simple program, it is now clear that when we append objects to a list, the more items we add, the more bytes that are used to store that list, which makes sense. However what's funny is this:

1 88
2 88
3 88
4 88
5 120
6 120
7 120
8 120
9 184

You can see here that the first 4 indexes store 88, and the next 4 store 120. This says to us that python automatically reserves some memory for a specific number of indexes. Instead of increasing the size of the list for each index, instead, python automatically reserves more memory, even though the items we are storing do not completely fit into it. This is interesting because it shows that python makes a compromise between allocating memeory for each index which is an inefficient and "tiring" process, and the alternative, reserving the whole computer's memory to store what may be just a couple of objects in a table.

Python has a made a compromise between inefficiency and slowness and taking up too much memory, so python resorts to reserving a set amount which allows the next few indexes to fit into it. \

Nice.
