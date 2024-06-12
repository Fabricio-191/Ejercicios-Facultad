package fabricio.rubio.proyecto.moea.commons;

import org.moeaframework.core.Solution;
import org.moeaframework.core.variable.Permutation;
import org.moeaframework.problem.AbstractProblem;

// requirements: id_stop_departure, id_stop_arrival, category, pickup_time, loading
// frames: id_stop_departure, id_stop_arrival, price, departure_datetime, arrival_datetime
// trunks: id_stop_parking, capacity,id

public class MOEAProblem extends AbstractProblem {
    public MOEAProblem(int numberOfVariables, int numberOfObjectives) {
        super(numberOfVariables, numberOfObjectives);
    }

    public MOEAProblem(int numberOfVariables, int numberOfObjectives, int numberOfConstraints) {
        super(numberOfVariables, numberOfObjectives, numberOfConstraints);
    }

    @Override
    public void evaluate(Solution solution) {
        // cubrir la mayor cantidad posible de requerimientos en la menor cantidad de tiempo posible
        double tiempo = 0;



        solution.setObjective(0, tiempo);
    }

    @Override
    public Solution newSolution() {
        Solution solution = new Solution(numberOfVariables, numberOfObjectives, numberOfConstraints);

        for (int i = 0; i < numberOfVariables; i++) {

            solution.setVariable(i, new Permutation());
        }

        return solution;
    }
}
