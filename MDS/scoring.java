abstract class Scoring
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
    }
}

public class MDS {

    public static void main(String[] args) {
        Scoring.score("abaabaradfasdfreacaerdaesdeaa", "abacareadsaf");
    }
    
}