import sys


def main():
    if len(sys.argv) < 2:
        print("please using the command line as 'python vtk_cfm2vtk_gmsh.py filename.vtk'")
        exit(1)
    filename = sys.argv[1]
    fi = open(filename, "r")
    fn = filename.split(".")
    fo = open("gmsh_"+str(fn[0])+".vtk", "w")

    cell_num = int()
    while True:
        line = fi.readline()
        if not line:
            break
        if line.startswith("DATASET"):
            line = "DATASET UNSTRUCTURED_GRID" + "\n"
        if line.startswith("LINES"):
            line = ""
        if line.startswith("2"):
            line = ""
        if line.startswith("POLYGONS"):
            line_list = line.split()
            line_list[0] = "CELLS"
            cell_num = int(line_list[1])
            line = " ".join(line_list) + "\n"
        fo.write(line)

    fo.write("CELL_TYPES"+" "+str(cell_num)+"\n")
    for index in range(cell_num):
        fo.write("5\n")
    fi.close()
    fo.close()


if __name__ == "__main__":
    main()
