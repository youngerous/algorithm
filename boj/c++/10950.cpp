#include <iostream>
using namespace std;

int main()
{
    int cases;
    cin >> cases;

    int a, b;
    for(int i=0; i<cases; i++)
    {
        cin >> a >> b;
        cout << a+b << '\n';
    }
}