/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        
        // sort list
        Collections.sort(intervals, new sortObjects());
        
        // initializations
        LinkedList<Interval> result = new LinkedList<Interval>();
        Interval a = new Interval();
        if(intervals.size() == 0) return result;
        boolean flag = false;
        
        for(int i = 0; i < intervals.size(); i++){
            
            // initialize
            Interval merged = new Interval();
            Interval b = new Interval();
            
            // get the first interval, either from intervals list or result list
            if(flag == false){
                a = intervals.get(i);
            } else{
                a = result.pollLast();
            }
            
            // get second interval, if it's not null
            if(i == intervals.size() - 1){
                break;
            }else{
                b = intervals.get(i+1);
            }
            
            // compare the two intervals for overlap and create a new interval if they do
            if(a.end >= b.start){
                merged.start = Math.min(a.start, b.start);
                merged.end = Math.max(a.end, b.end);
                flag = true;
            } else{
                merged = a;
                flag = false;
            }
            
            result.add(merged);
        }
        
        // handle edge case for last element
        result.add(a);
        
        return result;
    }
}

class sortObjects implements Comparator<Interval>{
    
    public int compare(Interval a, Interval b){
        if(a.start < b.start) return -1;
        else if(a.start == b.start) return 0;
        else return 1;
    }
}
