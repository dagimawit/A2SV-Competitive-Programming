class Solution(object):
    def interpret(self, command):
        comman_list = ['G', 'o', 'al']
        command = command.replace("()", "o").replace("(al)", "al").replace("G", "G")
        return command