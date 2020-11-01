#include <iostream>
using namespace std;

int main()
{
    int tt;
    cin >> tt;

    int a;
    int b;
    for(int i=0; i<tt; i++)
    {
        cin >> a >> b;
        cout << "Case #" << i+1 << ": " << a << " + " << b << " = " << a+b << endl;
    }
}