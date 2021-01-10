public class Arguments {
    public static void main(String[] args) {
        int sum = 0;

        for (String numberStr: args) {
            final int number = Integer.parseInt(numberStr);
            sum += number;
        }

        System.out.println(sum * 1f / args.length);
    }
}
