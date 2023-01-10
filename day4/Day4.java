package advent_of_code2022.day4;

import java.util.ArrayList;
import java.util.List;

public class Day4 {
    private MyQueue<Integer> queue;
    

    public Day4(MyQueue<Integer> queue) {
        this.queue = queue;
    }
    public Integer compare(){
        int a,b,c,d;
     
        a = queue.dequeue();
        b = queue.dequeue();
        c = queue.dequeue();
        d = queue.dequeue();

        if(a <= c){ // check left limit
            if(d <= b){  // check right limit
                // then c,d is an element in [a,b]
                return 1;     
            }
        }
        if(c <= a){ // check left limit
            if(b <= d){ // check right limit
                // then a,b is an element in [c,d]
                return 1;     
            }    
        }
        return 0;
    }
    public Integer overlap(){
        int a,b,c,d;
     
        a = queue.dequeue();
        b = queue.dequeue();
        c = queue.dequeue();
        d = queue.dequeue();

        if(a <= c && c <= b){ // if c is an element in [a,b]
            
            return 1;  
            }

        if(c <= a && a <= d){ //if a is an element in [c,d]
            return 1;
            }    
        return 0;
    }
  
}
