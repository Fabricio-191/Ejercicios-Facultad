package fabricio.rubio.proyecto.moea.commons;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

import org.moeaframework.core.Solution;
import org.moeaframework.core.variable.EncodingUtils;
import org.moeaframework.core.variable.Permutation;
import org.moeaframework.problem.AbstractProblem;

import fabricio.rubio.proyecto.moea.model.dto.FrameDTO;
import fabricio.rubio.proyecto.moea.model.dto.RequirementDTO;
import fabricio.rubio.proyecto.moea.model.dto.TrunkDTO;

// Atributes for DTO's
// FrameDTO: Long idStopDeparture, Long idStopArrival, Double price, LocalTime departureDatetime, LocalTime arrivalDatetime
// RequirementDTO: Long id, Long id_stop_departure, Long id_stop_arrival, String category, LocalTime pickup_time, Float loading
// TrunkDTO: Long id, Long id_stop_parking, Integer capacity, String category
// StopDTO: Long id

public class MOEAProblem extends AbstractProblem {
    Map<Long, Map<Long, FrameDTO>> frames;
	List<RequirementDTO>  requirements;
	List<TrunkDTO> trunks;

    public MOEAProblem(
        int numberOfVariables,
        int numberOfObjectives,
        int numberOfConstraints,
        Map<Long, Map<Long, FrameDTO>> frames,
        List<RequirementDTO> requirements,
        List<TrunkDTO> trunks
    ) {
        super(numberOfVariables, numberOfObjectives, numberOfConstraints);
        this.frames = frames;
        this.requirements = requirements;
		this.trunks = trunks;
    }

    @Override
    public void evaluate(Solution solution) {
        double precioTotal = 0.0; // precio total (precio frames)

        int[] permutation = EncodingUtils.getPermutation(solution.getVariable(0));

		int[] capacities = trunks.stream().mapToInt(TrunkDTO::getCapacity).toArray();
        long[] currentStops = trunks.stream().map(TrunkDTO::getId_stop_parking).mapToLong(x -> x).toArray();
        double[] times = new double[trunks.size()];

        int camion = 0;
        int solvedRequirements = 0;
        for(int requirementIndex : permutation){
            RequirementDTO requirement = requirements.get(requirementIndex);

            int camionOriginal = camion;
            if(capacities[camion] - requirement.getLoading() < 0){
                camion++;
                if(camion == camionOriginal) break;
                if(camion == trunks.size()) camion = 0;
            }
            capacities[camion] -= requirement.getLoading();

            FrameDTO frame = frames.get(currentStops[camion]).get(requirement.getId_stop_departure());
            if(frame == null) throw new RuntimeException("Frame not found");
            precioTotal += frame.getPrice();
            times[camion] += frame.getDeltaTime();
/
            frame = frames.get(requirement.getId_stop_departure()).get(requirement.getId_stop_arrival());
            if(frame == null) throw new RuntimeException("Frame not found");
            precioTotal += frame.getPrice();
            times[camion] += frame.getDeltaTime();

            currentStops[camion] = requirement.getId_stop_arrival();

            if(camion == trunks.size()) camion = 0;
            solvedRequirements++;
        }

        solution.setObjective(0, requirements.size() - solvedRequirements);
        solution.setObjective(1, Arrays.stream(times).reduce(Double::max).getAsDouble());
		solution.setObjective(2, precioTotal);
    }

    @Override
    public Solution newSolution() {
        Solution solution = new Solution(numberOfVariables, numberOfObjectives, numberOfConstraints);

        // https://github.com/MOEAFramework/MOEAFramework/blob/master/docs/listOfDecisionVariables.md#permutation
		Permutation permutation = EncodingUtils.newPermutation(requirements.size());
		permutation.randomize();
		solution.setVariable(0, permutation);

        return solution;
    }
}