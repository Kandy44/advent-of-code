#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <numeric>
using namespace std;

vector<int> read_data(ifstream &in)
{
    vector<int> calories;
    int cur_calories = 0;
    string cur_line;
    while (getline(in, cur_line))
    {
        if (cur_line.length() > 0)
        {
            int cur_calorie = stoi(cur_line);
            cur_calories += cur_calorie;
        }
        else
        {
            if (cur_calories > 0)
            {
                calories.push_back(cur_calories);
                cur_calories = 0;
            }
        }
    }

    if (cur_calories > 0)
    {
        calories.push_back(cur_calories);
        cur_calories = 0;
    }

    sort(calories.begin(), calories.end(), greater<int>());
    return calories;
}

int first_n_max_sum(vector<int> &calories, int n)
{
    return accumulate(calories.begin(), calories.begin() + n, 0);
}

int main()
{
    ifstream in("../inputs/1.in");
    vector<int> calories = read_data(in);
    cout << first_n_max_sum(calories, 1) << "\n";
    cout << first_n_max_sum(calories, 3) << "\n";
    in.close();
    return 0;
}
