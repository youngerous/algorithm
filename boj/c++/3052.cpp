#include <iostream>
using namespace std;
#define LEN 42
#define INPUT 10

int main()
{
    int arr[LEN] = {0, };
    int val;
    for(int i=0; i<INPUT; i++)
    {
        cin >> val;
        arr[val % 42] = 1;
    }

    int count = 0;
    for(int i=0; i<LEN; i++)
    {
        count += arr[i];
    }
    cout << count;
}