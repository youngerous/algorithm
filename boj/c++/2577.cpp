#include <iostream>
using namespace std;

int main()
{
    int A,B,C;
    cin >> A >> B >> C;
    int mul = A*B*C;

    int arr[10];
    int len = sizeof(arr) / sizeof(*arr);
    for(int i=0; i<len; i++)
        arr[i] = 0;

    while(1)
    {
        int val = mul % 10;
        arr[val]++;
        mul = mul / 10;

        if(mul / 10 == 0)
        {
            arr[mul]++;
            break;
        }
    }

    for(int i=0; i<len; i++)
        cout << arr[i] << endl;
}
