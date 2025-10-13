using System;
using System.IO;
using System.Collections.Generic; 

// generating .bat file

namespace Cuestionario {
	public class CodeGenerator {
		private string separator = "* ";
		private string questionColor = "Cyan";
		private string optionsColor = "White";
		private string selectedOptionColor = "Yellow";
		
		private string code = "";
		private int max_score = 0;

		public void setSeparator(string separator) {
			this.separator = separator;
		}

		public void addCode(string code) {
			// Console.WriteLine(code);
			this.code += code;
		}

		public void addIf(string condition) {
			addCode("if (" + condition + ")");
		}

		public void addPrint(string message) {
			addCode("Write-Host \"" + message + "\"\n");
		}

		public void addPrint(string message, string color) {
			addCode("Write-Host \"" + message + "\" -ForegroundColor " + color + " \n");
		}

		public void addFinalScore() {
			addPrint("Your score is $score out of " + max_score, "Magenta");
		}

		private Dictionary<Parser.Type, string> inputsTypesMap = new Dictionary<Parser.Type, string> {
			{Parser.Type.NUMBER, "int"},
			{Parser.Type.STRING, "string"},
		};

		public void addQuestion(
			string question, string correctAnswer, int value, bool includes,
			string name, Parser.Type inputType, string[] options
		) {
			if(options == null){
				addPrint(question, questionColor);
				addCode("\n$last_answer = [" + inputsTypesMap[inputType] + "] (Read-Host \"Respuesta\")\n");
			}else{
				string optionsStr = "";

				for(int i = 0; i < options.Length; i++){
					optionsStr += "\"" + options[i] + "\"";
					if(i < options.Length - 1){
						optionsStr += ", ";
					}
				}

				addCode("$last_answer = Show-Menu \"" + question + "\" @(" + optionsStr + ")\n");
			}

			if(name != null){
				addCode("$" + name + " = $last_answer\n");
			}
			addPrint("\n\n");

			if(correctAnswer == null){
				// no correct answer
				addCode("\n\n\n");
				return;
			};

			if(inputType == Parser.Type.STRING){
				if(includes){
					addCode("if ($last_answer.ToLower() -like \"*" + correctAnswer + "*\")");
				}else{
					addCode("if ($last_answer.ToLower() -eq \"" + correctAnswer + "\")");
				}
			}else{
				addCode("if ($last_answer -eq " + correctAnswer + ")");
			}

			addCode("{ $score += " + value + " }\n\n\n\n");
			max_score += value;
		}

		public void writeCode(string filename) {
			string baseCode = @"Function Clear-HostLight {
    Param ( [Parameter(Position=1)] [int32]$Count=1 )

    $CurrentLine  = $Host.UI.RawUI.CursorPosition.Y
    $ConsoleWidth = $Host.UI.RawUI.BufferSize.Width
    
    for ($i = 1; $i -le $Count; $i++) {
        [Console]::SetCursorPosition(0,($CurrentLine - $i))
        [Console]::Write(""{0,-$ConsoleWidth}"" -f "" "")
    }

    [Console]::SetCursorPosition(0,($CurrentLine - $Count))
}
		
Function Show-Menu {
    Param ( [string]$Question, [string[]]$Options )

    $selectedIndex = 0
    $key = $null

    while ($true) {
		Write-Host $Question -ForegroundColor " + questionColor + @"

        # Mostrar opciones
        for ($i = 0; $i -lt $Options.Count; $i++) {
            if ($i -eq $selectedIndex) {
                Write-Host """ + separator + @" $($Options[$i])"" -ForegroundColor " + selectedOptionColor + @"
            } else {
                Write-Host ""   $($Options[$i])"" -ForegroundColor " + optionsColor + @"
            }
        }

        # Capturar tecla presionada
        $key = $Host.UI.RawUI.ReadKey(""NoEcho,IncludeKeyDown"").VirtualKeyCode

        # Navegación con flechas
        switch ($key) {
            38 { # Flecha hacia arriba
                if ($selectedIndex -gt 0) { $selectedIndex-- }
            }
            40 { # Flecha hacia abajo
                if ($selectedIndex -lt ($Options.Count - 1)) { $selectedIndex++ }
            }
            13 { # Enter
                return $Options[$selectedIndex]
            }
        }
		
		Clear-HostLight ($Options.Count + 1)
    }
}

$score=0

";



			File.WriteAllText(filename, baseCode + code);
		}
	}
}

