#include <iostream>
#include <string>
#include <vector>

using namespace std;

// BinarysSearch of element in the array, that can be shifted as many times as you like
// if num is not in array  -->   return -1 
// else                    -->   return position of num
int binarySearch(vector<int>&arr_, int num)
    {
        int end = arr_.size(), begin = 0;
        int mid;
        while(begin < end)
        { 
            mid = (end+begin)/2;
            if(arr_[mid]>num)
            {
                if (num < arr_[begin])
                    begin=mid+1;
                else
                    end = mid;
            }
            else if(arr_[mid]<num)
            {
                if (num > arr_[begin])
                    begin=mid+1;
                else
                    end = mid;
            }  
            else return mid;
        }    
        return -1;
    }
    
    //check function on test data 
    bool test1()
    {
        int num = 1,
            pos = 4;
        vector<int> arr(6, 0);
        arr[0] = 3;
        arr[1] = 4;
        arr[2] = 5;
        arr[3] = 6;
        arr[4] = 1;
        arr[5] = 2;
        
        return binarySearch(arr,num) == pos;
    }
    
    int main()
    {
        if (test1()) cout << "Test is passed successfully" << endl;
        else cout << "Test is failed :(" << endl;
        return 0;
    }
