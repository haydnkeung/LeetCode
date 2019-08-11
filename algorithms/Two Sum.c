#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int *result = malloc(sizeof(int)*2);
    for(int i = 0; i < numsSize;i++){
        int outer = nums[i];
        for(int j = 0; j < numsSize;j++){
            if(outer+nums[j]==target&&i!=j){
                *result=i;
                *(result+1)=j;
            }
        }
    }
    return result;
}