/*
 * This program lists the top three UUIDv4s with regards to the sum of their values. It outputs the value of the said sums.
 * The list is user generated.
 *
 * N.B. No mechanisms have been implemented to safeguard the user from missusing the program.
 * This can be done with some conditional statements in the prompt method and reprompting the user to correct the input, as well as try/catch clauses.
 *
 * N.B. It is not clear what to do when we have more than three competing values for the top three places.
 * For instance, if three keys compete for the first two positions, what do we do with the next in line?
 * Do we consider it to be a winner?
 *
 * I solved this uncertainty by choosing to prioritise the sums of the values of each key.
 * This is, fisrt place is for all keys tied for first place, etc, second place - for all tiers for second place, etc.
 */

package keys;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Hashtable;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;
import java.util.UUID;

/**
 *
 * @author Georgi Karapetrov
 */

public class Keys
{       
    private static Hashtable<String, Integer> keys; // a map to store the input
    private static ArrayList<Map.Entry<String, Integer>> sorted; // a list that can be sorted by the values of the map rather than the keys
        
    //constructor
    public Keys()
    {
        keys = new Hashtable<String, Integer>();
        sorted = new ArrayList<Map.Entry<String, Integer>>();
    }
    
    //returns hash table
    private Hashtable<String, Integer> getTable() {
        return keys;
    }

    //promt, and storing the keys and summing over the values
    public static void prompt()
    {
        Scanner input = new Scanner( System.in ); // scanner for standart input
    
        //prompt
        System.out.print( "This program outputs the first three UUIDv4 keys from a list regarding the sum of their values. Let us create this list.\n"
                        + "Enter the first keys separated from their values by only a single space like this:\n"
                        + "8239b961379a4f9f854fd19d82b56dc9 24 \n" 
                        + "8239b961379a4f9f854fd19d82b56dc9 39 \n" 
                        + "533cc20dc02647cb98c9cc534112e092 166 \n"
                        + "Enter EXIT if you are finished.\n" );
        
        //store UUID's and add theirvalues while the list is being generated
        while (input.hasNext())
        {
            //check if user terminates
            String key = input.next();
            if (key.toLowerCase().contains("exit"))
            {
                break;
            }
            
            //add key and value if the user hasn't terminated
            //probram would break in most cases where the input format changes from (String + " " + int + "\n")
            int value = input.nextInt();
            addData(key, value);
        }
    }
    
    //add input line to hashtable
    public static void addData(String key, int value)
    {
        //add value to the existing value of an existing key
        if(keys.containsKey(key))
        {
            keys.put(key, value+keys.get(key));
        }
        
        //create new key and its value 
        else
            keys.put(key,value);
    }

    public static ArrayList sortTable( Hashtable<String, Integer> table )
    {
        //Transfer as List and sort
        ArrayList unsorted = new ArrayList(table.entrySet());
        Collections.sort(unsorted, new ComparatorImpl());
        return unsorted;
    }

    public static void printResults(ArrayList list)
    {
        int j = 0; // counts the tier (winner, second, third)
        for(int i=0; i < list.size(); ++i)
        {
            //break when we've printed the top three
            if ( j == 3 )
            {
                break;
            }
            
            //word wrap results
            else if ( i < list.size() - 1 )
            {
                int currentValue = Integer.parseInt( list.get(i).toString().split("=")[1] );
                int nextValue = Integer.parseInt( list.get(i+1).toString().split("=")[1] );
            
                if( currentValue == nextValue )
                System.out.print( list.get(i).toString().split("=")[0] + ", " );
                else
                {
                    System.out.println( list.get(i).toString().split("=")[0] + ": " + list.get(i).toString().split("=")[1] );
                    ++j;
                }
            }
            
            // To handle small lists as well as lists with less than three tier possition
            // we need to avoid attempting to check whether the key in the current itteration
            // has the same value as the next key
            // when we have reached the end of the list
            else if ( i == list.size() - 1 )
            {
                System.out.println( list.get(i).toString().split("=")[0] + ": " + list.get(i).toString().split("=")[1] );
            }
        }
    }
    
    //populate table automatically for test
    /*
     * This test is no proof that the program always halts or always works as intended.
     * Neither is this test able to test the prompt() method from the main file as we cannot simulate stdin.
     * However as many times as I have run this test, the tested methods run as intended.
     * Also as many times as I ran the main program, it works as long as you keep the input format (String + " " + int + "\n")
     */
    public static void generateTable()
    {
        //store each UUID and integer, in order to be able to print them
        Random integerGenerator = new Random();
        String uUID;
        int integer; 
             
        System.out.println("Input:" );
        
        //add 19 values and probably 19 UUIDs, any number should work in place of "19"
        for(int i=1; i <= 19; ++i)
        {
            uUID = UUID.randomUUID().toString();
            integer = integerGenerator.nextInt();
            //test adding method
            addData( uUID, integer );
            System.out.println(uUID + " " + integer );
        }
        
        System.out.println("Output:" );
    }
            
    public static void main(String[] args)
    {
        Keys keys1 = new Keys();
        
        //call prompt (comment out the following line if you want to test automatically)
        keys1.prompt();
        
        //or generate table automatically (uncomment the following line if you want to test automatically)
        //keys1.generateTable();
        
        //compute and print result
        keys1.printResults( sortTable( keys1.getTable( ) ) );
    } // end method main
    
    private static class ComparatorImpl implements Comparator<Map.Entry<String, Integer>> {

        public ComparatorImpl() {
        }

        @Override
        public int compare(Map.Entry<String, Integer> keyOne, Map.Entry<String, Integer> keyTwo) {
            //compare keys by value, sort in descending order
            return keyTwo.getValue().compareTo(keyOne.getValue());
        }
    }
    
} // end class Keys
