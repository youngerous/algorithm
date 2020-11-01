#include <iostream>
using namespace std;
#define TOTAL 8

int main()
{
    int status = -1; // ascending(0), descending(1), mixed(2)
    int newStatus = -1;
    int arr[8];
    for(int i=0; i<TOTAL; i++)
        cin >> arr[i];

    status = arr[0] > arr[1] ? 1 : 0; // 초기 상태 설정

    for(int i=1; i<TOTAL-1; i++)
    {
        newStatus = arr[i] > arr[i+1] ? 1 : 0;
        if(status != newStatus)
            break;
    }

    if(status != newStatus)
    {
        cout << "mixed";
    }else
    {
        if(status == 0)
        {
            cout << "ascending";
        }else
        {
            cout << "descending";
        }
    }


}