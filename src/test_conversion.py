def to_str(bytes_to_str):
	if isinstance(bytes_to_str,bytes):
		value = bytes_to_str.decode('utf-8')
	else:
		value = bytes_to_str
	return value


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))			

print(b'one' + b'two')
print('one' + 'two')

assert b'red' > b'blue'
assert 'red' > 'blue'
print(b'foo' == 'foo')

print (b'red %s' % b'blue')
print ('red %s' % 'blue')