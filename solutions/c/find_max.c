#include <stdio.h>

/* A function that finds the largest number in an array of numbers */

int find_largest(int arr[], int n) {
    int max = arr[0]; 
    
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i]; 
        }
    }
    
    return max;
}

int main() {
    int numbers[] = {5, 12, 8, 21, 16, 7}; 
    int size = sizeof(numbers) / sizeof(numbers[0]); 
    
    int largest = find_largest(numbers, size); 
    
    printf("The largest number is: %d\n", largest); 
    
    return 0;
}
