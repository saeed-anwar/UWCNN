### Requirements
python = 3.5
tensorflow =1.0.0
scipy = 1.1.0 (required)
Tested with python=3.6 and Tensorflow=1.14.0
### Quick start

1. The trained models are in 'checkpoint/coarse_230/'
2. Choose the needed model (For example, if you need the type 1 model, please put 'model_checkpoint_path: "coarse.model-type1"' on the first line of checkpoint text.)
3. Put the test images into 'test_real'

   **Use the following to test the algorithm**

    ```
    Python main_test.py
    ```
4. Find the results in 'test_real'
