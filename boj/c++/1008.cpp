#include <iostream>
using namespace std;

int main()
{
    double a, b;
    cin >> a >> b;
    cout.precision(15); // 정확도를 (유효숫자) 15자리까지 표시
    cout << a/b << endl;
}