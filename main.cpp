//#include "userGraph.h"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include "user.cpp"
#include "graph.cpp"

using namespace std;

int main()
{
	//Opening file sent from Python program
	string user;
	string temp;
	vector<int> listOfNames;

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

	/****************************BEGIN DUAL BFS******************************/
	//First we will turn every follower into a user object. Could do in above user loop.
	
	// Create a graph given in the above diagram 
	Graph g();// Insert graph size based on Followers data
	g.addEdge(); // Insert an edge by grabbing the Users ID and connecting it to either the orig user or the target account.
	return 0;
}