package fabricio.rubio.proyecto.moea.commons;

import java.util.*;

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
        List<Integer>[] requirementsPerTrunk = new List[trunks.size()];
        for(int i = 0; i < trunks.size(); i++) requirementsPerTrunk[i] = new ArrayList<>();

        double precioTotal = 0.0; // precio total (precio frames)

        int[] permutation = EncodingUtils.getPermutation(solution.getVariable(0));

		int[] capacities = trunks.stream().mapToInt(TrunkDTO::getCapacity).toArray();
        long[] currentStops = trunks.stream().mapToLong(TrunkDTO::getId_stop_parking).toArray();
        double[] times = new double[trunks.size()];

        int camion = 0;
        int solvedRequirements = 0;
        for(int requirementIndex : permutation){
            RequirementDTO requirement = requirements.get(requirementIndex);

            int camionOriginal = camion;
            while(capacities[camion] - requirement.getLoading() < 0){
                camion++;
                if(camion == camionOriginal) break;
                if(camion == trunks.size()) camion = 0;
            }
            requirementsPerTrunk[camion].add(requirementIndex);
            capacities[camion] -= requirement.getLoading();

            // 8652 4533
            FrameDTO frame = frames.get(currentStops[camion]).get(requirement.getId_stop_departure());
            if(frame == null) throw new NoSuchElementException("Frame not found");
            precioTotal += frame.getPrice();
            times[camion] += frame.getDeltaTime();

            frame = frames.get(requirement.getId_stop_departure()).get(requirement.getId_stop_arrival());
            if(frame == null) throw new NoSuchElementException("Frame not found");
            precioTotal += frame.getPrice();
            times[camion] += frame.getDeltaTime();

            currentStops[camion] = requirement.getId_stop_arrival();

            camion++;
            solvedRequirements++;
            if(camion == trunks.size()) camion = 0;
        }

        solution.setObjective(0, Arrays.stream(times).reduce(Double::max).getAsDouble());
		solution.setObjective(1, precioTotal);
        solution.setObjective(2, requirements.size() - solvedRequirements);
        solution.setAttribute("times", times);
        solution.setAttribute("capacities", capacities);
        solution.setAttribute("requirementsPerTrunk", requirementsPerTrunk);
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