import getopt
import json
import sys
import src.OPCV.api as api

if __name__ == "__main__":
	page_s = 1000
	num_p = 0
	fn = None 	
	
	options, remainder = getopt.getopt(sys.argv[1:],'',['page_size=','num_pages=','output='])
	for opt, arg in options:
		if opt == '--page_size':
			page_s = arg
		elif opt == '--num_pages':
			num_p = int(arg)
			if num_p <=0:
				raise Exception("num_pages should larger than 0") 
		elif opt == '--output':
			fn = arg
	if num_p <= 0:
		res = api.get_data(page_s)
	else:
		res = []
		for i in range(num_p):
			r = api.get_data(page_s, i)
			res.extend(r)
		
	if fn is None:
		for line in res:
			print(json.dumps(line))
	else:		
		with open(fn, "w") as fw:
			for line in res:
				fw.write(json.dumps(line))
				fw.write('\n')
				
