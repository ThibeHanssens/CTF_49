                                                                        #include <stdio.h>
                                                                   #include <stdlib.h>
                                                                                    void manipulate(int **arr, int size) {
                                                                      for (int i = 0; i < size; i++) {
                                             *(*(arr) + i) = (i + 1) * 10;
                                                                      }
                                                                            }
                                                                 int main() {
                                                                       int **ptrArr;
                                             int size = 5;
                                                                                                          ptrArr = (int **)malloc(size * sizeof(int *));
                                                                                                 for (int i = 0; i < size; i++) {
                                                                                                                      *(ptrArr + i) = (int *)malloc(sizeof(int));
                                                                                                 }
                                                                                                                   manipulate(ptrArr, size);
                                                                                                   for (int i = 0; i < size; i++) {
                                                                                                                  printf("Value at ptrArr[%d] = %d\n", i, *(*(ptrArr + i)));
                                                                                                         free(*(ptrArr + i));
                                                                                                                }
                                                                                                                    free(ptrArr);
                                                                         ptrArr = NULL;
                                                                                                                   for (int i = 0; i < size; i++) {
                                                                                   *(ptrArr + i) = (int *)malloc(sizeof(int));
                                                                                                               *(*(ptrArr + i)) = (i + 1) * 100;
                                                                             }
                                                                                                                     manipulate(ptrArr, size);
                                                                                                   for (int i = 0; i < size; i++) {
                                                                                                        printf("Updated value at ptrArr[%d] = %d\n", i, *(*(ptrArr + i)));
                                                                  free(*(ptrArr + i));
                                                                                                     }
                                                                                                                    free(ptrArr);
                                                                                                                    printf("Program Finished\n")
                                                                                                     return 0;
                                                                                                                  }
