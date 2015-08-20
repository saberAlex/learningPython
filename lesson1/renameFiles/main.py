import os

def rename_file():
	#find the file name of the folder
	fileList = os.listdir(r"./")
	print(fileList)
	print(os.getcwd())
	os.chdir(r"/home/luca/programming/PythonBasic/lesson1/renameFiles")
	for fileName in fileList:
		#remove the number and rename the file.. 
		newFileName = fileName.translate(None,"0123456789")
		os.rename(fileName,newFileName)

rename_file()