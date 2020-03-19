import getopt
import json
import sys
import src.OPCV.api as api
import datetime

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
			
    index_name = "nyctickets"
    es = api.create_index(index_name)
    idx = 1
    for r in res:
        print(f"Loaded {idx} record")
        r['issue_date'] = datetime.datetime.strptime(r['issue_date'], "%m/%d/%Y")
        es.index(index=index_name, doc_type='violation', id=idx, body=r)
        idx += 1
        
    print(f"Loaded {idx} records into ES")
	
	
	
		
				
