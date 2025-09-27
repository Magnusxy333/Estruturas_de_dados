#include <iostream>
using namespace std;

int main() 
{
    int x;
  cout << "Digite seu valo de compra: " << endl; 
  cin >> x;
  
  if(x < 100) {
    cout << "Sua compra é sem desconto!!!" << endl;
  } else {
    cout << "Sua compra é com desconto!!!" << endl;
  }
  
  return 0;
}