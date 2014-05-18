import java.util.HashSet;

public class ReservedStuff
{
	static HashSet<String> symbols;
	static HashSet<String> reservedWords;
	
	static boolean isUntouchable(String input)
	{
		if(isOperator(input) || isNumber(input) || isReservedWord(input))
		{
			return true;
		}
		return false;
	}
	static boolean isOperator(String input)
	{
		if(symbols.contains(input) == true)
		{
			return true;
		}
		return false;
	}
	
	static boolean isNumber(String input)
	{
		if(input.length() == 0)
		{
			return false;
		}
		
		for(int i = 0; i < input.length(); i++)
		{
			if(input.charAt(i) <'0' || input.charAt(i) > '9')
			{
				return false;
			}
		}
		
		return false;
	}
	
	static boolean isReservedWord(String input)
	{
		if(input.length() == 0)
		{
			return false;
		}
		
		if(reservedWords.contains(input))
		{
			return true;
		}
		return false;
	}
	
	public ReservedStuff()
	{
		symbols = new HashSet<String>();
		reservedWords = new HashSet<String>();
		
		symbols.add("~");//http://www.c-lang.thiyagaraaj.com/tutorials/c-basics/c-character-set
		symbols.add("!");
		symbols.add("#");
		symbols.add("$");
		symbols.add("%");
		symbols.add("^");
		symbols.add("&");
		symbols.add("*");
		symbols.add("(");
		symbols.add(")");
		symbols.add("+");
		symbols.add("|");
		symbols.add("\\");
		symbols.add("`");
		symbols.add("-");
		symbols.add("=");
		symbols.add("{");
		symbols.add("}");
		symbols.add("[");
		symbols.add("]");
		symbols.add(":");
		symbols.add("*");
		symbols.add(";");
		symbols.add("<");
		symbols.add(">");
		symbols.add("?");
		symbols.add(",");
		symbols.add(".");
		symbols.add("/");
		symbols.add("\"");
		
		reservedWords.add("auto");
		reservedWords.add("break");
		reservedWords.add("case");
		reservedWords.add("char");
		reservedWords.add("const");
		reservedWords.add("continue");
		reservedWords.add("default");
		reservedWords.add("do");
		reservedWords.add("double");
		reservedWords.add("else");
		reservedWords.add("enum");
		reservedWords.add("extern");
		reservedWords.add("float");
		reservedWords.add("for");
		reservedWords.add("goto");
		reservedWords.add("if");
		reservedWords.add("int");
		reservedWords.add("long");
		reservedWords.add("register");
		reservedWords.add("return");
		reservedWords.add("short");
		reservedWords.add("signed");
		reservedWords.add("sizeof");
		reservedWords.add("static");
		reservedWords.add("struct");
		reservedWords.add("switch");
		reservedWords.add("typedef");
		reservedWords.add("union");
		reservedWords.add("unsigned");
		reservedWords.add("void");
		reservedWords.add("volatile");
		reservedWords.add("while");
		reservedWords.add("inline");
		reservedWords.add("restrict");
		reservedWords.add("_Bool");
		reservedWords.add("_Complex");
		reservedWords.add("_Imaginary");		
		
	}
	
}