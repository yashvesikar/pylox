from typing import *

class GenerateAST:
    def __init__(self, args:List)->None:
        """
        Should provide one argument - the output directory
        :param args:
        """
        assert len(args) == 1

        output_dir = args[0]
        self.define_AST(output_dir, "Expr", {"Binary" : ["Expr left", "Token operator", "Expr right"],
                                             "Grouping": ["Expr expression"],
                                             "Literal" : ["Object value"],
                                             "Unary"   : ["Token operator", "Expr right"]
                                            })


    def define_AST(self, output_dir:str, base_name:str, types:Dict):
        """
        Meta-program to automate AST Node generation
        :param output_dir: Output directory of the file
        :param base_name: name of the base class
        :param types: types of grammar rules to implement
        :return:
        """
        path = f"{output_dir}/{base_name.lower()}.py"
        with open(path, 'w') as fp:
            fp.writelines(["from abc import ABC, abstractmethod\n\n",
                           f"class {base_name}(ABC):\n\n",
                           f"\tdef __init__(self):\n",
                           "\t\tpass\n\n"
                           ])

            fp.writelines(["\n",
                               "\t@abstractmethod\n",
                               "\tdef accept(self, visitor):\n",
                               "\t\tpass\n\n"])

            self.define_visitor(fp, base_name, types)


            for class_name, fields in types.items():
                self.define_type(fp, base_name, class_name, fields)
                fp.write("\n")

            fp.writelines(["\n",
                           ""])




    def define_type(self, writer, base_name, class_name, fields):
        """
        Writes each class of grammars to the file
        :param writer:
        :param base_name:
        :param class_name:
        :param fields:
        :return:
        """

        writer.write(f"class {class_name}({base_name}):\n")

        names = [pair.split()[1] for pair in fields]
        # Constructor
        writer.writelines([f"\tdef __init__(self, {', '.join(str(name) for name in names)}):\n",
                          f"\t\tsuper().__init__()\n"])

        # Parameters:
        for name in names:
            writer.write(f"\t\tself.{name} = {name}\n")

        # Visitor Pattern
        writer.writelines(["\n",
                           "\tdef accept(self, visitor):\n",
                           f"\t\treturn visitor.visit_{class_name}_{base_name}(self)\n"])


    def define_visitor(self, writer, base_name, types):

        writer.write("class Visitor(ABC):\n")
        for class_name, fields in types.items():
            writer.writelines([f"\tdef visit_{class_name}_{base_name}(self, {base_name.lower()}):\n",
                               "\t\tpass\n\n"])



# if __name__ == "__main__":
#     cwd = os.getcwd()[:-4] + "lox"
#     AST = GenerateAST([cwd])