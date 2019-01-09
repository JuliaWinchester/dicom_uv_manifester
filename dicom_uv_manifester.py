from json 	 import dump
from math    import ceil
from os      import listdir
from os.path import isfile, join
from sys     import argv

# Take in a directory name of .dcm files and export the desired number of manifest files, with options being an integer or 'log'

def gen_slice_list(input_dir, split='by_slice_num', num=200):
	dicom_list = [x for x in listdir(input_dir) if isfile(join(input_dir, x)) and (x.lower().endswith('.dcm') or x.lower().endswith('.dicom'))]
	
	if split == 'by_slice_num':
		step = ceil(len(dicom_list)/num)
	elif split == 'by_percent':
		step = ceil(1/num)
	# todo log 

	return dicom_list[::step]

def gen_manifest(html_dir, slice_list):
	return { 'baseurl': html_dir, 'series': slice_list }

if __name__ == '__main__':
	input_dir, html_dir, split, num, file = argv[1:]
	
	slice_list = gen_slice_list(input_dir, split=split, num=float(num))
	print(len(slice_list))
	manifest_dict = gen_manifest(html_dir, slice_list)

	with open(file, 'w') as write_file:
		dump(manifest_dict, write_file)

