//library
#include<iostream>

using namespace std;
//write the main function
int main()
{
    // declaring variable
    double count = 0;
    //using for loop
    for(int a=1;((double) 1/a) > 0.001;a++)
    {
        
        count +=((double)1/a)  ; 
       
    }
    cout << count << endl;

}
