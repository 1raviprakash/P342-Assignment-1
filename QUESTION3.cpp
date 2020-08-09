//library
#include<iostream>

using namespace std;
//write the main function
int main()
{
    // declaring variable
    double count = 0;
    //using for loop
    for(int i=1;((double) 1/i) > 0.001;i++)
    {
        // cout << i ; 
        count +=((double)1/i)  ; 
        // cout << endl;
    }
    cout << count << endl;

}
