## Note:
* result download:https://drive.google.com/drive/folders/1dwY-tlhUNDKUZYTRSR3YgKpBO1eD6Q2i?usp=share_link
## Note:
* `nntools.py` is Neural Network tools developed for UCSD ECE285 MLIP. Copyright 2019. Charles Deledalle, Sneha Gupta, Anurag Paul, Inderjot Saggu.

* should create a folder called dataset and download BSD300 folder（including train_data and test_data） into "dataset"from [Google]: https://drive.google.com/drive/folders/1F0_w4z8ImdzGTwJe3Ajy4ax2Ew58aLg_?usp=sharing
* any zip or 7z of train and test data should unpack and put into dataset folder and change root_dir in `argument.py`:

  ```
  --root_dir='../dataset/BSD300/images'
  ```

## Test:
  ```
python /model/test.py
  ```
* `test.py`is a demo for test ,you can set path of the test pictures and saved pictures at In29:
  ```
  file_root = '../test/try/'
  save_out = "../test/tryout/" 
  ```

* should create a folder called "test" and put valid_image into test folder,you can get final pics in folder "outputpic"

  
