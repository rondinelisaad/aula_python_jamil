"""

"""
import sys

def dictify_logline(line):
    """
    Retornará um dicionário com partes do arquivo que nos interessa.
    Aparentemente o que nos interessa desse arquivo são: datetime,
    loglevel e message
    """
    line_stripped = line.strip('\n')
    split_line = line_stripped.split(']')
    return {
        "datetime": split_line[0].strip(' ['),
        "logleve": split_line[1].strip(' ['),
        "message": split_line[2].strip(' ['),
    }

def generate_log_report(logfile):
    report_dict = {}
    for line in logfile:
        line_dict = dictify_logline(line)
        print(line_dict)
        
if __name__ == "__main__":
    infile = open("apache.log")
    
log_report = generate_log_report(infile)
print(log_report)
#print(log_report)
# print(dictify_logline("[Sun Dec 04 04:52:05 2005] [notice] \
    # jk2_init() Found child 6737 in scoreboard slot 8"))