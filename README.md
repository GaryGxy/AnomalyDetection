# AnomalyDetection
Algorithm: The underlying algorithm of this anomaly detection is using a sliding window calculation. The algorithm takes two parameters - the percentage of data as the size of sliding window and the threshold for classifying as outliers. First of all, I build a sliding window and shift this window one by one element to the right untile it reaches the end of the dataset. The size of this sliding window is determined by the parameter percentage as a centain percentage of the dataset size. According to my testing, I set 20% as the optimal percentage for both cpc and cpm dataset. For each window, I compute the mean and percentile of that window and calculate upper and lower band for the window. I define the upper band as the mean of the window adds threshold quantile value and lower band as the mean of the window subtracts threshold quantile value. And then, I compare the real value with the upper and lower band and classify those values that are either greater than the upper band or smaller than the lower band as outliers. After testing, I set 0.5 threshold as the optimal threshold for the cpc dataset and 0.95 as the optimal threshold for the cpm dataset since the outliers in cpm dataset have much greater variance.

Confusion Matrix:

- cpc_2 dataset:                           
   |(Actual Anomaly)|0|1| 
   |----|----|----|----|----|----|
   |(Predicted Anomaly)|0|1611 |0|                    
   |(Predicted Anomaly)|1|12| 1|                      

- cpm_2 dataset:            (Actual Anomaly)                
                             0    |    1                      
   (Predicted Anomaly) 0     1621      1                      
   (Predicted Anomaly) 1     1         1                      




- cpc_2 dataset:            (Actual Anomaly)                - cpc_3 dataset:            (Actual Anomaly)                 - cpc_4 dataset:            (Actual Anomaly) 
                             0    |    1                                                  0   |   1                                                    0   |   1
   (Predicted Anomaly) 0    1611       0                      (Predicted Anomaly) 0      1480     1                        (Predicted Anomaly) 0      1536     0
   (Predicted Anomaly) 1    12         1                      (Predicted Anomaly) 1      55       2                        (Predicted Anomaly) 1      104      3

- cpm_2 dataset:            (Actual Anomaly)               - cpm_3 dataset:            (Actual Anomaly)                 - cpm_4 dataset:            (Actual Anomaly) 
                             0    |    1                                                  0   |   1                                                    0   |   1
   (Predicted Anomaly) 0     1621      1                      (Predicted Anomaly) 0       1535    0                        (Predicted Anomaly) 0       1623    1
   (Predicted Anomaly) 1     1         1                      (Predicted Anomaly) 1       2       1                        (Predicted Anomaly) 1       16      3
