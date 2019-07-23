
#v1
if value[0] == 'True':
		f= open(path, 'r')
		f_read= f.read()
		f2_r= f_read.split()
		i = len(f2_r) -1 
		while True:

			if f2_r[i] == s:
				f.close()
				return True
			elif f2_r[i] == "=======================================" and i != len(f2_r) -1:
				f.close()
				return False
			i-=1
	else:
		return 


#v2
start = int(dt.datetime.now().strftime("%s")) # gets the current time in seconds 
		f= open(path, 'r')
		
		# get file size and moves to backline
		f_size = os.stat(filename)[6] - backline
		# set current position to said backline
		f.seek(st_size)

		delta_time = 0
		timeout = (t if type(t)==int else t_file)
		while 1:
			now = int(dt.datetime.now().strftime("%s"))
			delta = now - start
			left = timeout - delta
			# if timeout
			if int(delta) > timeout:
				logging.error('PATTER NOT FOUND, TRY AGAIN')
				f.close()
				return False

			if int(delta)%1 == 0 and delta_time != delta:
				logging.warning("[LOOKING FOR "+ s +" time left : "+ str(left) + " sec ]")
				delta_time = delta

			where = file.tell()
			line = file.readline()

			# In case no line is reached 
			if not line:
				time.sleep(0.1)
				file.seek(where)

		# Seek for the log in the line
		else:
			logging.debug(line.rsplit("\n"))
			searchObj = re.search(r'' + log + '', line, re.M | re.I)
			if searchObj:
				logging.info("PATTERN FOUND IN : " + line)
				file.close()
				return True