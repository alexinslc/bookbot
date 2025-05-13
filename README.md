# BookBot

BookBot is a text analysis tool that helps you analyze text files by providing word count and character frequency statistics. It's particularly useful for analyzing books and other text documents.

## Features

- Word count analysis
- Character frequency analysis (shows how many times each letter appears)
- Sorted output of character frequencies

## Requirements

- Python 3.x

## Usage

Run the program from the command line by providing a path to a text file:

```bash
python3 main.py <path_to_book>
```

## Example

To analyze Moby Dick:

```bash
python3 main.py books/mobydick.txt
```

Example output:
```
============ BOOKBOT ============
Analyzing book found at books/mobydick.txt...
----------- Word Count ----------
Found 215830 total words
--------- Character Count --------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...
============= END ===============
```

## Sample Books

The project includes several sample books in the `books` directory:
- Moby Dick
- Adventures of Huckleberry Finn
- Pride and Prejudice
- Frankenstein
- Dracula

You can analyze any of these books or provide your own text file for analysis.