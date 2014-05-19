// Hamming.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include<iostream>
#include<math.h>
#include<bitset>
#include<string>
#include<vector>

using namespace std;

void output()
{
}

int getNumberOfBits(int toGetBits)
{
	return log2(toGetBits) + 1;
}

string trim(string toTrim , int keptBits)
{
	return toTrim.substr(toTrim.length() - keptBits);
}

bool isPowerOf2(int x) 
{
	return x > 0 && !(x & (x-1));
}

void codeHamming(int bl, int rl, int ml, string toCodeString)
{
	vector<int> hammingCode(ml+1);
	int toCodeBinary = stoi(toCodeString);
	cout << toCodeBinary << endl;
	hammingCode.at(0) = 3;
	for (int i = ml; i > 0; i--)
	{
		if (isPowerOf2(i))
		{
			hammingCode.at(i) = 2;
		}
		else
		{
			hammingCode.at(i) = toCodeBinary % 10;
			toCodeBinary = toCodeBinary / 10;
		}
	}

	vector<int> trueHammingCode(ml);
	for (int i = 1; i <= ml; i++)
	{
		trueHammingCode.at(i - 1) = hammingCode.at(i);
	}

	for (vector<int>::iterator it = trueHammingCode.begin(); it != trueHammingCode.end(); ++it)
	{
		cout << *it;
	}
	cout << endl;
}

/*
BMR stands for:
1. Block length.
2. Message length.
3. Redundancy length.
B+R=M.
*/
void calculateBMR(string toCodeString)
{
	int blockLength = toCodeString.length();
	int redundancyLength;

	for (int i = 0;; i++)
	{
		if (pow(2, i) >= blockLength + i + 1)
		{
			redundancyLength = i;
			break;
		}
	}

	int messageLength = blockLength + redundancyLength;

	codeHamming(blockLength, redundancyLength, messageLength, toCodeString);
}

void convert(int toCodeDecimal)
{
	int numberOfBits = getNumberOfBits(toCodeDecimal);
	string toCodeString64 = bitset<64>(toCodeDecimal).to_string();
	string toCodeString = trim(toCodeString64, numberOfBits);
	calculateBMR(toCodeString);
}

void input()
{
	int toCodeDecimal;
	cout << "Input number to code: "<< endl;
	cin >> toCodeDecimal;

	convert(toCodeDecimal);
}

int _tmain(int argc, _TCHAR* argv[])
{
	input();
	return 0;
}

