#include <iostream>

using namespace std;

int main()
{
    string Categories[8] = {"Title", "Developer", "Publisher", "Genre", "Platform", "Completion", "Rating"};
    string Answers[8];

    for (int i = 0; i < 7; i++)
    {
        cout << Categories[i] << ": ";
        cin >> Answers[i];
    }

    cout << "<tr>\n";
    for (int i = 0; i < 7; i++)
    {
        cout << "    <td class=\"fitwidth\">" + Answers[i] + "</td>\n";
    }
    cout << "</tr>\n";
}