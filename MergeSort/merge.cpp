#include "merge.h"

int is_all_num(char *av[])
{
    int i = 1;
    int j = 0;

    while (av[i])
    {
        while (av[i][j])
        {
            if (av[i][j] >= 48 && av[i][j] <= 57)
                j++;
            else
                return (-1);
        }
        i++;
    }
    return (1);
}

void f_error(string msg)
{
    cout << msg << endl;
    exit(0);
}

int *convert_to_array(char *av[])
{
    int i = 1;
    while (av[i])
        i++;
    int arr[i-1];
    i = 1;
    while (av[i])
    {
        arr[i-1] = atoi(av[i]);
        i++;
    }
    return (arr);
}

int len_of_arr(int arr[])
{
    int i = 0;

    while (arr[i])
        i++;
    return (i);
}

void merge(int arr[], int p, int q, int r)
{

    // Create L ← A[p..q] and M ← A[q+1..r]
    int n1 = q - p + 1;
    int n2 = r - q;

    int L[n1], M[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[p + i];
    for (int j = 0; j < n2; j++)
        M[j] = arr[q + 1 + j];

    // Maintain current index of sub-arrays and main array
    int i, j, k;
    i = 0;
    j = 0;
    k = p;

    // Until we reach either end of either L or M, pick larger among
    // elements L and M and place them in the correct position at A[p..r]
    while (i < n1 && j < n2) {
        if (L[i] <= M[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = M[j];
            j++;
        }
        k++;
    }

    // When we run out of elements in either L or M,
    // pick up the remaining elements and put in A[p..r]
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = M[j];
        j++;
        k++;
    }
}

int main(int ac, char *av[])
{
    if (ac >= 1)
    {
        if (is_all_num(av) == -1)
            f_error("Wrong type for input!");
        int *numbers = convert_to_array(av);
    }
    else
    {

    }
}