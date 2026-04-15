namespace GamelogHelper
{
    class Program
    {
        static string[] categories = { "Type", "Title", "Creator", "Release", "Completion", "Rating" };
        static List<string> answers = new List<string>();

        static void GetInput()
        {
            DateTime today = DateTime.Today;
            DateTime yesterday = today.AddDays(-1);

            foreach (string category in categories)
            {
                Console.Write($"{category}: ");
                string answer = Console.ReadLine() ?? "";

                if (category == "Completion")
                {
                    string cleaned = answer.Trim().ToLower();

                    if (cleaned == "tday")
                    {
                        answer = today.ToString("MMMM d, yyyy");
                    }
                    else if (cleaned == "yday")
                    {
                        answer = yesterday.ToString("MMMM d, yyyy");
                    }
                    else
                    {
                        try
                        {
                            string[] formats = { "d/M/yy", "d/M/yyyy" };
                            DateTime parsed = DateTime.ParseExact(answer.Trim(), formats, null, System.Globalization.DateTimeStyles.None);
                            answer = parsed.ToString("MMMM d, yyyy");
                        }
                        catch (FormatException)
                        {
                            Console.WriteLine($"Couldn't parse date, keeping as-is: {answer}");
                        }
                    }
                }

                if (category == "Release")
                {
                    try
                    {
                        string[] formats = { "d/M/yy", "d/M/yyyy" };
                        DateTime parsed = DateTime.ParseExact(answer.Trim(), formats, null, System.Globalization.DateTimeStyles.None);

                        // This stops it putting in 2060. It hasn't happened yet.
                        if (parsed.Year > DateTime.Today.Year)
                        {
                            parsed = parsed.AddYears(-100);
                        }

                        answer = parsed.ToString("MMMM d, yyyy");
                    }
                    catch (FormatException)
                    {
                        Console.WriteLine($"Couldn't parse date, keeping as-is: {answer}");
                    }
                }

                if (category == "Rating")
                {
                    answer = answer.Trim() + "/5";
                }

                answers.Add(answer);
            }
        }

        static string FormatHtml()
        {
            // This is for the funny indent stuff, it kind of looks like shit but.
            string baseIndent = new string(' ', 3);
            string baseOffset = new string(' ', 15);

            string trIndent = baseOffset;
            string tdIndent = baseOffset + baseIndent;

            string finalString = $"{trIndent}<tr>\n";
            int totalAnswers = answers.Count;

            for (int index = 0; index < totalAnswers; index++)
            {
                string answer = answers[index];

                if (index == totalAnswers - 1)
                {
                    finalString += $"{tdIndent}<td class=\"alnright\">{answer}</td>\n";
                }
                else
                {
                    finalString += $"{tdIndent}<td>{answer}</td>\n";
                }
            }

            finalString += $"{trIndent}</tr>";
            return finalString;
        }

        static void FormatTweet()
        {
            // Makes it more natural sounding depending on the type
            string article;
            string type = answers[0].ToLower();

            if (type == "anime" || type == "music")
            {
                article = "An";
            }
            else
            {
                article = "A";
            }

            string artType = "";

            // Asks what type of music it is before continuing
            if (answers[0].ToLower() == "music")
            {
                Console.WriteLine("What type of musical release?");
                artType = Console.ReadLine() ?? "";
            }
            else
            {
                artType = answers[0];
            }

            // Prints the tweet out
            Console.WriteLine("-------------");
            Console.WriteLine($"{answers[1]} - {article} {artType} by {answers[2]}, released in {answers[3][^4..]}.\nRating: {answers[5]}");
            Console.WriteLine("https://www.nerveship.net/artlog/");
            Console.WriteLine("-------------");
        }

        static void WriteToHtml()
        {
            string htmlFile = @"artlog\index.html";

            string data = File.ReadAllText(htmlFile, System.Text.Encoding.UTF8);
            string[] lines = data.Split('\n');
            List<string> lineList = new List<string>(lines);

            string htmlString = FormatHtml();

            // The insert point will be used to put it into the right table
            // I just can't be fucked changing this yet, because it is a mess.
            int insertPoint = 0;
            if (answers[0].ToLower() == "film") insertPoint = 0;
            else if (answers[0].ToLower() == "game") insertPoint = 0;
            else if (answers[0].ToLower() == "literature") insertPoint = 0;
            else if (answers[0].ToLower() == "music") insertPoint = 0;

            lineList.Insert(49, htmlString);

            File.WriteAllText(htmlFile, string.Join('\n', lineList), System.Text.Encoding.UTF8);

            Console.WriteLine($"html string written to {htmlFile}");
        }

        static void Main()
        {
            GetInput();
            FormatTweet();
            WriteToHtml();
        }
    }
}