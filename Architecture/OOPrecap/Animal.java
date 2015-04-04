public class Animal
{
    private String name;
    private String sound;
    private int weight;

    public Animal()
    {
        System.out.println("Making an animal.");
    }

    public void setName(String newName)
    {
        this.name = newName;
    }

    public void setSound(String newSound)
    {
        this.sound = newSound;
    }

    public void setWeight(int newWeight)
    {
        if(newWeight > 0)
        {
            this.weight = newWeight;
        }
        else
        {
            System.out.println("Bad weight.");
        }
    }

    public String getName()
    {
        return this.name;
    }

    public String getSound()
    {
        return this.sound;
    }

    public int getWeight()
    {
        return this.weight;
    }
}
