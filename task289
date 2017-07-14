#include <iostream>
#include <vector>

using namespace std;
void gameOfLife(vector<vector<int>>& board) 
{
	if (board.size() == 0)
		return;
	vector<vector<int>> b = board;
	int n = board.size(), m = board[0].size();
	
	
	if (m == 1)
	{
		if (b[0][0] == 1)
		{
			board[1][0] += 1;
			board[0][0] += 10;
		}

		if (b[n - 1][0] == 1)
		{
			board[n - 2][0] += 1;
			board[n - 1][0] += 10;
		}

		for (int i = 1; i < n - 1; ++i)
		{
			if (b[i][0] == 1)
			{
				board[i - 1][0] += 1;
				board[i + 1][0] += 1;
				board[i][0] += 10;
			}
		}
		return;
	}

	else
	{
		if (b[0][0] == 1)
		{
			board[1][0] += 1;
			board[0][1] += 1;
			board[1][1] += 1;
			board[0][0] += 10;
		}

		if (b[n - 1][0] == 1)
		{
			board[n - 2][0] += 1;
			board[n - 2][1] += 1;
			board[n - 1][1] += 1;
			board[n - 1][0] += 10;
		}

		if (b[0][m - 1] == 1)
		{
			board[0][m - 2] += 1;
			board[1][m - 2] += 1;
			board[1][m - 1] += 1;
			board[0][m - 1] += 10;
		}

		if (b[n - 1][m - 1] == 1)
		{
			board[n - 1][m - 2] += 1;
			board[n - 2][m - 1] += 1;
			board[n - 2][m - 2] += 1;
			board[n - 1][m - 1] += 10;
		}

		return;
	}
}

int main()
{
	vector <vector<int>> myBoard(2);
	myBoard[0].push_back(1);
	myBoard[0].push_back(0);
	gameOfLife(myBoard);

	for (int i = 0; i < 1; ++i)
	{
		for (int j = 0; j < 2; ++j)
		{
			cout << myBoard[i][j] << " ";
		}
		cout << endl;
	}
	system("pause");
	return 0;
}
