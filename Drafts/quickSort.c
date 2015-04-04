#include<stdlib.h>
#include<stdio.h>

void swap(long int *a, long int *b)
{
    long int temp = *a;
    *a = *b;
    *b = temp;
}

long int partition(long int toPartition[], long int startIndex, long int endIndex)
{
    long int pivot = toPartition[endIndex];
    long int i = startIndex - 1;
    long int j = 0;
    for(j = startIndex; j < endIndex; j++)
    {
        if(toPartition[j] <= pivot)
        {
            i++;
            swap(&toPartition[i],&toPartition[j]);
        }  
    }
    swap(&toPartition[i+1],&toPartition[endIndex]);
    return i+1;
}

void quickSort(long int toSort[], long int startIndex, long int endIndex)
{
    if(startIndex < endIndex)
    {
        long int pivot = partition(toSort,startIndex,endIndex);
        quickSort(toSort,startIndex,pivot-1);
        quickSort(toSort,pivot+1,endIndex);
    }
}

void displayArray(long int toDisplay[],long int size)
{
    long int i = 0;
    printf("[");
    for(i = 0; i<size; i++)
    {
        if(i != size-1)
        {
            printf("%ld, ",toDisplay[i]);
        }
        else
        {
            printf("%ld",toDisplay[i]);
        }
    }
    printf("]\n");
}

int main(int argc, char* argv[])
{
    if(argc < 2)
    {
        printf("Insuficient arguments.\n");
        return 1;
    }
    else
    {
        char toCompare = *argv[1];
        if((argc == 2)&&(toCompare == 'h'))
        {
            printf("A proper input is of the form: ./qs size a0 a1 a2 ... a[size-1].\n");
            return 0;
        }
        else
        {
            char *endPointer;
            long int size;
            size = strtol(argv[1],&endPointer,10);
            
            printf("Size: %ld\n",size);
            
            long int toSort[size];
            long int i = 0;
            for(i = 2; i < size+2; i++)
            {
                printf("Str: %s\n",argv[i]);
                long int x = strtol(argv[i],&endPointer,10);
                toSort[i-2] = x;
                printf("toSort[%ld]: %ld\n",i-2,toSort[i]);
            }
            
            displayArray(toSort,size);
            quickSort(toSort,0,9);
            displayArray(toSort,size);
        }
    }
    return 0;
}
