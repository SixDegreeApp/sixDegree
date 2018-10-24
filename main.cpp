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

	cout << "What is the username of the person you're searching? ";
	getline(cin, user);
	ifstream inFile;
	inFile.open(user);
	if (inFile.is_open()) {
		cout << "File is open!" << endl;
		while (getline(inFile, temp)) {
			int tempInt = stoi(temp);
			listOfNames.push_back(tempInt);
			cout << temp << endl;
		}
		inFile.close();
	}
	else
		cout << "Error opening file. Check spelling." << endl;

	/****************************BEGIN DUAL BFS******************************/
	//First we will turn every follower into a user object. Could do in above user loop.
	Graph listOfIds();// Insert graph size based on Followers data
	for (int iter = 0; iter < listOfNames.size(); iter++) {
		listOfIds.addEdge(listOfNames[iter]); // Insert an edge by grabbing the Users ID and connecting it to either the orig user or the target account.
	}

	//Perform BFS with above graph.
	listOfIds.bfs();
	// Create a graph given in the above diagram.
	return 0;
}