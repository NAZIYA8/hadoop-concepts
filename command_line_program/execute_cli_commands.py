'''
@Author: Naziya
@Date: 2021-08-19
@Last Modified by: Naziya
@Last Modified : 2021-08-19
@Title : Program Aim is to execute hadoop cli commands
'''

import subprocess

def run_command(args_list):
	print("Running system command: {}".format(" ".join(args_list)))
	proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	s_output = proc.communicate()
	return s_output

if __name__ == "__main__":
	cmd = run_command(['hdfs','dfs','-mkdir','/testdir'])
	cmd = run_command(['hdfs','dfs','-put','/home/naziya/Desktop/input.txt','/test'])
	cmd = run_command(['hdfs','dfs','-ls','/'])
	cmd = run_command(['hdfs','dfs','-cp','/mydir1/input.txt','/testdir'])
	cmd = run_command(['hdfs','dfs','-ls','/testdir'])
	cmd = run_command(['hadoop','version'])
	print(cmd)

