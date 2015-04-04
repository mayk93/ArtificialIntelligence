
import br.ufpe.cin.groundhog.Project;
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

class Scoring
{
    static void score(String contentOne,String contentTwo)
    {
        int [][]pointsTable=new int[contentOne.length()+1][contentTwo.length()+1];
        
        for(int i=1;i<=contentOne.length();i++)
            for(int j=1;j<=contentTwo.length();j++)
            {
                if(contentOne.toCharArray()[i-1]==contentTwo.toCharArray()[j-1])
                {
                    pointsTable[i][j]=pointsTable[i-1][j-1]+1;
                }
                else
                {
                    pointsTable[i][j]=0;
                }
            }
        
        int sum=0;
        int max = 0;
        for(int i=1;i<=contentOne.length();i++)
        {
            int max1=max;
            
            for(int j=1;j<=contentTwo.length();j++)
            {
                if(pointsTable[i][j]>max)
                {
                    max=pointsTable[i][j];
                }
            }
            if(max1>max)
            {
                System.out.println(max1);
                sum+=max1;
            }
        }
        sum+=max;
        
        System.out.println((sum*100)/contentOne.length()+"% of contentOne");
        System.out.println((sum*100)/contentTwo.length()+"% of contentTwo");
        
		try {
                        // De refactorizat preluare numelor
                        String inputFile = "inputFileName.c";
                        
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
                        

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}        
    }

    void newScore() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    float newScore(String toSearchFileName, Project p) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}