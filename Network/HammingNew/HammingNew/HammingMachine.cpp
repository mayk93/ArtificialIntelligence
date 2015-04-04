#include "stdafx.h"
#include "HammingMachine.h"


HammingMachine::HammingMachine()
{
}


HammingMachine::~HammingMachine()
{
}

bool HammingMachine::isPowerOfTwo(int toCheck)
{
	return toCheck && !(toCheck & (toCheck - 1));
}

bool HammingMachine::parity(vector<bool> toEncode, int step)
{
	int sum = 0;
	int index = step;
	int vectorLength = toEncode.size();
	while (index < vectorLength)
	{
		int steppingIndex = index;
		while ((steppingIndex <= step) && (steppingIndex < vectorLength))
		{
		}

	}
}

vector<bool> HammingMachine::encode(vector<bool> toEncode)
{
	vector<bool> redundancyBits;
	int vectorLength = toEncode.size();
	for (int step = 1; (step << 1) < vectorLength; step <<= 1)
	{
		redundancyBits.push_back(this->parity(toEncode,step));
	}
}