#include <iostream>
using namespace std;
const int MAX = 1000000;

int main()
{
    int nn;
    cin >> nn;
    
    int min = MAX, max = -MAX;
    int input;
    
    for(int i=0; i<nn; i++)
    {
        cin >> input;
        max = input > max ? input : max;
        min = input < min ? input : min;
    }
    cout << min << ' ' << max;
    
}