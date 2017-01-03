import os, time
import zipfile

def fileignore(file):
	list = [".blend1", ".blend2", ".blend3", ".blend4", ".blend5", ".pyc", "ehthumbs.db", "~", "__pycache__"]
	for l in list:
		if file.endswith(l): return True

def zipdir(path, ziph):
	# ziph is zipfile handle
	for root, dirs, files in os.walk(path):
		for file in dirs + files:
			if not fileignore(file): ziph.write(os.path.join(root, file))
			
if __name__ == '__main__':

	#Update version date
	lines = []
	with open("addon/community/macro.py", 'r') as f:
		for line in f.readlines():
			if line.startswith("VERSION"):
				line = "VERSION = " + time.strftime("%y%m%d")
			lines.append(line)
	
	with open("addon/community/macro.py", 'w') as f:
		for line in lines: f.write(line)
		
	
	#data.zip
	zipf = zipfile.ZipFile('addon/community/data.zip', 'w', zipfile.ZIP_DEFLATED)
	zipdir('project/', zipf)
	zipf.write('project.json')
	zipf.close()
	
	#CommunityAddon.zip
	os.chdir("addon/")
	zipf = zipfile.ZipFile('CommunityAddon.zip', 'w', zipfile.ZIP_DEFLATED)
	zipdir('community/', zipf)
	zipf.close()
	os.chdir("../")