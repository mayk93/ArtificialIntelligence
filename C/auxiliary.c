#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h> 

int isInteger(char *toCheck)
{
    while(toCheck && *toCheck != '\0')
    {
        if(!isdigit(*toCheck))
        {
            return 0;
        }

        toCheck++;
    }
    return 1;
}

int toInteger(char *toConvert)
{
    long int toReturn;
    char * pEnd;
    toReturn = strtol(toConvert,&pEnd,10);
    
    return (int)toReturn;
}
