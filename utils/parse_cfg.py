from configparser import ConfigParser
import sys

def read_config(fpath):
	'''This function reads a configuration file and returns an equivalent dictionary'''

	config = ConfigParser()  #.SafeConfigParser() from python 3.2 SageConfigParser has been renamed to ConfigParser
	with open(fpath, 'r') as fid:
		config.read_file(fid)
	return config._sections

if __name__ == '__main__':
	if len(sys.argv) < 2:
		quit('usage: {} "file.cfg"'.format(sys.argv[0]))

	print(read_config(sys.argv[1]))
