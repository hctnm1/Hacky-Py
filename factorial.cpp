#include<iostream>
using namespace std;
int main(){
   int i,fact=1,num;
   cout<<"Enter a number: ";
   cin>>num;
   for(i=1;i<=num;i++){
   	fact=fact*i;
   }	
   cout<<"The Factorial of "<<num<<" is "<<fact<<endl;
	return 0;
}
