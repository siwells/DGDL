import sys
import antlr3
import antlr3.tree
from dgdlLexer import dgdlLexer
from dgdlParser import dgdlParser

def pretty_print_tree(tree):
    indent = 0
    last = ""
    for child in tree.getChildren():
        if child.text == "{":
            indent += 1
            sys.stdout.write(child.text)
            sys.stdout.write("\n")
        elif child.text == "}":
            indent -= 1
            sys.stdout.write("\n")
            sys.stdout.write("    "*indent+child.text)
        elif child.text == ",":
            sys.stdout.write(child.text + "\n")
        elif child.text == ":":
            sys.stdout.write(child.text)
        elif child.text == "then":
            sys.stdout.write("\n"+"    "*indent+child.text)
        elif child.text == "and":
            sys.stdout.write(" "+child.text)
        elif child.text == "else":
            sys.stdout.write(" "+child.text)
        else:
            if last == ":":
                sys.stdout.write(child.text)
            elif last == "if":
                sys.stdout.write(" "+child.text)
            elif last == "then":
                sys.stdout.write(" "+child.text)
            elif last == "and":
                sys.stdout.write(" "+child.text)
            elif last == "else":
                sys.stdout.write(" "+child.text)
            else:
                sys.stdout.write("    "*indent+child.text)
        last = child.text

def main():
    if len(sys.argv) != 2:
        print "Usage: dgdl file.dgdl"
        sys.exit(1)
    
    infile = sys.argv[1]
    
    char_stream = antlr3.ANTLRFileStream(infile)
    lexer = dgdlLexer(char_stream)
    tokens = antlr3.CommonTokenStream(lexer)
    
    parser = dgdlParser(tokens)
    
    try:  
        t = parser.dgdl().tree
    except RecognitionException:
        traceback.print_stack()
    
    if parser.getNumberOfSyntaxErrors() is 0:
        print "Using grammar file:\t", repr(parser.grammarFileName)
        print "Using input file:\t", repr(parser.getSourceName())
        print "Generates the following AST:"
        pretty_print_tree(t)

if __name__ == "__main__":
    main()
