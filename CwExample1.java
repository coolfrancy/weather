import java.util.Scanner;

public class CwExample2 {

    // Method to calculate circle area
    public static double circleArea(double circleDiameter) {
        double circleRadius;
        double circleArea;

        // convert diameter to radius
        circleRadius = circleDiameter / 2.0;

        // calculate circle area
        circleArea = Math.PI * circleRadius * circleRadius;

        // send computed area back to caller
        return circleArea;
    }

    /**
     * Estimates total calories of a round pizza given its diameter
     * @param diameter pizza diameter
     * @return total calories
     */
    public static double pizzaCalories(double diameter) {
        final double CALORIES_SQUARE_INCH = 16.7;
        double totalCalories;

        totalCalories = circleArea(diameter) * CALORIES_SQUARE_INCH;

        return totalCalories;
    }

    // Validate user input for diameter
    public static double diameterValidation(Scanner input) {
        double positiveDiameter = 0;

        while (true) {
            // Validate numeric input
            if (input.hasNextDouble()) {
                positiveDiameter = input.nextDouble();
                if (positiveDiameter > 0) {
                    break; // valid positive diameter
                } else {
                    System.out.println("Please enter a positive number!");
                }
            } else {
            

                System.out.println("Invalid input. Please enter a numeric value.");
                input.nextLine();
            }
        }
        return positiveDiameter;
    }


    public static void main(String[] args) {
        double calories, diameter;
        char another;
        Scanner input = new Scanner(System.in);

        do {
            System.out.print("Enter pizza diameter: ");
            diameter = diameterValidation(input);

            calories = pizzaCalories(diameter);

            System.out.printf("%.1f inch pizza has %.2f calories.%n", diameter, calories);

            System.out.print("Do you want to calculate another pizza? (y/n): ");
            another = input.next().toLowerCase().charAt(0);

        } while (another == 'y');

        input.close();
    }
}