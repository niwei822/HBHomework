log_file = open("um-server-01.txt")


def generate_sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


generate_sales_reports(log_file)
#mv: move and rename
#can move accross directories
#cp: copy
#rm: remove files
#~ home directory
#cd ~/src
#output <
#echo "new content" > existing file(redirecting output to a file)
#pip3 freeze > requirements.txt
#echo "new content" >> file(append to a file)
#redirect input <
#python3 python.py < file > outfile
#pipelines cat file | python3 python.py
