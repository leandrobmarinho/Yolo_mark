import argparse, glob, os, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, help="images path to write in the file")
parser.add_argument("-t", "--percentage", type=float, help="percentage for training")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")


args = parser.parse_args()

if args.path:
	files = glob.glob(os.path.join(args.path, '*.jpg'))
	np.random.shuffle(files)

	if files:

		file = open("train.txt","w") 

		for filename in files:
			filename = "data/img/{}".format(os.path.basename(filename))
			if args.verbose:
			    print("writing '{}'".format(filename))

			file.write("{}\n".format(filename))

		file.close()
		print("done")

	else:
		print("No images")