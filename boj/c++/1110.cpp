#include <iostream>
using namespace std;

int main() 
{
    int num;
    cin >> num;
    
    if(num < 10)
    {
        num *= 10;
    }
    
    int cycle = 0;
    int after = num;
    int ten, one, sum;
    
    while(1)
    {
        ten = after / 10;
        one = after % 10;
        sum = ten + one;
        
        after = (one * 10) +  (sum % 10);
        
        cycle++;
        
        if(num == after)
        {
            break;
        }
    }
    
    cout << cycle;
}