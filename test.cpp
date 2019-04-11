#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int a[1000+100];
int b[1000+100];

int main() {
    int n, h, res = 0; 
    scanf("%d%d", &n, &h);
    for (int i = 0; i<n; i++)   scanf("%d", &a[i]);
    for (int i = 0; i<n; i++) {
        int flag = 0, num = h;
        memset(b, 0, sizeof(b));
        for (int j = 0; j<=i; j++)  b[j] = a[j];
        sort(b, b+i+1);
        for (int j = i; j>=0; j--) {
            if (num >= b[j]) {
                num -= b[j];
                j --;
            }
            else {
                flag = 1;
                break;
            }
        }
        if (flag == 0)  res = i+1;  
    }
    printf("%d\n", res);
    return 0;
}