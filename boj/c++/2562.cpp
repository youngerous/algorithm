#include <iostream>
using namespace std;
#define MAX 101
#define NUM 9

int main()
{
    int maxVal = -MAX;
    int maxIdx = -1;
    for(int i=0; i<NUM; i++)
    {
        int input;
        cin >> input;
        if(input > maxVal)
        {
            maxVal = input;
            maxIdx = i+1;
        }
    }
    cout << maxVal << endl;
    cout << maxIdx;
}