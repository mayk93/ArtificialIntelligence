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
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;

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
        
        //Utilizam crawlerul de Git pentru a obtine proiecte relevante
        List<Project> crawlGit(String toSearchFileName)
        {
            Injector injector = Guice.createInjector(new SearchModule());
            SearchGitHub searchGitHub = injector.getInstance(SearchGitHub.class);
            return searchGitHub.getProjects(toSearchFileName, 1, SearchGitHub.INFINITY);
        }
        
        //Calculam rezultatul
        Project computeResults(List<Project> projects , String toSearchFileName, int scoreLimit)
        {
            Scoring s = new Scoring();
            for(Project p : projects)
            {
                float score = s.newScore(toSearchFileName , p);
                if(score > scoreLimit)
                {
                    return p;
                }
            }
            
            return null;
        }
        
        //Actualizam baza de date in urma rezultatului
        void addToDB(Project p)
        {
            try {
                        MongoClient mongoClient = new MongoClient( "localhost" , 27017 );
                        DB db = mongoClient.getDB( "theftDB" );
                        DBCollection coll = db.getCollection("testCollection");
                        BasicDBObject doc = new BasicDBObject("name", "MongoDB")
                        .append("type", "database")
                        .append("count", 1)
                        .append("info", new BasicDBObject("Problem Name", "test0").append("Result", true));
                        coll.insert(doc);
                        
                        /*
                        Ultimul append din BasicDBObject-ul interior trebuie sa aiba loc
                        dupa evaluarea problemei.
                        
                        */
                        
                        DBObject myDoc = coll.findOne();
                        System.out.println(myDoc);
                        

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        }        
}
