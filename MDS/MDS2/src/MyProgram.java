import java.util.ArrayList;

public class MyProgram 
{
	ArrayList<Element> Elements;
	ArrayList<String> Rename;
	
	MyProgram()
	{
		Elements = new ArrayList<Element>();
		Rename = new ArrayList<String>();
	}
	
	void myAdd(Element e)
	{
		Elements.add(e);
		if(e.isEditable())
		{
			Rename.add(e.getInf());
		}
	}
}
