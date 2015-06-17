#include <stdio.h>
#include <math.h>

void metersToFeetAndInches(double meters, unsigned int *ftPtr, double *inPtr)
{

    double rawFeet = meters * 3.281;

    unsigned int feet = (unsigned int)floor(rawFeet);

    printf("Storing %u to the address %p\n", feet, ftPtr);
    *ftPtr = feet;

    double fractionalFoot = rawFeet - feet;
    double inches = fractionalFoot * 12.0;

    printf("Storing %.2f to the address %p\n", inches, inPtr);
    *inPtr = inches;
}


int main(int argc, const char * argv[])
{
    double meters = 3.0;
    unsigned int feet;
    double inches;

    metersToFeetAndInches(meters, &feet, &inches);
    printf("%.1f meters is equal to %d feet and %.1f inches.", meters, feet, inches);

    return 0;
}