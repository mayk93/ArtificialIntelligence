#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

typedef struct heapType 
{
    int (* parent)();
    int (* left)();
    int (* right)();
    void (* calculeateHeapSize)();
    void (* maxHeapify)();    
    void (* buildHeap)();
    void (* printfHeap)();
    void (* displayAsTree)();    
     
    int arraySize;
    int heapSize;
    int *array;
} Heap;

int parent(int index)
{
    return floor(index/2);
}

int left(int index)
{
    return index << 1;
}

int right(int index)
{
    return (index << 1) + 1;
}

void calculeateHeapSize(Heap *h)
{
    //h->heapSize = h->arraySize/sizeof(int);
    h->heapSize = h->arraySize;  
}

void maxHeapify(Heap *h, int index)
{
    int l = h->left(index);
    int r = h->right(index);
    
    int largest;
    
    if( (l <= h->heapSize) && (h->array[l] > h->array[index]) )
    {
        largest = l;
    }
    else
    {
        largest = index;
    }
    
    if( (r <= h->heapSize) && (h->array[l] > h->array[largest]) )
    {
        largest = r;
    }
    
    if( largest != index )
    {
        int temp = h->array[index];
        h->array[index] = h->array[largest];
        h->array[largest] = temp;
        maxHeapify(h,largest);
    }
}

void buildHeap(Heap *h)
{
    h->heapSize = h->arraySize;
    int i = 0;
    for(i = (floor(h->heapSize/2)); i>= 1; i--)
    {
        maxHeapify(h,i);
    }
}

void displayAsTree(Heap *h)
{
    int i = 0;
    for(i = 1; i <= h->arraySize; i++)
    {
        printf("Current Node: %d\n",h->array[i]);
        if(left(i) <= h->arraySize)
        {
            printf("Left Child: %d\n",h->array[left(i)]);
        }
        if(right(i) <= h->arraySize)
        {
            printf("Right Child: %d\n",h->array[right(i)]);
        }
        printf("\n---\n");
    }
}

void printfHeap(Heap *h)
{
    int i;
    for(i = 1; i <= h->arraySize; i++)
    {
        if(i != h->arraySize -1)
        {
            printf("%d, ",h->array[i]);
        }
        else
        {
            printf("%d.\n",h->array[i]);
        }
    }
}

Heap *heapConstructor(int size)
{
    Heap *newHeap=(Heap*)malloc(sizeof(Heap));
    
    newHeap->array=(int *)malloc(sizeof(int)*size);
    
    newHeap->arraySize = size;
    newHeap->heapSize = size;
    
    newHeap->parent = parent;
    newHeap->left = left;
    newHeap->right = right;
    newHeap->calculeateHeapSize = calculeateHeapSize;
    newHeap->maxHeapify = maxHeapify;
    newHeap->printfHeap = printfHeap;
    newHeap->buildHeap = buildHeap;
    newHeap->displayAsTree = displayAsTree;
    
    return newHeap;
}

void arguments(int argc)
{
    if(argc <= 0)
    {
        printf("Negative or 0 arguments.\n");
        exit(1);
    }
    if(argc == 1)
    {
        printf("Empty heap.\n");
        exit(1);
    }
}

Heap initialize(int argc, char* argv[])
{
    Heap *h = heapConstructor(argc);
    int inputVectorIndex = 0;

    for(inputVectorIndex = 1; inputVectorIndex < argc; inputVectorIndex++)
    {
        if(isInteger(argv[inputVectorIndex]))
        {
            h->array[inputVectorIndex] = toInteger(argv[inputVectorIndex]);
        }
        else
        {
            printf("Invalid Input.\n");
            exit(1);
        }
    }
    return *h;
}

int main(int argc, char* argv[])
{
    arguments(argc);
    Heap h = initialize(argc, argv);
    h.printfHeap(&h);
    h.displayAsTree(&h);
    h.buildHeap(&h);
    //h.maxHeapify(&h,1);
    //h.printfHeap(&h);
    h.displayAsTree(&h);
    
    return 0;
}
