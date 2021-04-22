import sys 

results = sys.argv[1]

files = open(results, 'r')

accuracy = []
roc = []

for line in files:

	if line.startswith("Accuracy:"):
		accuracy.append(float(line.split(" ")[1][:-1]))
	else:
		roc.append(float(line.split(" ")[1]))

print("Accuracy score mean: {}".format(sum(accuracy)/len(accuracy)))
print("Roc-auc score mean: {}".format(sum(roc)/len(roc)))

