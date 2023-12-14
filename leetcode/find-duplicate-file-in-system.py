class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_info = {}
        for path in paths:
            spath = path.split(" ")
            dpath =spath[0]
            files =spath[1:]
            for file in files:
                fname,fcontent =file.split("(")
                fcontent =fcontent[:-1]

                if fcontent not in file_info:
                    file_info[fcontent] = []
                file_info[fcontent].append(dpath + "/"+fname)
        output= []
        for files in file_info.values():
            if len(files) >1:
                output.append(files)
        return output
        

        