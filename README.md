# RISC-V_-2-Bit_Histroy_Predictor 
Implementing 2-Bit_Histroy_Predictor with Python 
## To run the code: 
>* STEP1 Enter your input "T" and "N" (Must Be in capital letters)    
>* STEP2 RUN!  

## Sample Inputs and Outputs:   
>Input:  TTTTNNTNTNTNTNTNT  
>  
>Output:
>NN ['sn', 'sn', 'sn', 'sn']    Ground truth: T  Predict: N     predict wrong     Mispredict count =  1  
>NT ['wn', 'sn', 'sn', 'sn']    Ground truth: T  Predict: N     predict wrong     Mispredict count =  2  
>TT ['wn', 'wn', 'sn', 'sn']    Ground truth: T  Predict: N     predict wrong     Mispredict count =  3  
>TT ['wn', 'wn', 'sn', 'wn']    Ground truth: T  Predict: N     predict wrong     Mispredict count =  4  
>TT ['wn', 'wn', 'sn', 'wt']    Ground truth: N  Predict: T     predict wrong     Mispredict count =  5  
>TN ['wn', 'wn', 'sn', 'wn']    Ground truth: N  Predict: N     predict correct   Mispredict count =  5  
>NN ['wn', 'wn', 'sn', 'wn']    Ground truth: T  Predict: N     predict wrong     Mispredict count =  6  
>NT ['wt', 'wn', 'sn', 'wn']    Ground truth: N  Predict: N     predict correct   Mispredict count =  6  
>TN ['wt', 'sn', 'sn', 'wn']    Ground truth: T  Predict: N     predict wrong     Mispredict count =  7  
>NT ['wt', 'sn', 'wn', 'wn']    Ground truth: N  Predict: N     predict correct   Mispredict count =  7  
>TN ['wt', 'sn', 'wn', 'wn']    Ground truth: T  Predict: N     predict wrong     Mispredict count =  8  
>NT ['wt', 'sn', 'wt', 'wn']    Ground truth: N  Predict: N     predict correct   Mispredict count =  8  
>TN ['wt', 'sn', 'wt', 'wn']    Ground truth: T  Predict: T     predict correct   Mispredict count =  8  
>NT ['wt', 'sn', 'st', 'wn']    Ground truth: N  Predict: N     predict correct   Mispredict count =  8  
>TN ['wt', 'sn', 'st', 'wn']    Ground truth: T  Predict: T     predict correct   Mispredict count =  8  
>NT ['wt', 'sn', 'st', 'wn']    Ground truth: N  Predict: N     predict correct   Mispredict count =  8  
>TN ['wt', 'sn', 'st', 'wn']    Ground truth: T  Predict: T     predict correct   Mispredict count =  8  
