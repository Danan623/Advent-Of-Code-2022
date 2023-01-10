package advent_of_code2022.day4;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {
    
    public static void main(String[] args) throws IOException {
        // a-b, c-d
        // är (1) a <= c ? om sant/falskt => är (2) d <= b ? om sant : [a,..,c,...,d,...,b] annars falsk
        // om a är falsk så kommer b vara falsk också, kontrollera i så fall om (3) c <= a om sant/falskt => är (4) b <= d om sant : [c,..,a,...,b,...,d] annars falsk

        // vi har alltså : (1) = true -> check if (2) = true, if (2) return 0 else return 1
        // check if (3) = true -> check if (4) = true, if (4) false return 0 else return 1
        /**
         * file class Java 7 ++
         */ 
        List<String> lines2 = new ArrayList();
        
        // test case
        lines2.add("2-4,6-8");
        lines2.add("2-3,4-5");
        lines2.add("5-7,7-9");
        lines2.add("2-8,3-7");
        lines2.add("6-6,4-6");
        lines2.add("2-6,4-8");

        List<String> lines = Files.readAllLines(Paths.get("src/advent_of_code2022/day4/day4.txt"));
        MyListModifier<String> mod_lines = new MyListModifier<>(lines);

        List<String> moded_list = new ArrayList<>();
        moded_list = mod_lines.remove("", ",", "-");
        MyQueue<Integer> queue_task1 = new MyQueue<>();
        MyQueue<Integer> queue_task2 = new MyQueue<>();
        int day4_task1 = 0;
        int day4_task2 = 0;
        for(String s : moded_list){

            queue_task1.enqueue(Integer.valueOf(s));
            queue_task2.enqueue(Integer.valueOf(s));

            if(queue_task1.getSize() == 4){

                Day4 task1 = new Day4(queue_task1);
                day4_task1 += task1.compare();

                Day4 task2 = new Day4(queue_task2);
                day4_task2 += task2.overlap();

            }

            
        } System.out.println(day4_task1); // ********** correct!
        System.out.println(day4_task2); // ********** correct!
       
          
    }
    
}
