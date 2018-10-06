#include<iostream>
#include <list> 
#include <string>

using namespace std;

class User
{
	int userID; //Unique Instagram User ID number
	string userName; //The users actaul handle for printing purposes
	int followerCount, followingCount; //Just in case this data is needed

public:
	User(); //Default Contructor

	User(int userID, string userName, int followerCount, int followingCount); //Full Contructor

	int getID();
	string getName();
	int getFollower();
	int getFollowing();
};


User::User() {
	userID = 0;
	userName = "";
	followerCount = 0;
	followingCount = 0;
}

User::User(int userID, string userName, int followerCount, int followingCount) {
	this->userID = userID;
	this->userName = username;
	this->followerCount = followerCount;
	this->followingCount = followingCount;
}

int User::getID() {
	return userID;
}

string User::getName() {
	return userName;
}

int User::getFollower() {
	return followerCount;
}

int User::getFollowing() {
	return followingCount;
}