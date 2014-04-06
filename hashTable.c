#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include <limits.h>

//The name itemS stands for itemStructure, the structure of an item that will
//be placed in the table. It is a key-value pair, and can be chained
//to solve collisions.
struct itemS
{
    char *key;
    char *value;
    struct itemS *next; //This particular hash table solves collisions
                          //by chaining, that is, if two keys are mapped to
                          //the same slot, it will create a list, that must
                          //be iterated to found the correct value.
                          
    /*       ______      
    abc ---> |    | ***> |Slot 1| X
    def ***> |hash| ---> |Slot 2| Y, Z
    ghi ...> |fct | ===> |      |
    jkl '''> |    | '''> |Slot 3| A
    mno ===> |____| ...> |Slot 4| B
    
    Both "abc" and "mno" map to Slot 2 of the hash table, however, the
    value of "abc" is Y and the value of "mno" is Z.
    */                          
};

//We define a type itemT (T as in table) that has an itemS structure.
//These will be the table items.
typedef struct itemS itemT;

//Again, S stands for Structure.
struct hashtableS 
{
    int size;
    struct itemS **table;	
};
 
typedef struct hashtableS hashtableT;

//This function creates a Hash Table. Think of it as a constructor.
hashtableT *createHashTable( int size ) 
{
    //This is what we create.
    hashtableT *hashtable = NULL;
    //We use i for iterations.
    int i;
    //A 0 or negative size doesn't make sense. We test for bad size input. 
    if( size < 1 )
    {
        return NULL;
    }  
    //Allocate the table itself.
    //We check if malloc return a NULL pointer in order to ensure
    //the memory allocation was successful.
    if( ( hashtable = malloc( sizeof(hashtableT) ) ) == NULL ) 
    {
        return NULL;
    }
    //Allocate pointers to the head nodes.
    //In the table field of the hashtable structure, we make room for
    //size itemTs. If size were 7, there would be 7 itemTs.
    if( ( hashtable->table = malloc( sizeof(itemT *) * size ) ) == NULL )
    {
        return NULL;
    }
    //Initially, all table items are empty.
    for( i = 0; i < size; i++ ) 
    {
        hashtable->table[i] = NULL;
    }
     
    hashtable->size = size;
     
    return hashtable;	
}

//This is the core of a hash table. The hash Function.
//You give the table and a key. The function will map
//the key to a value that will be found in a table.
int hashFunction( hashtableT *hashtable, char *key ) 
{
    int hashval = 3079; //The number is from here: 
                        //http://planetmath.org/goodhashtableprimes
    int i = 0;
     
    //Convert our string to an integer
    //More string to int hash functions can be found here:
    //http://www.cse.yorku.ca/~oz/hash.html
    while( (hashval < ULONG_MAX) && (i < strlen( key )) ) 
    {
        hashval = hashval << 8;
        hashval = hashval + key[ i ];
        i++;
    }
    
    return hashval % hashtable->size;
}

int anotherHashFunction( hashtableT *hashtable, char *key )
{
    int hashval = 5381;
    int c;

    while (c = *key++)
    {
        hashval = ((hashval << 5) + hashval) + c;
    }
    
    return hashval % hashtable->size;
}

//Create a key-value pair.
itemT *createNewItem( char *key, char *value ) 
{
    itemT *newitem;
    //The new item will have a itemT size. 
    if( ( newitem = malloc( sizeof( itemT ) ) ) == NULL ) 
    {
        return NULL;
    }
    //We try to set the key field of the new item to be the inputed key.
    //Should the operation return null, it means it failed. 
    if( ( newitem->key = strdup( key ) ) == NULL ) 
    {
        return NULL;
    }
 
    if( ( newitem->value = strdup( value ) ) == NULL ) 
    {
        return NULL;
    }
    //At the moment, there are no other items linked to our item, so we set
    //next to NULL. 
    newitem->next = NULL;
     
    return newitem;
}

//Insert a key-value pair (item) into a hash table.
void insert( hashtableT *hashtable, char *key, char *value ) 
{
    int index = 0;
    //These will be used in collision solving.
    itemT *newitem = NULL;
    itemT *next = NULL;
    itemT *last = NULL;
    
    //Compute the index using the hash function. 
    index = hashFunction( hashtable, key );
    next = hashtable->table[ index ];
    
    //Now we check for collisions.
    //We iterate the items found at the index until we get to the end of 
    //the chain or get a key match, in which case we must update the value. 
    while( next != NULL && next->key != NULL && strcmp( key, next->key ) > 0 ) 
    {
        last = next;
        next = next->next;
    }
     
    //There's already an item with the same key. We replace the value.
    if( next != NULL && next->key != NULL && strcmp( key, next->key ) == 0 ) 
    {
        free( next->value );
        next->value = strdup( value );
    }
    //If we didn't get a key match, it means a new value must be mapped to the
    //key. So we do this. 
    else 
    {
        newitem = createNewItem( key, value );
     
        if( next == hashtable->table[ index ] ) 
        {
            newitem->next = next;
            hashtable->table[ index ] = newitem;
        } 
        else if ( next == NULL ) 
        {
            last->next = newitem;
        } 
        else 
        {
            newitem->next = next;
            last->next = newitem;
        }
    }
}

/* Retrieve a key-value pair from a hash table. */
char *search( hashtableT *hashtable, char *key ) 
{
    int index = 0;
    itemT *item;
     
    index = hashFunction( hashtable, key );
     
    //Step through the index, looking for our value.
    item = hashtable->table[ index ];
    while( item != NULL && item->key != NULL && strcmp( key, item->key ) > 0 ) 
    {
        item = item->next;
    }
     
    //Did we actually find anything?
    if( item == NULL || item->key == NULL || strcmp( key, item->key ) != 0 ) 
    {
        return NULL; 
    } 
    else 
    {
        return item->value;
    }
}

int main( int argc, char **argv ) 
{
    hashtableT *hashtable = createHashTable( 65536 );
    hashtableT *anotherHT = createHashTable( 389 );
     
    insert( hashtable, "abc", "X" );
    insert( hashtable, "def", "Y" );
    insert( hashtable, "ghi", "Z" );
    insert( hashtable, "jkl", "A" );
    insert( hashtable, "mno", "B" ); 
     
    printf( "%s\n", search( hashtable, "abc" ) );
    printf( "%s\n", search( hashtable, "def" ) );
    printf( "%s\n", search( hashtable, "ghi" ) );
    printf( "%s\n", search( hashtable, "jkl" ) );
    printf( "%s\n", search( hashtable, "mno" ) );
    
    insert( anotherHT, "xyz", "Q" );
    insert( anotherHT, "uvw", "W" );
    insert( anotherHT, "!2@41bt*^2cdvR", "Random" );
    
    printf( "%s\n", search( anotherHT, "xyz" ) );
    printf( "%s\n", search( anotherHT, "uvw" ) );
    printf( "%s\n", search( anotherHT, "!2@41bt*^2cdvR" ) );
        
    return 0;
}
