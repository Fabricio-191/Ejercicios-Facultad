using System;

namespace Cuestionario {
	class Cuestionario {

		public static void Main (string[] args) {
			if (args.Length != 2){
				Console.WriteLine("Usage: Cuestionario.exe <inputfile> <outputfile>");
				if(args.Length == 0){
					Console.WriteLine("No input file specified");
				}else if(args.Length == 1){
					Console.WriteLine("No output file specified");
				}else if(args.Length > 2){
					Console.WriteLine("Too many arguments");
				}
			} else {
				Scanner scanner = new Scanner(args[0]);
				Parser parser = new Parser(scanner);
				parser.tab = new SymbolTable(parser);
				parser.gen = new CodeGenerator();
				parser.Parse();
				if (parser.errors.count == 0) {
					parser.gen.writeCode(args[1]);
				}
			}
		}
	}
}
