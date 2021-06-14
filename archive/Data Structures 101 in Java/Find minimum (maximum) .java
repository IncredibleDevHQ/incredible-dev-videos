class MinMax {
    static int getMin(int arr[], int n){
        int res = arr[0];
        for (int i = 1; i < n; i++)
            res = Math.min(res, arr[i]);
        return res;}
  
    static int getMax(int arr[], int n){
        int res = arr[0];
        for (int i = 1; i < n; i++)
            res = Math.max(res, arr[i]);
        return res;}
