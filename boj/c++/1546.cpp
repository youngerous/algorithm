#include <iostream>
using namespace std;
#define MIN 0

int main()
{
    int nn;
    cin >> nn;

    double arr[nn];
    double max = MIN;
    for(int i=0; i<nn; i++)
    {
        cin >> arr[i];
        max = max < arr[i] ? arr[i] : max;
    }

    double ans = 0.0;
    for(int i=0; i<nn; i++)
    {
        ans += (arr[i] / max * 100) / nn;
    }
    /*
     * fixed가 없는 경우: 정수부 + 소수부 기준으로 반올림
     * fixed가 있는 경우: 소수부만을 기준으로 반올림
     */
    cout << fixed;
    cout.precision(2);
    cout << ans;
}