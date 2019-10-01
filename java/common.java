/*
I'm more famialiar with Python, so this will be a mapping 
from use frequnently used Python snippets to Java.
*/


// print()
System.out.print()
System.out.println()


// **************
// string manipulation
// **************

// string length
s.length // len(s)

// subtring 
String s = "coding in java.";
s.substring(1, 5); // s[1:5]

// s[idx]
s.charAt(idx);

// split
String[] tokens = s.split(' ');

// join
// " ".join(['1', '2', '3'])
List<String> tokens = Arrays.asList("foo", "bar", "baz");;
String s = String.join(' ', tokens);

// .startswith()
s.startsWith("cod");

// isNumeric()

// **************
// sorting
// **************

Arrays.sort() // .sort() / sorted()


// **************
// collections
// **************

// primitive array
int[]
String[]

// tuple
// List   ->  List, ArrayList, LinkedList
// dict   ->  HashMap<> TreeMap<>
// set    ->  HashSet<> TreeSet<>
// collections.deque -> Queue<> 
// heapq

// len(collection) -> <Collection>.size()
// in  ->  contains() / containsKey()
// List .add() .remove() .get()
// Map .put() .getOrDefault()
// Queue .offer() .poll()
// Set .addAll() retainAll() .removeAll()

for (int i : numbers) {
}

// python: for k,v in dict.items():
for (Map.Entry<String,String> entry : myMap.entrySet()) {
    entry.key
    entry.value
}

// set union, intersection, difference
A.addAll(B)
A.retainAll(B)
A.difference(B)


List<>
ArrayList<>
