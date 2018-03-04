import csv

#Definitions...
bindeffilename = ''
infilename = ''
outfilename = ''
infile_xcol = 0
infile_ycol = 1
infile_valcol = 2
outfile_headerline = 'class,modsin_x,modsin_y,agbv8a,category'

#--------End of Definitions------------

print("Reading bin definition file:", bindeffilename)

bins = []

with open(bindeffilename, 'r') as infile:
	reader = csv.reader(infile, delimiter=',')
	for row in reader:

		#Bin Definition file format:
		#columns : bin name, bin minimum, bin max, n_elements, sum of elements, bin average
		
		print(','.join(row) + '\n')
		current_bin = (row[0], float(row[1]), float(row[2]), int(row[3]), float(row[4]), float(row[5]))
		print("Bin read with name:", current_bin[0], " min:", current_bin[1], " max:", current_bin[2], " n_elements:", current_bin[3], " sum of elements:", current_bin[4], " bin average:", current_bin[5])

		bins.append(current_bin)


with open(infilename, 'r') as infile:
	with open(outfilename, 'w') as outfile:

		outfile.write(outfile_headerline + '\n')

		print("Processing training points...")

		reader = csv.reader(infile, delimiter=',')
		header = next(reader)

		print("X column:", header[infile_xcol], " Y column:", header[infile_ycol], " Value column:", header[infile_valcol])

		for row in reader:
			xcoord = row[infile_xcol] #don't convert to number to avoid losing precision
			ycoord = row[infile_ycol] #don't convert to number to avoid losing precision

			value = float(row[infile_valcol])
			#Find which bin this point belongs in
			for i in range(0,len(bins)):
				binmin = (bins[i])[1]
				binmax = (bins[i])[2]
				if ((value >= binmin) and (value < binmax)):
					outfile.write((bins[i])[0] + ',' + xcoord + ',' + ycoord + ',' + row[infile_valcol] + ',' + str(i) + '\n')
					break
