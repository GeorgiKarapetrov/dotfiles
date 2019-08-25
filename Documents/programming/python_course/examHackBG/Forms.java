/*
 * This program seats all correct configurations in standart cinema salon.
 * 
 * 
 */
package forms;


import java.util.Arrays;
import java.util.Hashtable;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

/**
 *
 * @author george
 */
public class Forms {
    //the firs set of variables allows to declare arrays in the prompt body
    //hoping that the input will be correct
    private final int rows;
    private final int cols;
    private final int instructionsCount;
    
    //stores the input salon configuration
    private final String[][] matrix;
    // deep clone of matrix
    private String[][] clone; 
    
    // store the names and their seating coordinates
    //with respct to the central name with coordinates [0,0]
    private final Hashtable<String, int[]> centralisedCoords; 
    

    //this constructor uses a user prompt and centalises the data
    public Forms()
    {
        this.centralisedCoords = new Hashtable<String, int[]>();
        Scanner input = new Scanner(System.in);
        
        //the first line gives us the salon dimensions
        String[] coords = input.nextLine().split(" ");
                
        rows = Integer.parseInt(coords[1]);
        cols = Integer.parseInt(coords[0]);
                
        this.matrix = new String[rows][cols];

        //populate the matrix
        for(int row = 0; row<rows; row++) {
            String line = input.nextLine();
            for(int col = 0; col<cols; col++) {
                this.matrix[row ][col] = line.substring(col, col+1);
            }
        }
        
        //next comes the number of instructions
        instructionsCount = Integer.parseInt(input.nextLine());
        
        //take the central element
        this.centralisedCoords.put(input.nextLine(), new int[]{0,0});
        //System.out.println(Arrays.toString(centralisedCoords.get( "A"  )));
        
        //the rest of the instructions
        for(int i = 0; i < instructionsCount; i++){
            String line = input.nextLine();
            String targetPerson = line.substring(0, 1);
            String referencePerson = line.substring(2, 3);
            String instruction = line.substring(1, 2);
            int[] delta = new int[2];
                
            //dictionary
            switch(instruction) {
                case "L":
                    delta[0] = 0;
                    delta[1] = -1;
                    break;
                case "R":
                    delta[0] = 0;
                    delta[1] = 1;
                    break;
                case "A":
                    delta[0] = -1;
                    delta[1] = 0;
                    break;
                case "B":
                    delta[0] = 1;
                    delta[1] = 0;
                    break;
            }
                
            int[] newCoordinates = new int[2];
            int[] referenceCoordinates = centralisedCoords.get(  referencePerson  );
            
            //luckily the translation is transitive
            newCoordinates[0] = referenceCoordinates[0] + delta[0];
            newCoordinates[1] = referenceCoordinates[1] + delta[1];
            
            //set
            this.centralisedCoords.put( targetPerson , newCoordinates);
        }
        // declare a resetable initial copy of the salon
        clone = new String[rows][cols];
    }
    
    //get
    public String[][] getSalon(){
        return this.matrix;
    }
    
    //get
    public Hashtable<String, int[]> getCoords(){
        return this.centralisedCoords;
    }
    
    //set clone to initial salon
    private String[][] resetClone() {        
        final String[][] clone = new String[matrix.length][];
        
        for (int row = 0; row < matrix.length; row++) {
            clone[row] = Arrays.copyOf(matrix[row], matrix[row].length);
        }
        
        return clone;
    }
    
    //maps the desired seating with respect to the central element and a given starting seat
    //this is the main method that follows the dictionary
    //and tries to map the seating fonfiguration on to the salon,
    //with respect to the central element only in order to avoid repeating solutions
    //this method also counts the solution in traversing the salon
    private boolean printIfValid(int startRow, int startCol, Set<Map.Entry<String,int[]>> entries, String[][] dummySolution)
    {
        int instructionCounter = 0;
        //for the set of instructions, follow each instruction
        //iff within the seating margins and if the seat in iteration is available
        for (Map.Entry<String, int[]> entry : entries) {
            String name = entry.getKey();
            int[] coordinates = entry.getValue();
            
            int x = startRow + coordinates[0];
            int y = startCol + coordinates[1];
            
            boolean isSafe = x >= 0 && y >= 0 && x < rows && y < cols && ".".equals(matrix[x][y]);
            
            if ( isSafe ) {
                dummySolution[x][y] = name;
            }
            
            else {
               break;
            }
            
            //print if also the last instruction has been carried out
            if( instructionCounter == entries.size() - 1) {
                this.print(dummySolution);
                return true;
            }
            
            instructionCounter++;
        }
        return false;
    }
    
    //format the printing in printIfValid()
    private void print( String[][] solution )
    {
        //print column indices
        System.out.print( " " );
        for(int j = 0; j<cols; j++)
        {
            System.out.print( j );
        }
        System.out.println( );
        
        //print the solution
        for (int i=0; i < rows; i++)
        {
            //print the row index
            System.out.print( i );
            
            //print the row
            for (int j=0; j < cols; j++)
            {
                System.out.print( solution[i][j] );
            }
            System.out.println();
        }
        //print end of solution delim
        System.out.println("----------");
    }
    
    //calls printIfValid()
    public void traverse(){
        int solutionCounter = 0;
        
        for(int row = 0; row < rows; row++) 
        {
            for(int col = 0; col < cols; col++)
            {
                
                if( printIfValid(row, col, centralisedCoords.entrySet(), this.resetClone() ) )
                {
                    solutionCounter++;
                }
            }
        }
        System.out.println( solutionCounter );
    }
    
    public static void main(String[] args) {
        Forms myCinema = new Forms();
        myCinema.traverse();
    }   
}
