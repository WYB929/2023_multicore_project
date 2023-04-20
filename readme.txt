All our code could be run on the CIMS crunchy1 server

For generating dataset(generate_dataset.py):

generate_dataset.py ---> dataset.csv
Remark: a ---> b means output file b after execution of file a

Please install Parsec 3.0 first by following instructions here: https://parsec.cs.princeton.edu/parsec3-doc.htm
In terminal, use cd commend to go to the root directory of Parsec 3.0, then run python3 generate_dataset.py to collect data.
NOTICE: This commends might take 7 to 8 hours to run.



The rest of sources code are written in jupyter notebook file, all package used in the files are available on CIMS crucnhy 1 server.
You can directly run these files with jupyter notebook and see the output.

Here are guidelines for code review:

Baseline Models Creation and Evaluation:
baseline_models.ipynb
vanilla_net.ipynb

Data Preprocessing and Feature Selection:
data_preprocessing.ipynb ---> preprocessed_data.csv
ts_tp_overhead_feature_selection.ipynb ---> dataset_s.csv
                                            dataset_p.csv

Sub-models Creation and Evaluation for TSTP Model:
overhead_model.ipynb also create an advanced version of preprocessed dataset with T_s and T_p

overhead_model.ipynb ---> preprocessed_data_s_p_speedup.csv
                     ---> overhead_model.joblib
SNet.ipynb ---> SNet.pt
PNet.ipynb ---> PNet.pt

TSTP Model Creation and Evaluation:
TSTP_model.ipynb

If you have any question about running the code, please reach out Yibin Wang (yw4145@nyu.edu).
