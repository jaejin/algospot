import java.util.HashMap;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

class Main {

    public List<Integer> sumOfDivisorList(int n) {
        List<Integer> list = new ArrayList<Integer>();

        for (int i = 1; i < n-1; i++) {
            if (n % i == 0) list.add(i);
        }
        return list;
    }

    public int sumList(List<Integer> list) {
        int sum = 0;
        for ( int i : list) {
            sum += i;
        }
        return sum;
    }
    
    public boolean isSemiPerfect(int n, List<Integer> list) {
        for(int i =list.size()-1;i>=0;i--) {
            if ( n >= list.get(i) ) {
                    n = n - list.get(i);
            } else if ( n < 0 ) {
                return false;
            }
        }
        return n == 0 ? true : false;
    }
    
    public String isWeird(int n) {
        List<Integer> list = sumOfDivisorList(n);
        int sum = sumList(list);
        if ( sum >= n ) {
            return isSemiPerfect(n,list) ? "not weird" : "weird";
        }
        return "not weird";
    }
    
    public static void main(String[] args) {
        Main weird = new Main();
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while(cases-- > 0) {
            int name = sc.nextInt();
            System.out.println(weird.isWeird(name));
        }
    }
}

