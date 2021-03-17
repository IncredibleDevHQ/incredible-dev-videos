#include<iostream>
#include<algorithm>

using namespace std;

// Define A Comparator function 
bool compare(int a, int b) { 
    return b > a; // to sort in increasing order
}
int main() {
    int a[] = { 1, 5, 3, 4, 2, 0 };
    int n = sizeof(a) / sizeof(a[0]);
    // sort an array using sort() function, more efficient
    sort(a, a+n);
    // [0, 1, 2, 3, 4, 5]
    sort(a, a+n, compare);
    // [0, 1, 2, 3, 4, 5]
    sort(a, a+n, greater<int>());
    // [5, 4, 3, 2, 1, 0]  
    for(int i = 0; i < n; i++) {
        cout << a[i] << ", ";
    }
    return 0;
}
