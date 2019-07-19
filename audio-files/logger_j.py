import logging

def j_log(typ,s):
	value_file = open('active.value','r')
	v_f_read = value_file.read()
	value  = v_f_read.split()
	if value[0] == 'True':
		active = True
	else :
		active = False
	print('active_2= '+str(active))
	if active :
		if typ == 'info':
			return logging.info(s)
		if typ == 'error':
			return logging.error(s)
		if typ == 'warning':
			return logging.warning(s)
	else:
		return 

