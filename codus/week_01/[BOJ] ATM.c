#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

void select(int arr[], int n);
void swap(int* a1, int* a2);

int main() {
	int n = 0;
	int arr[1000];
	int sum = 0;
	int result = 0;

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}

	select(arr, n);

	for (int i = 0; i < n; i++)
	{
		sum = 0;
		for (int j = 0; j <= i; j++)
		{
			sum = sum + arr[j];
		}
		result = result + sum;
	}
	printf("%d", result);
}

void select(int arr[], int n)
{
	int min = 0;
	for (int i = 0; i < n - 1; i++)
	{
		min = i;
		for (int j = i+1; j < n; j++)
		{
			if (arr[j] < arr[min])
			{
				min = j;
			}
		}
		swap(&arr[min], &arr[i]);
	}
}

void swap(int *a1, int *a2)
{
	int tmp = *a1;
	*a1 = *a2;
	*a2 = tmp;
}