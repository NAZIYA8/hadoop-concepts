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
