#include <iostream>
using namespace std;

class search
{

  public:
    int LIS(int key,int D,int A[10]);
    int LRS(int key,int D,int A[10]);

};

int search ::LIS(int key,int D,int A[10])
{ 
  for(int i=0;i<D;i++)
  { 
     if(A[i]==key)
     {return i;}
  }
return -1;
}

int search ::LRS(int key,int D,int A[10])
{ 
   if(D>0)
   { 
     if(A[D]==key)
     {return D;}
     
     else
     {return LRS(key,D-1,A);}
   }

   else
   {return -1;}
}

int main()
{
   int A[10] ={1,2,4,5,3,6,7,8,9,6};
   search s1;

   int j =s1.LIS(3,9,A);
   int i =s1.LRS(3,9,A);

   if(i!=-1)
   {cout<<"item found at position "<<i<<endl;}

   else
   {cout<<"item not found"<<endl;}

   if(j!=-1)
   {cout<<"item found at position "<<j<<endl;}

   else
   {cout<<"item not found"<<endl;}

return 0;}
