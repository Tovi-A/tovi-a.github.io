#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

void test() {
    static int count = 0;
    count ++ ;
    cout << count << endl;
}

int main() {
    test();
    test();
    test();
    test();
    return 0;
}