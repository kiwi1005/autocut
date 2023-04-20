import sys
import os
import glob

def preprocess(input_dir):
    process_list = []
    process_list = glob.glob(os.path.join(input_dir,"*.mp4"))
    print(process_list)
    
    for process in process_list:
        print(process)
        os.system('autocut --whisper-model medium -t "./%s" ' % process  ) 
    
    
if __name__ == "__main__":
    preprocess(sys.argv[1])