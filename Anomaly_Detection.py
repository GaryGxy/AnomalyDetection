import pandas as pd
import Anomaly_Detection_Module as adm
import yaml

# Load in parameters from yaml file
with open('parameter.yaml') as file:
    parameter_list = yaml.load(file, Loader=yaml.FullLoader)
cpc_percentage = parameter_list["cpc parameters"]["percentage"]
cpc_threshold = parameter_list["cpc parameters"]["threshold"]
cpm_percentage = parameter_list["cpm parameters"]["percentage"]
cpm_threshold = parameter_list["cpm parameters"]["threshold"]
# Load in the datasets
cpc1 = pd.read_csv("exchange-2_cpc_results.csv")
cpc2 = pd.read_csv("exchange-3_cpc_results.csv")
cpc3 = pd.read_csv("exchange-4_cpc_results.csv")
cpm1 = pd.read_csv("exchange-2_cpm_results.csv")
cpm2 = pd.read_csv("exchange-3_cpm_results.csv")
cpm3 = pd.read_csv("exchange-4_cpm_results.csv")
# List the abnormal data points
cpc1_outlier = ["2011-07-14 13:00:01"]
cpc2_outlier = ["2011-07-14 10:15:01", "2011-07-20 10:15:01", "2011-08-13 10:15:01"]
cpc3_outlier = ["2011-07-16 09:15:01", "2011-08-02 12:15:01", "2011-08-23 08:15:01"]
cpm1_outlier = ["2011-07-26 06:00:01", "2011-08-10 17:00:01"]
cpm2_outlier = ["2011-08-19 18:15:01"]
cpm3_outlier = ["2011-07-16 09:15:01", "2011-08-01 07:15:01", "2011-08-23 08:15:01", "2011-08-28 13:15:01"]
# Label the dataset
cpc1["Label"] = [1 if t in cpc1_outlier else 0 for t in cpc1["timestamp"]]
cpc2["Label"] = [1 if t in cpc2_outlier else 0 for t in cpc2["timestamp"]]
cpc3["Label"] = [1 if t in cpc3_outlier else 0 for t in cpc3["timestamp"]]
cpm1["Label"] = [1 if t in cpm1_outlier else 0 for t in cpm1["timestamp"]]
cpm2["Label"] = [1 if t in cpm2_outlier else 0 for t in cpm2["timestamp"]]
cpm3["Label"] = [1 if t in cpm3_outlier else 0 for t in cpm3["timestamp"]]
outlier_cpc1 = adm.anomaly_detect(cpc1, cpc_percentage, cpc_threshold)
adm.summary(outlier_cpc1)
outlier_cpc2 = adm.anomaly_detect(cpc2, cpc_percentage, cpc_threshold)
adm.summary(outlier_cpc2)
outlier_cpc3 = adm.anomaly_detect(cpc3, cpc_percentage, cpc_threshold)
adm.summary(outlier_cpc3)
outlier_cpm1 = adm.anomaly_detect(cpm1, cpm_percentage, cpm_threshold)
adm.summary(outlier_cpm1)
outlier_cpm2 = adm.anomaly_detect(cpm2, cpm_percentage, cpm_threshold)
adm.summary(outlier_cpm2)
outlier_cpm3 = adm.anomaly_detect(cpm3, cpm_percentage, cpm_threshold)
adm.summary(outlier_cpm3)
