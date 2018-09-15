#include<stdio.h>
#include<time.h>
#include<stdlib.h>
int cmpfunc(const void * a, const void * b)
{
	return (*(int*)a - *(int*)b);
}
int distributeCandies(int* candies, int candiesSize) {
	qsort(candies, candiesSize, sizeof(int), cmpfunc);
	int sum = 0;
	int i = 0;
	for (; i < candiesSize - 1; i++)
		if (candies[i] != candies[i + 1])
			sum++;
}
int main(void) {


}