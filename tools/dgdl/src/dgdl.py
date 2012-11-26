import argparse
import sys
import antlr3
import antlr3.tree
from dgdlLexer import dgdlLexer
from dgdlParser import dgdlParser

def pretty_print_tree(tree):
    fragments = []
    indent = 0
    last = ""
    for child in tree.getChildren():
        if child.text == "<EOF>":
            pass
        elif child.text == "{":
            indent += 1
            fragments.append(child.text)
            fragments.append("\n")
        elif child.text == "}":
            indent -= 1
            fragments.append("\n")
            fragments.append("    "*indent+child.text)
        elif child.text == ",":
            fragments.append(child.text + "\n")
        elif child.text == ":":
            fragments.append(child.text)
        elif child.text == "then":
            fragments.append("\n"+"    "*indent+child.text)
        elif child.text == "and":
            fragments.append(" "+child.text)
        elif child.text == "else":
            fragments.append(" "+child.text)
        else:
            if last == ":":
                fragments.append(child.text)
            elif last == "if":
                fragments.append(" "+child.text)
            elif last == "then":
                fragments.append(" "+child.text)
            elif last == "and":
                fragments.append(" "+child.text)
            elif last == "else":
                fragments.append(" "+child.text)
            else:
                fragments.append("    "*indent+child.text)
        last = child.text
    return ''.join(fragments)

def pretty_print(tree, outfile):
    if outfile:
        with open(outfile, 'w') as f:
            data = pretty_print_tree(tree)
            f.write(data)
    else:
        print pretty_print_tree(tree)

def main():
    parser = argparse.ArgumentParser(description="DGDL command line tool. Use to verify and prettyprint DGDL game descriptions.")
    
    parser.add_argument("infile", help="The input DGDL game description to work with.")
    parser.add_argument("-o", "--out", help="Write the game description to the output file instead of stdout", nargs=1)    
    parser.add_argument("-p", "--prettyprint", help="prettyprint infile by adding whitespace to increase comprehension", action="store_true")
    
    args = parser.parse_args()
    
    infile = args.infile
    char_stream = antlr3.ANTLRFileStream(infile)
    lexer = dgdlLexer(char_stream)
    tokens = antlr3.CommonTokenStream(lexer)
    
    parser = dgdlParser(tokens)
    
    outfile = ""
    if(args.out):
        outfile = ''.join(args.out)
    
    try:  
        t = parser.dgdl().tree
    except RecognitionException:
        traceback.print_stack()
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print "There were errors whilst parsing the supplied input file \""+infile+"\""
        sys.exit(0)
    elif args.prettyprint:
        pretty_print(t, outfile)

if __name__ == "__main__":
    main()
