import os
class TraverseCurrentDir :
    def files_in_cur_dir(self, input_dir) :
        current_files = []
        RESULT_OK = 0
        if input_dir == '/'  or input_dir == '' :
            files = os.listdir(os.curdir) 
            for f in files:
                if not f.startswith('.'):
                    current_files.append(f)
        else:
            current_path = os.path.dirname(os.path.realpath(__file__))
            current_path = current_path + "/" + input_dir
            if (os.path.isdir(current_path) or os.path.isfile(current_path)) :
                files = os.listdir(current_path)
                for f in files:
                    if not f.startswith('.') :
                        current_files.append(f)
            else:
                RESULT_OK = -1
        return RESULT_OK, current_files
    
    def files_and_links_in_cur_dir(self, input_dir) :
        current_files = []
        current_links = []
        RESULT_OK = 0
        if input_dir == '/'  or input_dir == '' : 
            current_path = os.path.dirname(os.path.realpath(__file__))
            files = os.listdir(os.curdir) 
            for f in files:
                if not f.startswith('.'):
                    current_files.append(f)
                    #print "TEST1", current_path, f
                    if (os.path.isdir(current_path +  "/" + f)):
                        current_links.append(current_path + "/" + f)
                    else :
                        current_links.append('-')
        else:
            current_path = os.path.dirname(os.path.realpath(__file__))
            current_path = current_path + "/" + input_dir
            if (os.path.isdir(current_path) or os.path.isfile(current_path)) :
                files = os.listdir(current_path)
                for f in files:
                    if not f.startswith('.') :
                        current_files.append(f)
                        if (os.path.isdir(current_path + "/" + f)):
                            current_links.append(current_path + "/" + f)
                        else :
                            current_links.append('-')
            else:
                RESULT_OK = -1
        return RESULT_OK, current_files, current_links


