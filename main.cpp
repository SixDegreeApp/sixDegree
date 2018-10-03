//#include "userGraph.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	//Opening file sent from Python program
	string user;
	string temp;
	vector<string> listOfNames;

	cout << "What is the name of the user? ";
	getline(cin, user);
	ifstream inFile;
	inFile.open(user);
	if (inFile.is_open()) {
		cout << "File is open!" << endl;
		while (getline(inFile, temp)) {
			listOfNames.push_back(temp);
			cout << temp << endl;
		}
		inFile.close();
	}
	else
		cout << "Error opening file. Check spelling." << endl;

	return 0;
}