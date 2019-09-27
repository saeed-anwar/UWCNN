python = 3.5
tensorflow =1.0.0

Test

1. Download the trained models and place them in 'checkpoint/coarse_230/'
2. Choose the needed model (For example, if you need the type 1 model, please put 'model_checkpoint_path: "coarse.model-type1"' on the first line of checkpoint text.)
3. Put the testing images into 'test_real'
4. Python main_test.py
5. Find the results in 'test_real'