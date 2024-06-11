package fabricio.rubio.proyecto.moea.commons;

import org.moeaframework.core.Solution;
import org.moeaframework.core.variable.Permutation;
import org.moeaframework.problem.AbstractProblem;

public class MOEAProblem extends AbstractProblem {
    public MOEAProblem(int numberOfVariables, int numberOfObjectives) {
        super(numberOfVariables, numberOfObjectives);
    }

    public MOEAProblem(int numberOfVariables, int numberOfObjectives, int numberOfConstraints) {
        super(numberOfVariables, numberOfObjectives, numberOfConstraints);
    }

    @Override
    public void evaluate(Solution solution) {

    }

    @Override
    public Solution newSolution() {
        Solution solution = new Solution(numberOfVariables, numberOfObjectives, numberOfConstraints);

        solution.setVariable(0, new Permutation());

        return solution;
    }
}
