

a = [1,2,3,'sashant','pardeshi'];

print a[3]

firstname = 'sashant'

print firstname

checkboxes = ['turbo','power','energy','exorbitant']
checked = set()
unchecked = set()

bu_names = {'bigrock':1,'resellerclub':1,'logicboxes':0}


for k,v in bu_names.iteritems():
	
	print k , v	
	
	if v == 1 :
		print k
		checked.add(k)
		# print checked.count(k)
		# if checked.count(k) == 0 :
		# 	checked.append(k)
	elif v == 0 :
		print k
		unchecked.add(k)
		# if unchecked.count(k) == 0 :
		# 	unchecked.append(k)

# checked.sort()
# unchecked.sort()

print ''.join(checked)
print ''.join(unchecked)


			