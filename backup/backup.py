import os
import time
import datetime

#this file tries to perform an automatic backup of
#the html folder

#formatted time 'May-16-0245PM-2011'
now_time = datetime.datetime.now().strftime('%b-%d-%I%M%p-%G')

# end in /
root_folder = "./.."
html_folder = root_folder + "/html"
backup_folder = root_folder + "/backup"
dest_backup_folder = backup_folder + "/backup_" + now_time

# create destination folder
os.system("mkdir " + dest_backup_folder)

# go to folder
os.system("cd " + html_folder)

#git commit
os.system("git add .")
os.system("git commit -m 'new changes at " + now_time + " ' ")

#copy to backup folder 
os.system("cp " + html_folder + "/ " + dest_backup_folder)
os.system("cp " + html_folder + "/* " + dest_backup_folder)
os.system("cp " + html_folder + "/.* " + dest_backup_folder)

#delete .git folder in new backup
os.system("rm -R " + dest_backup_folder + "/.git")

#zip folder 
os.system("zip -r " + dest_backup_folder + ".zip " + dest_backup_folder)


#delete new backup folder
os.system("rm -R " + dest_backup_folder + "/.git")