import subprocess

#This file was written by Weston Odom and was used for debugging purposes.

class TreeViz:
    def __init__(self, filename, parse_tree):
        self.tree = parse_tree
        self.dotfile = filename + ".dot"
        self.image_file = filename + ".png"
        self.i = 0

    def viz(self):
        f = open(self.dotfile, "w")
        f.write("digraph Lexeme {\n")
        f.write("\tnode [shape=record];\n")
        if not self.tree:
            f.write("\tNo Parse Tree\n")
        else:
            self.viz_helper(f, self.tree)
        f.write("}\n")
        f.close()

    def viz_helper(self, stream, node):
        stream.write(
            '\t{0} [label="<f0> left| <f1> token_type = {1} | <f2> value = {2} | <f3> right"];\n'.format(
                id(node),
                node.name,
                node.value
                )
            )
        if node.left:
            stream.write('\t{0}:f0 -> {1};\n'.format(id(node), id(node.left)))
            self.viz_helper(stream, node.left)
        else:
            stream.write('\t{0}:f0 -> {1};\n'.format(id(node), str(node.left) + str(self.i)))
            self.i += 1
        if node.right:
            stream.write('\t{0}:f3 -> {1};\n'.format(id(node), id(node.right)))
            self.viz_helper(stream, node.right)
        else:
            stream.write('\t{0}:f3 -> {1};\n'.format(id(node), str(node.right) + str(self.i)))
            self.i += 1

    def create_image(self):
        subprocess.call(["dot", "-Tpng", self.dotfile, "-o", self.image_file])

    def open_image(self):
        subprocess.call(["open", self.image_file])

