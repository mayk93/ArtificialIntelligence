#pragma once
#include <iostream>
#include <vector>

using namespace std;

class HammingMachine
{
public:
	HammingMachine();
	~HammingMachine();
	vector<bool> encode(vector<bool> toEncode);
	bool check(vector<bool> toCheck);
private:
	bool parity(vector<bool> toEncode, int step);
	bool isPowerOfTwo(int toCheck);
};

