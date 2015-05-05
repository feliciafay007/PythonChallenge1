import os
class TraverseCurrentDir :
    def files_in_cur_dir(self, input_dir) :
        current_files = []
        files = []
        if input_dir == '/'  or input_dir == '' :
            files = os.listdir(os.curdir) 
            for f in files:
                if not f.startswith('.'):
                    current_files.append(f)
            RESULT_OK = 0
        else:
            current_path = os.path.dirname(os.path.realpath(__file__))
            current_path = current_path + "/" + input_dir
            if (os.path.isdir(current_path) or os.path.isfile(current_path)) :
                files = os.listdir(current_path)
            #else :
            #    files = os.listdir(os.curdir)
            for f in files:
                if not f.startswith('.') :
                    current_files.append(f)
            RESULT_OK = -1
        return RESULT_OK, current_files

