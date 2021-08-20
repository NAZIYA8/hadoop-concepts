# hadoop-concepts

# WORD COUNT PROBLEM

STEP 1: Create input5.txt file by writing command in the terminal
$ mkdir word_count    #Creating a directory
$ cd word_count    # getting inside word_count folder
$ touch input5.txt    # creating input5.txt file
$ nano input5.txt    # editing file and adding data
$ cat input5.txt        # viewing the file

Then create mapper.py and reducer.py file using the same process for implementing mapper and reducer tasks. Write the code.

STEP 2: Start the hadoop script
$ start-all.sh

STEP 3: Create a folder on hdfs
$ hdfs dfs -mkdir /Demo_word_count

STEP 4: put the input5.txt file inside the hdfs Demo_word_count folder
hdfs dfs -put /home/naziya/hadoop-concepts/word_count/input5.txt /Demo_word_count

STEP 5: Now execute the map reduce program.
hadoop jar /home/naziya/Downloads/hadoop-streaming-2.7.3.jar \
-file /home/naziya/hadoop-concepts/word_count/mapper.py -mapper 'python3 mapper.py' \
-file /home/naziya/hadoop-concepts/word_count/reducer.py -reducer 'python3 reducer.py' \ 
-input /Demo_word_count/input5.txt \
-output /Demo_word_count/output5

We can check the results manually by visiting the location in HDFS or with the help of cat command
hdfs dfs -cat /Demo_word_count/output5/part-00000


# MATRIX MULTIPLICATION PROBLEM

STEP 1: Create matrix.txt file by writing command in the terminal
$ mkdir matrix_multiplication    #Creating a directory
$ cd matrix_multiplication    # getting inside matrix_multiplication folder
$ touch matrix.txt        # creating matrix.txt file
$ nano matrix.txt        # editing file and adding data
$ cat matrix.txt            # viewing the file


Then create mapper.py and reducer.py file using the same process for implementing mapper and reducer tasks. Write the code.


STEP 2: Start the hadoop script
$ start-all.sh


STEP 3: Create a folder on hdfs
$ hdfs dfs -mkdir /Demo_matrix_multiplication


STEP 4: Put the matrix.txt file inside the hdfs Demo_matrix_multiplication folder

hdfs dfs -put /home/naziya/hadoop-concepts/matrix_multiplication/matrix.txt /Demo_matrix_multiplication


STEP 5: Now execute the map reduce program.

hadoop jar /home/naziya/Downloads/hadoop-streaming-2.7.3.jar \
-file /home/naziya/hadoop-concepts/matrix_multiplication/mapper.py -mapper 'python3 mapper.py' \
-file /home/naziya/hadoop-concepts/matrix_multiplication/reducer.py -reducer 'python3 reducer.py' \ 
-input /Demo_matrix_multiplication/input5.txt \
-output /Demo_matrix_multiplication/output6


We can check the results manually by visiting the location in HDFS or with the help of cat command
hdfs dfs -cat /Demo_matrix_multiplication/output6/part-00000


# WORD LENGTH COUNT PROBLEM

STEP 1: Create word.txt file by writing command in the terminal
$ mkdir word_length    #Creating a directory
$ cd word_length    # getting inside word_length folder
$ touch word.txt    # creating word.txt file
$ nano word.txt    # editing file and adding data
$ cat word.txt        # viewing the file


Then create mapper.py and reducer.py file using the same process for implementing mapper and reducer tasks. Write the code.

STEP 2: Start the hadoop script
$ start-all.sh

STEP 3: Create a folder on hdfs
$ hdfs dfs -mkdir /Demo_word_length

STEP 4: put the input5.txt file inside the hdfs Demo_word_length folder
hdfs dfs -put /home/naziya/hadoop-concepts/word_length/word.txt /Demo_word_length

STEP 5: Now execute the map reduce program.
hadoop jar /home/naziya/Downloads/hadoop-streaming-2.7.3.jar \
-file /home/naziya/hadoop-concepts/word_length/mapper.py -mapper 'python3 mapper.py' \
-file /home/naziya/hadoop-concepts/word_length/reducer.py -reducer 'python3 reducer.py' \ 
-input /Demo_word_length/word.txt \
-output /Demo_word_length/output7

We can check the results manually by visiting the location in HDFS or with the help of cat command
hdfs dfs -cat /Demo_word_length/output7/part-00000

