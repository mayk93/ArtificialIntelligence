#include<stdlib.h>
#include<stdio.h>

int map(char toMap)
{
    if(((int)toMap >= 33)&&((int)toMap <= 126))
    {
        return ((int)toMap-33);
    }
    return -1;
}

int check(int frequencyVector[], char toCheck)
{
    int index = map(toCheck);
    if(frequencyVector[index] > 0)
    {
        return 0;
    }
    frequencyVector[index]++;
    return 1;
}

void initialize(int toInitialize[], int size,int with)
{
    int i = 0;
    for(i = 0; i< size; i++)
    {
        toInitialize[i] = with;
    }
}

void fsm(char* toCheck)
{
    int size = 95, result = 0, finalResult = 1;
    int frequencyVector[size];
    char toBeChecked = *toCheck;
    
    initialize(frequencyVector,size,0);
    
    while((toCheck!=NULL&&toCheck[0]!='\0')&&(map(toBeChecked))&&finalResult)
    {
        result = check(frequencyVector,toBeChecked);
        
        /*
        printf("To Be Checked: %c\n",toBeChecked);
        printf("Map of %c: %d\n",toBeChecked,map(toBeChecked));
        printf("Result: %d\n",result);
        printf("FV[%d] = %d\n",map(toBeChecked),frequencyVector[map(toBeChecked)]);
        */
        
        switch(result)
        {
            case 0:
            {
                finalResult = 0;
                printf("Not Unique.\n");
                break;
            }
            case 1:
            {
                break;
            }
            default:
            {
                finalResult = -1;
                exit(finalResult);
            }
        }
        toCheck++;
        toBeChecked = *toCheck;
    }
    
    if(finalResult == 1)
    {
        printf("Unique.\n");
    }    
    return;    
}

void argumentNumberMessage(int argc)
{
    switch(argc)
    {
        case 0:
        {
            printf("Number of arguments: %d. Insufficient arguments.\n",argc);
            exit(1);
        }
        case 1:
        {
            printf("Number of arguments: %d. Insufficient arguments.\n",argc);
            exit(1);
        }
        case 2:
        {
            printf("String Checker.\n");
            return;
        }
        default:
        {
            printf("Number of arguments: %d. Excess arguments.\n",argc);
            exit(1);
        }
    }
    exit(-1);
}

int main(int argc, char *argv[])
{
    argumentNumberMessage(argc);
    fsm(argv[1]);
    return 0;
}
