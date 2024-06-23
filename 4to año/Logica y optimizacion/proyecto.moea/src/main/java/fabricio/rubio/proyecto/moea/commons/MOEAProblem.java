package fabricio.rubio.proyecto.moea.commons;

import java.util.HashMap;
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
    HashMap<Long, Long> cities;
	List<RequirementDTO>  requirements;
	List<TrunkDTO> trunks;

    public MOEAProblem(
        int numberOfVariables,
        int numberOfObjectives,
        int numberOfConstraints,
        Map<Long, Map<Long, FrameDTO>> frames,
        HashMap<Long, Long> cities,
        List<RequirementDTO> requirements,
        List<TrunkDTO> trunks
    ) {
        super(numberOfVariables, numberOfObjectives, numberOfConstraints);
        this.frames = frames;
        this.cities = cities;
        this.requirements = requirements;
		this.trunks = trunks;
    }

    @Override
    public void evaluate(Solution solution) {
        double maxTime = 0.0; // maximo tiempo recorrido (tomar en cuenta stopID)
        double precioTotal = 20.0; // precio total (precio frames)
		int requisitosNoAtendidos = 0; // cantidad de requisitos no atendidos

        int[] permutation = EncodingUtils.getPermutation(solution.getVariable(0));

		int trunk = 0;
		int capacity = trunks.get(0).getCapacity();
        double time = 0;
        long currentStop = trunks.get(0).getId_stop_parking();

        for(int i = 0; i < permutation.length; i++) {
            RequirementDTO requirement = requirements.get(permutation[i]);

            if(capacity - requirement.getLoading() < 0) { // el camion no puede llevar mas
                if(time > maxTime) maxTime = time;

                trunk++;
                if(trunks.size() == trunk) {
                    requisitosNoAtendidos = permutation.length - i;
                    break;
                }

                capacity = trunks.get(trunk).getCapacity();
                currentStop = trunks.get(trunk).getId_stop_parking();
                time = 0;
            }
            capacity -= requirement.getLoading();
            // time += requirement.getPickup_time();

            if(currentStop != requirement.getId_stop_departure()){
                FrameDTO frame = frames.get(currentStop).get(requirement.getId_stop_departure());
                if(frame == null) {
                    precioTotal += 10000;
                    time += 1000000;
                }else{
                    precioTotal += frame.getPrice();
                    time += frame.getDeltaTime();
                }

                currentStop = requirement.getId_stop_departure();
            }

            FrameDTO frame = frames.get(currentStop).get(requirement.getId_stop_arrival());
            if(frame == null) {
                precioTotal += 10000;
                time += 1000000;
            }else{
                precioTotal += frame.getPrice();
                time += frame.getDeltaTime();
            }
        }

        if(maxTime == 0) maxTime = time;


        solution.setObjective(0, requisitosNoAtendidos);
        solution.setObjective(1, maxTime);
		solution.setObjective(2, precioTotal);;
        solution.setAttribute("camionesSinUsar", trunks.size() - trunk - 1);
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