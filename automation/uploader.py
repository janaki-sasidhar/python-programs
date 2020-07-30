import os,sys,pyperclip

def main():
	try:
		file_name=sys.argv[1]
	except Exception as e:
		print(e)
		file_name=input("Enter the file name -> ...")
	command=f"curl -F 'file=@{file_name}' http://0x0.st"
	print("Uploading the file ",file_name," to 0x0.st")
	a=os.popen(command).read()
	print(" -"*10)
	print("The link to the uploaded file is \n ",a)
	pyperclip.copy(a)
	print("The link has been copied to your clipboard ")
	
if __name__ == "__main__":
	main()
