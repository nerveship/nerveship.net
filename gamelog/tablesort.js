
var table = document.querySelectorAll("table.center")

for (i = 0; i < table.length; i++)
{
    table = table[i];

    if (thead = table.querySelector("thead")) 
    {
        headers = thead.querySelectorAll("th");

        for (j = 0; j < headers.length; j++)
        {
            headers[j].innerHTML = "<a href='#'>" + headers[j].innerText + "</a>";
        }
        thead.addEventListener("click", sortTableFunction(table))
    }
}

function sortTableFunction(table) {
    return function(ev) {
        if (ev.target.tagName.toLowerCase() == 'a') {
            sortRows(table, siblingIndex(ev.target.parentNode));
            ev.preventDefault();
        }
    };
}