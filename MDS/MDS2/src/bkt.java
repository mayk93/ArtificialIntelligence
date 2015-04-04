import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.StringTokenizer;

import javax.swing.text.html.HTMLDocument.Iterator;

public class bkt
{
	static Set<String> variable1;
	static Set<String> variable2;
	static ArrayList<String> variables;
	static int maxId;
	static MyProgram myProgram;
	static ReservedStuff reservedStuff;
	
	static String getFile(String file1, String file2) throws FileNotFoundException
	{
		Scanner sc1 = new Scanner(new File(file1));
		Scanner sc2 = new Scanner(new File(file2));
		while(sc1.hasNext())
		{
			String input = sc1.next();
			if(!reservedStuff.isUntouchable(input))
			{
				variable1.add(input);
			}
		}
		
		while(sc2.hasNext())
		{
			String input = sc2.next();
			if(!reservedStuff.isUntouchable(input))
			{
				variable2.add(input);
			}
		}
		
		if(variable1.size() > variable2.size())
		{
			java.util.Iterator<String> it = variable1.iterator();
			while(it.hasNext())
			{
				String input = it.next();
				variables.add(input);
			}
			variable1.clear();
			variable2.clear();
			sc1.close();
			sc2.close();
			return file2;
		}
		else
		{
			java.util.Iterator<String> it = variable2.iterator();
			while(it.hasNext())
			{
				String input = it.next();
				variables.add(input);
			}
			variable1.clear();
			variable2.clear();
			sc1.close();
			sc2.close();
			return file1;
		}
	}
	
	static void buildProgram(String file) throws IOException
	{
		BufferedReader br = new BufferedReader(new FileReader(file));
		String line = br.readLine();
		while(line != null)
		{
			if(line.contains("#"))
			{
				StringTokenizer st = new StringTokenizer(line);
				while(st.hasMoreTokens())
				{
					myProgram.myAdd(new Element(st.nextToken(), false));
					myProgram.myAdd(new Element(" ", false));
				}
			}
			else
			{
				StringTokenizer st = new StringTokenizer(line);

				while(st.hasMoreTokens())
				{
					String input = st.nextToken();
					if(reservedStuff.isUntouchable(input))
					{
						myProgram.myAdd(new Element(input, false));
						
					}
					else
					{
						myProgram.myAdd(new Element(input, true));
					}
					myProgram.myAdd(new Element(" ", false));
				}
			}
			
			myProgram.myAdd(new Element("\n", false));
			line = br.readLine();
		}
		br.close();
	}
	
	static void replace()
	{
		int it = 0;
		System.out.print(myProgram.Rename.size());
		for(int i = 0; i < myProgram.Elements.size(); i++)
		{
			if(!reservedStuff.isUntouchable(myProgram.Elements.get(i).inf) && myProgram.Elements.get(i).inf != " " && myProgram.Elements.get(i).inf != "\n")
			{
				myProgram.Elements.set(i, new Element(myProgram.Rename.get(it++),true));
			}
		}
	}
	
	static void bk(int k)
	{
		if(k == myProgram.Rename.size())
		{
			replace();
			afis();
		}
		else
		{
			
			for(int i = 0; i < variables.size() ; i++)
			{
				myProgram.Rename.set(k, variables.get(i));
				bk(k+1);
			}
		}
	}
	
	static void afis()
	{	
		
		java.util.Iterator<Element> it = myProgram.Elements.iterator();
		while(it.hasNext())
		{
		    System.out.print(it.next().inf);
		}
	}
	
	public static void main(String args[]) throws IOException
	{
		myProgram = new MyProgram();
		variable1 = new HashSet<String>();
		variable2 = new HashSet<String>();
		variables = new ArrayList<String>();
		reservedStuff = new ReservedStuff();
		String file = getFile("mySample.c", "clearfile.c");
		
		buildProgram(file);
		bk(0);
		
	}
	
}
