import re
def is_gsm(num):
	"""Very flexible, accepts a number of white spaces. Also allows unorthodox representations such as '0888777 555' or '0888 555777.'"""

	reg = '(\+359( )?|00( )?359( )?|0)8(7|8|9)\d( )?\d{3}( )?\d{3}'
	if re.match(reg, str(num)):
		print(f'{num} is a valid number')
		return True
	else:
		print(f'{num} is not valid number')
		return False
