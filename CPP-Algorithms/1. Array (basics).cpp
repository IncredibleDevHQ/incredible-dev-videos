#include<iostream>
using namespace std;
int main() {
    int a[3] = {1, 2, 3};
    // int a[10] = {1, 2, 3};
    int b[10];
    for(int i = 0; i < 10; i++) {
        cin >> b[i];
    }
    for(int i = 0; i < 10; i++) {
        cout << b[i] << ", ";
    }
    return 0;
}