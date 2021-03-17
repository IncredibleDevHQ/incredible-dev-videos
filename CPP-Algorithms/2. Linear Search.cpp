#include<iostream>
using namespace std;
int main() {
    int n, key, i;
    cin >> n;
    int a[1000];
    for(int i=0; i<n; i++) {
        cin >> a[i];
    }
    cout << "Enter the element you want to search:";
    cin >> key;
    // Linear Search Algorithm
    for( i=0; i<= n-1; i++){
        if(a[i] == key) {
            cout << key << " found at index " << i;
            break;
        }
    }
    if(i==n) {
        cout<< key << " is not present " << endl;
    }

    return 0;
}