import java.util.Random;
import java.util.Scanner;

public class CoinFlipExample {

    // Validate user input for number of flips
    public static int numberValidation(Scanner input) {
        int validNumber = 0;

        while (true) {
            if (input.hasNextInt()) {
                validNumber = input.nextInt();
                if (validNumber > 0) {
                    break; // valid positive number
                } else {
                    System.out.print("Please enter a positive number: ");
                }
            } else {
                System.out.print("Invalid input. Please enter a numeric value: ");
                input.next(); // discard invalid token
            }
        }
        return validNumber;
    }

    // Perform coin flips starting from a random position
    public static String coinFlip(int flips, Random value) {
        int position = value.nextInt(21) - 10; // random start between -10 and 10
        int start = position;

        for (int i = 0; i < flips; i++) {
            int result = value.nextInt(2); // 0 or 1
            if (result == 0) {
                position--; // tails subtracts 1
            } else {
                position++; // heads adds 1
            }
        }

        return " flips final position" + position + ".";
    }

    // Main method
    public static void main(String[] args) {
        int numberCoinFlips;
        String result;

        Scanner input = new Scanner(System.in);
        Random value = new Random();

        System.out.print("Enter the number of coin flips: ");
        numberCoinFlips = numberValidation(input);

        result = coinFlip(numberCoinFlips, value);

        System.out.println(result);

        input.close();
    }
}