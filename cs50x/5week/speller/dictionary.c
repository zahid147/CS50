// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Default dictionary
#define DICTIONARY "dictionaries/large"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Create a variable to keep track of word count
int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hashIndex = hash(word);

    // Create a pointing variable
    node *point = table[hashIndex];

    // Loop through the linked list untill it ends
    while (point != NULL)
    {
        // Check if the word are same or move the point forward
        if (strcasecmp(point->word, word) == 0)
        {
            return true;
        }
        point = point->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open file to read
    FILE *Dict = fopen(DICTIONARY, "r");

    // Check the file
    if (Dict == NULL)
    {
        return false;
    }

    // Create a char array for fscanf
    char str[LENGTH + 1];

    // Check thee end of file in loop
    while (fscanf(Dict, "%s", str) != EOF)
    {
        // Create a node for word
        node *temp = malloc(sizeof(node));

        // Check if the return value is NULL
        if (temp == NULL)
        {
            return false;
        }

        // Copy word into node
        strcpy(temp->word, str);

        // Use hash funcion
        int hashIndex = hash(str);

        // Check if the head points to NULL
        if (table[hashIndex] == NULL)
        {
            // Point temp to NULL
            temp->next = NULL;
        }
        else
        {
            // Point temp to the first node
            temp->next = table[hashIndex];
        }

        // Point the header to temp
        table[hashIndex] = temp;

        // Increment the count
        count++;

        // Free the temp
        free(temp);
    }

    // Close the file and free the temporary node
    fclose(Dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Return the word count
    return count;
}

// Free nodes recursively
void freeNode(node *n)
{
    if (n->next != NULL)
    {
        freeNode(n->next);
    }
    free(n);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    //
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            // Free the node
            freeNode(table[i]);
        }
    }
    return false;
}
