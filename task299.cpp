#include <iostream>
#include <string>

using namespace std;

// function convert integer to equivalent string
string i_s(int n)                         
{
	string s = "", sym, temp = "";
	if (n < 10)
	{
		s = n + 48;
		return s;
	}
	while (n > 0)
	{
		sym = (n % 10) + 48;
		temp += sym;
		n /= 10;
	}
	for (unsigned i = temp.size() - 1; i > 0; --i)
	{
		s += temp[i];
	}
	s += temp[0];
	return s;
}


// function shows how many numbers are equals in secret value and guess value; and how many numbers take their place
string getHint(string secret, string guess)  
{
	string g = guess;
	int l = secret.length();
	int b = 0, c = 0;
	for (int i = 0; i < l; ++i)
	{
		if (secret[i] == guess[i])
		{
			b++;
			guess[i] = 'a';
		}
	}
	
	for (int i = 0; i < l; ++i)
		for (int j = 0; j < l; ++j)
		{
			if (secret[i] == guess[j])
				c++;
		}
	guess = g;
	string res = "";
	string num1, num2;
	num1 = i_s(b);
	num2 = i_s(c);
	res += num1;
	res += "A";
	res += num2;
	res += "B";
	return res;
}
int main()
{
	string s1, s2, s;
	s1 = "11";
	s2 = "10";
	s = getHint(s1, s2);
	cout << s << endl;
	system("pause");
	return 0;
}
