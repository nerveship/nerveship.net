#include <iostream>
#include <string>

int main()
{
    int size_of = 6;
    std::string Categories[6] = {"Type", "Title", "Creator", "Release", "Completion", "Rating"};
    std::string Answers[6];

    //Get answers for each category
    for (int i = 0; i < size_of; i++)
    {
        std::cout << Categories[i] << ": ";
        std::getline(std::cin, Answers[i]);
    }

    //Clear terminal
    std::cout << "\033[2J\033[1;1H";

    //Print out the formatted html
    std::cout << "<tr>\n";
    for (int i = 0; i < size_of; i++)
    {
        std::cout << "    <td class=\"fitwidth\">" + Answers[i] + "</td>\n"; 
    }
    std::cout << "</tr>\n";

    std::cout << "---------------------";
    if (Answers[0].is_lower())

}