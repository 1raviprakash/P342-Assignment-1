//library
#include<iostream>

using namespace std;
//write the main function
int main()
{
    // declaring variable
    int result= 0;
    int n = 0;
    cout<<"Enter the number till which you want to add";
    cin>>n;
    for (int a=0;a<=n;a++)
    {
        result=result+ a;

    }
    cout << result << endl;
}
