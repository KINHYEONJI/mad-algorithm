#include <iostream>
#include <string>
 
using namespace std;
 
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
	int N;
	cin >> N;
	
	string ptn;
	cin >> ptn;
	
	int pos = ptn.find('*');
	string first = ptn.substr(0, pos);
	string last = ptn.substr(pos+1, ptn.length());
	
	for(int i = 0; i < N; i++){
		string input;
		cin >> input;
		
		if(input.length() < first.length() + last.length()){
			cout << "NE" << "\n";
			continue;
		}
		
		string compfirst = input.substr(0, first.length());
		string complast = input.substr(input.length()-last.length(), input.length());
		
		if(compfirst == first && complast == last)
			cout << "DA" << "\n";
		else
			cout << "NE" << "\n";
	}	
}    