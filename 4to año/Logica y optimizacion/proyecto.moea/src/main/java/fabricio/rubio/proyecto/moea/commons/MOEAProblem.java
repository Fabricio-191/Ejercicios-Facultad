package fabricio.rubio.proyecto.moea.commons;

import fabricio.rubio.proyecto.moea.model.dto.RequirementDTO;
import fabricio.rubio.proyecto.moea.model.dto.TrunkDTO;
import org.moeaframework.core.Solution;
import org.moeaframework.core.variable.EncodingUtils;
import org.moeaframework.core.variable.Permutation;
import org.moeaframework.problem.AbstractProblem;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MOEAProblem extends AbstractProblem {
    HashMap<Long, HashMap<Long, Long>> times;
    HashMap<Long, Long> cities;
    Map<String, List<RequirementDTO>>  requirements;
    Map<String, List<TrunkDTO>> trunks;
    Array<String> types;

    public MOEAProblem(
        int numberOfVariables,
        int numberOfObjectives,
        int numberOfConstraints,
        HashMap<Long, HashMap<Long, Long>> times,
        HashMap<Long, Long> cities,
        Map<String, List<RequirementDTO>> requirements,
        Map<String, List<TrunkDTO>> trunks
    ) {
        super(numberOfVariables, numberOfObjectives, numberOfConstraints);
        this.times = times;
        this.cities = cities;
        this.requirements = requirements;
        this.trunks = trunks;
        this.types = requirements.keySet().toArray();
    }

    // maximo tiempo recorrido (tomar en cuenta stopID)
    // precio total (precio frames)
    // cantidad de requisitos no atendidos
    @Override
    public void evaluate(Solution solution) {
        double maxTime = 0.0;

        for(int i = 0; i < numberOfVariables; i++) {
            int[] permutation = EncodingUtils.getPermutation(solution.getVariable(i));
            double time = 0.0;

            for(int j = 0; j < permutation.length - 1; j++) {

            }
        }

        solution.setObjective(0, time);
    }

    @Override
    public Solution newSolution() {
        Solution solution = new Solution(numberOfVariables, numberOfObjectives, numberOfConstraints);

        int i = 0;
        for(String type : requirements.keySet()){
            Permutation permutation = EncodingUtils.newPermutation(requirements.get(type).size());
            permutation.randomize();
            solution.setVariable(i, permutation);
        }

        return solution;
    }
}
