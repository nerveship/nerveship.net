#include <iostream>
#include <string>

int main()
{
    std::string Categories[8] = { "Title", "Developer", "Publisher", "Genre", "Platform", "Release", "Completion", "Rating" };
    std::string Answers[8];

    //Get answers for each category
    for (int i = 0; i < 8; i++)
    {
        std::cout << Categories[i] << ": ";
        std::getline(std::cin, Answers[i]);
    }

    //Print out the formatted html
    std::cout << "<tr>\n";
    for (int i = 0; i < 8; i++)
    {
        std::cout << "    <td class=\"fitwidth\">" + Answers[i] + "</td>\n";
    }
    std::cout << "</tr>\n";
}