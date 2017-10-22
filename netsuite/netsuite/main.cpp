//
//  main.cpp
//  netsuite
//
//  Created by Petr Lefner on 18.01.15.
//  Copyright (c) 2015 Petr Lefner. All rights reserved.
//

#include <iostream>


int * removeDuplicates(int * pValues, int * pValuesEnd)
{
    // sanity check (invalid input values) or input array empty
    if (!pValues || !pValuesEnd)
        return NULL;
    int * pRet = pValues;
    for(int * pVal = pValues; pVal != pValuesEnd; )
    {
        // shift to first item of duplicit sequence
        while (pVal != pValuesEnd && *pVal != *(pVal + 1))
        {
            pVal++;
            pRet++;
        }
        if (pVal+1 == pValuesEnd)
            return pRet;    // last sequence of duplicit values
        int * pLastUnique = pVal;
        // shift to first different value, write it after the last known end
        while (*pVal == *pLastUnique && pVal != pValuesEnd)
            pVal++;
        if (pVal == pValuesEnd)
            return pRet;    // no other different value
        *pRet = *pVal;
    }
    return pRet;
}

//               1, 2, 2, 2, 3, 3, 4
// 1, 2, 3,

int main(int argc, const char * argv[]) {
    // insert code here...

//    int values[] = {1,1, 2,2, 2,3, 3,4};
//    int * pEnd = &values[7];
    int values[] = {2,2,2};
    int * pEnd = &values[2];
    int * last = removeDuplicates(values, pEnd);
    for (int * p = values; p != pEnd; p++)
        printf("%i ", *p);
    printf("\n");
    if (last)
    {
        for (int * p = last; p != last; p++)
            printf("%i ", *p);
        printf("length: %i", last - values);
    } else
        printf("last NULL");

    std::cout << "\nHello, World!\n";
    return 0;
}

