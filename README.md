## Note:
* `nntools.py` is Neural Network tools developed for UCSD ECE285 MLIP. Copyright 2019. Charles Deledalle, Sneha Gupta, Anurag Paul, Inderjot Saggu.

* should download BSD300 folder（including train_data and test_data）from 

  [Google]: https://drive.google.com/drive/folders/1F0_w4z8ImdzGTwJe3Ajy4ax2Ew58aLg_?usp=sharing

* `test.ipynb`is a demo for test ,you can set path of the test pictures and saved pictures at In29:

  ```
  file_root = '../test/try/'
  save_out = "../test/tryout/" 
  ```

* should put valid_image into test folder.

* ```
  https://drive.google.com/file/d/1QLxZw99zn1hjx2ivgN9VqaRU4m1kyO0v/view?usp=share_link
  wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=FILEID" -O FILENAME && rm -rf /tmp/cookies.txt
  ```

  

* any zip or 7z of train and test data should unpack and put into dataset folder and change root_dir in `argument.py`:

  ```
  --root_dir='../dataset/BSD300/images'
  ```

  
