public class Element
{
	String inf;
	boolean editable;
	int id;
	Element(String input, boolean edit)
	{
		inf = input;
		editable = edit;
	}

	public String getInf()
	{
		return inf;
	}
	
	public void setInf(String input)
	{
		inf = input;
	}
	public boolean isEditable() 
	{
		return editable;
	}
	
}