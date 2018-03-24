import zipfile

def execute(zip_file):
	with zipfile.ZipFile(zip_file + '.zip','r') as zip_ref:
		zip_ref.extractall(zip_file + 'Unzip')