#include <iostream>
using namespace std;

int main()
{
    string Categories[8] = {"Title", "Developer", "Publisher", "Genre", "Platform", "Release", "Completion", "Rating"};
    string Answers[8];

    //Get answers for each category
    for (int i = 0; i < 8; i++)
    {
        cout << Categories[i] << ": ";
        getline(cin, Answers[i]);
    }

    //Print out the formatted html
    cout << "<tr>\n";
    for (int i = 0; i < 8; i++)
    {
        cout << "    <td class=\"fitwidth\">" + Answers[i] + "</td>\n"; 
    }
    cout << "</tr>\n";
}