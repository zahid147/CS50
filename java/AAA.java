import java.util.Scanner;

public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter the score: ");
    int score = scanner.nextInt();

    if (score >= 70 && score <= 100) {
        String grade = "A";
    } else if (score >= 50 && score <= 69) {
        String grade = "B";
    } else if (score >= 40 && score <= 49) {
        String grade = "C";
    } else if (score >= 0 && score <= 39) {
        String grade = "D";
    } else {
        return "Invalid";
    }

    System.out.println("Grade: " + grade);

    scanner.close();
}

