"""
Quick plotting tool meant to be used with GnuCap
"""

import argparse
import matplotlib.pyplot as plt

def main():
	# Argument parsing
	parser = argparse.ArgumentParser(description="Plot something")
	parser.add_argument("in_path", nargs="+", type=str, 
        help="Path (or paths) to plot data")
	parser.add_argument("--out", default="grafica.png",
        type=str, help="Path to output PNG, defaults to \"grafica.png\"")
	parser.add_argument("--ylabel", type=str, default="")
	parser.add_argument("--xlabel", type=str, default="")
	parser.add_argument("--xlog", type=bool, default=False)
	parser.add_argument("--ylog", type=bool, default=False)
	parser.add_argument("--title", type=str, default="")
	parser.add_argument("--labels", type=str, default="_",
		help="The legends of the plots separated by \";\"")
	args = parser.parse_args()

	labels = args.labels.split(";")
	if len(labels) != len(args.in_path):
		print("Error: Every plot must have a legend.")
		return
	xlog = args.xlog
	ylog = args.ylog

	# Plot
	if (xlog):
		plt.xscale('log')
		plt.grid(True, which="minor", axis="x", linestyle="--")
	if (ylog):
		plt.yscale('log')
		plt.grid(True, which="minor", axis="y", linestyle="--")
	plt.grid()
	plt.xlabel(args.xlabel)
	plt.ylabel(args.ylabel)
	plt.title(args.title)

	for L, path in enumerate(args.in_path):
		with open(path, "r") as f:
			rawdata = [ [float(i) for i in line.split()] 
					   for line in f.readlines()[1:-1] ]
			x = [ i[0] for i in rawdata ]
			y = [ i[1] for i in rawdata ]

		plt.plot(x, y, label=labels[L])

	if len(labels) > 1:
		plt.legend()
		
	plt.savefig(args.out)

	print("Plot saved correctly")

	return

if __name__ == "__main__":
	main()

