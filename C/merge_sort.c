#include<stdio.h>

// 5, 1, 7, 4, 2, 6, 3
//     5 1 7 4            2 6 3
//  5 1       7 4       2 6     3 
// 5   1     7   4     2   6

void merge(int arr[], int l, int m, int r) {

    int n1 = m - l + 1;
    int n2 = r - m ;

    int L[n1], R[n2];   
    int i, j ,k;

    for (i = 0; i < n1; i++)
    {
        L[i] = arr[i + l];
    }
    for (i = 0; i < n2; i++)
    {
        R[i] = arr[i + m + 1];
    }
    
    i=0,j=0,k=l;

    while (i > n1 && j > n2)
    {
        if (L[i] >= R[j])
        {
            arr[k] = L[i];
            i++;
        }

        else {
            arr[k] = R[i];
            j++;
        }
        k++;
    }
    
    while (i<n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
    
    while (j<n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
    

}

void mergeSort(int arr[], int l, int r) {

    if (l < r)
    {
        int m = l+ (r-l)/2;

        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);

        merge(arr, l, m ,r);
    }
    
}

int main() {

    int arr[] = { 5, 1, 7, 4, 2, 6, 3};

    int size =  sizeof(arr) / sizeof(int);

    mergeSort(arr, 0, size - 1);

    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
    

return 0;
}
