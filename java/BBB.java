import java.util.Scanner;

public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter a string: ");
    String originalString = scanner.nextLine();

    char[] chars = str.toCharArray();
    for (int i = 0; i < chars.length; i++) {
        char c = chars[i];
        if (Character.isUpperCase(c)) {
            chars[i] = Character.toLowerCase(c);
        } else if (Character.isLowerCase(c)) {
            chars[i] = Character.toUpperCase(c);
        }
    }

    String swappedString = String(chars);
    System.out.println("Original String: " + originalString);
    System.out.println("Swapped String: " + swappedString);

    scanner.close();
}
