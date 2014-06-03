import br.ufpe.cin.groundhog.Project;
import br.ufpe.cin.groundhog.search.SearchGitHub;
import br.ufpe.cin.groundhog.search.SearchModule;
import com.google.inject.Guice;
import com.google.inject.Injector;
import com.mongodb.BasicDBObject;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBObject;
import com.mongodb.MongoClient;
import java.awt.*;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import javax.swing.*;

public class ClearFile 
{
        Injector injector = Guice.createInjector(new SearchModule());
        SearchGitHub searchGitHub = injector.getInstance(SearchGitHub.class);
    
	static PrintWriter writer;
	static boolean existingComment = false;
	static boolean needSpace = false;
	static ReservedStuff reservedStuff;
	
	public static String getSubstring(String line,int start, int finish)
	{
		if(start > finish || finish + 1 > line.length())
		{
			return null;
		}
		return line.substring(start,finish + 1);
	}
	
	public static void write(String line,boolean endLine)
	{
		if(line == null)
		{
			return;
		}
		if(line.contains("#"))
		{
			endLine = true;
		}
		
		StringBuilder stringBuilder = new StringBuilder();
		stringBuilder.append(" ");
		for(int j = 0; j < line.length(); j++)
		{
			if(reservedStuff.isOperator(String.valueOf(line.charAt(j))))
			{
				if(j > 0)
				{
					if(stringBuilder.charAt(stringBuilder.length() - 1) == ' ')
					{
						stringBuilder.append(line.charAt(j));
					}
					else
					{
						if(!reservedStuff.isOperator(String.valueOf(line.charAt(j - 1))))
						{
							stringBuilder.append(" ");
						}
						stringBuilder.append(line.charAt(j));
					}
				}
				else
				{
					stringBuilder.append(line.charAt(j));
				}
			}
			
			else//nu e operator
			{
				if(line.charAt(j) == ' ' && (stringBuilder.charAt(stringBuilder.length() - 1) ==  ' '))
				{
					
				}
				else
				{
					boolean ok = true;
					if(reservedStuff.isOperator(String.valueOf(stringBuilder.charAt(stringBuilder.length()-1))))
					{
						stringBuilder.append(" ");
						ok = false;
					}
					if(ok == false)
					{
						if(line.charAt(j) != ' ')
						{
							stringBuilder.append(line.charAt(j));
						}
					}
					else
					{
						stringBuilder.append(line.charAt(j));
					}
				}
			}
		}
		
		if(stringBuilder.length() == 1)
		{
			return;
		}
		
		if(endLine)
		{
			stringBuilder.append("\n");
		}
		if(needSpace && stringBuilder.length() > 1)
		{
			System.out.print(stringBuilder);
                        
		}
		else
		{
			System.out.print(stringBuilder.substring(1));
		}
		
		if(stringBuilder.charAt(stringBuilder.length() - 1) == ' ' || stringBuilder.charAt(stringBuilder.length() - 1) == '\n')
		{
			needSpace = false;
		}
		else
		{
			needSpace = true;
		}
		
	}
	
	public static void clear(String line)
	{
		
		int start = 0;
		boolean available = true;
		for(int i = 0; i < line.length(); i++)
		{
			
			if(!existingComment)
			{
				switch (line.charAt(i))
				{
					case '#':
						for(int j = start; j < i ; j++)
						{
							if(line.charAt(j) == '#')
							{
								write(getSubstring(line, start, i - 1), true);
								start = i;
							}
						}
					break;
				
					case ';':
						write(getSubstring(line,start,i), true);
						start = i + 1 ;
					break;
								
					case '{':
						write(getSubstring(line,start,i),true);
						start = i + 1;
					break;
					
					case '}':
						write(getSubstring(line,start,i),true);
						start = i + 1;
					break;
					
					case '/':
						if(i < line.length() - 1)
						{
							if(line.charAt(i + 1) == '*')
							{
								write(getSubstring(line,start,i-1),false);
								available = false;
								existingComment = true;
							}
							
							if(line.charAt(i + 1) == '/')
							{ 
								write(getSubstring(line,start,i-1),false);
								i = line.length();
								available = false;
							}
						}
						
					break;
					
					default:
						if(i == line.length() - 1 && available == true)
						{
							write(getSubstring(line,start,i),false);
						}
					break;
				}
			}
			else
			{
				if( i < line.length() - 1)
				{
					if(line.charAt(i) == '*' && line.charAt(i + 1) == '/')
					{
						existingComment = false;
						start = i + 2;
					}
				}
			}
		}
	}
	
	public static void main(String args[])
	{
            
                ProcessInput processInput = new ProcessInput();
            
                JFrame frame = new JFrame("Notif");
                
                frame.setSize(500,500);
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                
                JPanel panel = new JPanel();
                frame.add(panel);
                JLabel label = new JLabel("File");
                panel.add(label);
                
                JTextField textField = new JTextField("mySample.c",20);
                panel.add(textField);
                
                frame.setVisible(true);
                
		try {
                        String inputFile = textField.getText();
                        
                        MongoClient mongoClient = new MongoClient( "localhost" , 27017 );
                        DB db = mongoClient.getDB( "theftDB" );
                        DBCollection coll = db.getCollection("testCollection");
                        BasicDBObject doc = new BasicDBObject("name", "MongoDB")
                        .append("type", "database")
                        .append("count", 1)
                        .append("info", new BasicDBObject("Problem Name", inputFile).append("Result", true));
                        coll.insert(doc);
                        
                        /*
                        Ultimul append din BasicDBObject-ul interior trebuie sa aiba loc
                        dupa evaluarea problemei.
                        
                        */
                        
                        DBObject myDoc = coll.findOne();
                        System.out.println(myDoc);
                        
			reservedStuff = new ReservedStuff();
			BufferedReader br = new BufferedReader(new FileReader(inputFile));
			writer = new PrintWriter("the-file-name.txt", "UTF-8");
			String line = br.readLine();
			while (line != null)
			{
				clear(line);
				line = br.readLine();
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
                
	}
}
