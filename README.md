# RISC-V_-2-Bit_Histroy_Predictor 
Implementing 2-Bit_Histroy_Predictor with Python 
## To run the code: 
>* STEP1 Enter your input "T" and "N" (Must Be in capital letters)    
>* STEP2 RUN!  

## Sample Inputs and Outputs: 
>code method  >![image](code_flow_chart.png)

## Sample Inputs and Outputs:   
>Input:  TTTTNNTNTNTNTNTNT  
>  
>Output:  
>NN ['sn', 'sn', 'sn', 'sn'] &nbsp;     Ground truth: T  Predict: N     predict wrong    &nbsp;  Mispredict count =  1  
>NT ['wn', 'sn', 'sn', 'sn'] &nbsp;     Ground truth: T  Predict: N     predict wrong    &nbsp;  Mispredict count =  2  
>TT ['wn', 'wn', 'sn', 'sn'] &nbsp;     Ground truth: T  Predict: N     predict wrong    &nbsp;  Mispredict count =  3  
>TT ['wn', 'wn', 'sn', 'wn'] &nbsp;     Ground truth: T  Predict: N     predict wrong    &nbsp;  Mispredict count =  4  
>TT ['wn', 'wn', 'sn', 'wt'] &nbsp;     Ground truth: N  Predict: T     predict wrong    &nbsp;  Mispredict count =  5  
>TN ['wn', 'wn', 'sn', 'wn'] &nbsp;     Ground truth: N  Predict: N     predict correct  &nbsp;  Mispredict count =  5  
>NN ['wn', 'wn', 'sn', 'wn'] &nbsp;     Ground truth: T  Predict: N     predict wrong    &nbsp;  Mispredict count =  6  
>NT ['wt', 'wn', 'sn', 'wn'] &nbsp;     Ground truth: N  Predict: N     predict correct  &nbsp;  Mispredict count =  6  
>TN ['wt', 'sn', 'sn', 'wn'] &nbsp;     Ground truth: T  Predict: N     predict wrong    &nbsp;  Mispredict count =  7  
>NT ['wt', 'sn', 'wn', 'wn'] &nbsp;     Ground truth: N  Predict: N     predict correct  &nbsp;  Mispredict count =  7  
>TN ['wt', 'sn', 'wn', 'wn'] &nbsp;     Ground truth: T  Predict: N     predict wrong    &nbsp;  Mispredict count =  8  
>NT ['wt', 'sn', 'wt', 'wn'] &nbsp;     Ground truth: N  Predict: N     predict correct  &nbsp;  Mispredict count =  8  
>TN ['wt', 'sn', 'wt', 'wn'] &nbsp;     Ground truth: T  Predict: T     predict correct  &nbsp;  Mispredict count =  8  
>NT ['wt', 'sn', 'st', 'wn'] &nbsp;     Ground truth: N  Predict: N     predict correct  &nbsp;  Mispredict count =  8  
>TN ['wt', 'sn', 'st', 'wn'] &nbsp;     Ground truth: T  Predict: T     predict correct  &nbsp;  Mispredict count =  8  
>NT ['wt', 'sn', 'st', 'wn'] &nbsp;     Ground truth: N  Predict: N     predict correct  &nbsp;  Mispredict count =  8  
>TN ['wt', 'sn', 'st', 'wn'] &nbsp;     Ground truth: T  Predict: T     predict correct  &nbsp;  Mispredict count =  8  
