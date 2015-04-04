window.onload = myMain;

function myMain() 
{
    var toSearchIn  = document.getElementById("textArea");
    var toSearchFor = document.getElementById("textInput");
    var button      = document.getElementById("inputButton");
    
    button.onclick = function(){searchFunction(toSearchFor,toSearchIn);}
}

function Test(toTest)
{
    if(!toTest || 0 === toTest.length)
    {
        alert("Empty String.");
        return 0;
    }
    else
    {
        pattern = /{/g;
        if(pattern.test(toTest))
        {
            alert("Curly braces detected. Malicious code assumed.");
            return 0;
        }
    }
    return 1;
}

function searchFunction(toSearchFor,toSearchIn)
{
    var toSearch = toSearchFor.value;
    if(Test(toSearch) == 1)
    {
        switch(toSearchIn.value.search(toSearch))
        {
            case 0:
            {
                alert("Found");
                break;
            }
            case -1:
            {
                alert("Not Found");
                break;
            }
            default:
            {
                alert("Error");
                break;
            }
        }
    }
}
