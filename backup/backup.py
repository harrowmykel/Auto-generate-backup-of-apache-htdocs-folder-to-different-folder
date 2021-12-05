import os
import time
import datetime

#this file tries to perform an automatic backup of
#the html folder

#formatted time '16-May-2011_02-45-PM'
now_time = datetime.datetime.now().strftime('%d-%b-%G_%I-%M-%p')

# end in /
root_folder = "./.."
html_folder = root_folder + "/html"
backup_folder = root_folder + "/backup"
dest_backup_folder = backup_folder + "/backup_" + now_time

# create destination folder
os.system("mkdir " + dest_backup_folder)

# go to html folder and run commit
os.system("cd " + html_folder)
os.system("git add .")
os.system("git commit -m 'new changes at " + now_time + " ' ")

#copy all files and folders to backup folder 
for name in os.listdir(html_folder):
	if name != ".git" and name != "." and name != "..":
		os.system("cp -r '" + html_folder + "/" + name +"' '" + dest_backup_folder+ "/" + name + "'")

#delete .git folder in new backup
#os.system("rm -R " + dest_backup_folder + "/.git")

#zip folder 
os.system("zip -r " + dest_backup_folder + ".zip " + dest_backup_folder)


#delete new backup folder
os.system("rm -R " + dest_backup_folder)