from json 	 import dump
from math    import ceil
from os      import listdir
from os.path import basename, normpath, isfile, join
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
	input_dir, out_dir, html_dir = argv[1:]
	split = 'by_slice_num'
	slice_sets = [20, 50, 100, 200, 300, 400, 500]

	for num in slice_sets:
		slice_list = gen_slice_list(input_dir, split=split, num=float(num))
		print(len(slice_list))
		manifest_dict = gen_manifest(html_dir, slice_list)
		file = join(out_dir, basename(normpath(input_dir)) + "_" + str(num) + "_slices.json")
		with open(file, 'w') as write_file:
			dump(manifest_dict, write_file)


	



