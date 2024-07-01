package fabricio.rubio.proyecto.moea.services;

import java.util.*;
import java.util.stream.Collectors;

import org.json.JSONArray;
import org.json.JSONObject;
import org.moeaframework.Executor;
import org.moeaframework.core.NondominatedPopulation;
import org.moeaframework.core.Solution;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Service;

import fabricio.rubio.proyecto.moea.commons.MOEAProblem;
import fabricio.rubio.proyecto.moea.model.dto.FrameDTO;
import fabricio.rubio.proyecto.moea.model.dto.RequirementDTO;
import fabricio.rubio.proyecto.moea.model.dto.StopDTO;
import fabricio.rubio.proyecto.moea.model.dto.TrunkDTO;

@Service
public class MOEAService {
    private final FramesService framesService;
    private final StopService stopService;
    private final RequirementsService requirementsService;
    private final TrunkService trunkService;

    private final HashMap<Long, StopDTO> cities = new HashMap<>();
    private Map<String, List<RequirementDTO>> requirements;
    private Map<String, List<TrunkDTO>> trunks;
    private final Map<Long, Map<Long, FrameDTO>> frames = new HashMap<>();
    private final String[] types = { "PARTES", "SÓLIDO", "DELICADO", "LÍQUIDO", "INFLAMABLE" };

    public MOEAService(
        FramesService framesService,
        StopService stopService,
        RequirementsService requirementsService,
        TrunkService trunkService
    ) {
        this.framesService = framesService;
        this.stopService = stopService;
        this.requirementsService = requirementsService;
        this.trunkService = trunkService;
    }

    public void loadCities(){
        // 8766
        Page<StopDTO> stops = stopService.get("id", "DESC", 0, 1000000000);

        for (StopDTO stop : stops.getContent()) {
            if(stop.getId() == 4533 || stop.getId() == 8652) continue;
            cities.put(stop.getId(), stop);
        }

        System.out.println("Cities: " + cities.size());
    }

    public String getStopName(long id){
        return cities.get(id).getName();
    }

    public void loadRequirements(){
        requirements = requirementsService
            .get("id", "DESC", 0, 1000000000)
            .stream()
            .filter(requirement ->
                  cities.containsKey(requirement.getId_stop_departure()) &&
                  cities.containsKey(requirement.getId_stop_arrival())
            )
            .collect(Collectors.groupingBy(RequirementDTO::getCategory));
    }

    public void loadTrunks(){
        trunks = trunkService
            .get("id", "DESC", 0, 1000000000)
            .stream()
                .filter(x -> cities.containsKey(x.getId_stop_parking()))
            .collect(Collectors.groupingBy(TrunkDTO::getCategory));
    }

	public void loadFrames(){
		for(long cityId : cities.keySet()){
		    this.frames.put(cityId, new HashMap<>());
		    FrameDTO newFrame = new FrameDTO();		
		    newFrame.setIdStopDeparture(cityId);
		    newFrame.setIdStopArrival(cityId);
		    newFrame.setPrice(0.0);
		    newFrame.setDeltaTime(0L);		
		    this.frames.get(cityId).put(cityId, newFrame);
		}

		List<FrameDTO> framess = framesService.get("id", "DESC", 0, 1000000000).getContent();
		for (FrameDTO frame : framess) {
            if (!cities.containsKey(frame.getIdStopDeparture())) continue;
            if (!cities.containsKey(frame.getIdStopArrival())) continue;

		    this.frames.get(frame.getIdStopDeparture()).put(frame.getIdStopArrival(), frame);
		    this.frames.get(frame.getIdStopArrival()).put(frame.getIdStopDeparture(), frame);
		}

		ArrayList<long[]> missing = new ArrayList<>();
        Long[] cityIds = cities.keySet().toArray(new Long[0]);
        for(int i = 0; i < cityIds.length - 1; i++){
            long cityAId = cityIds[i];
            for(int j = i + 1; j < cityIds.length; j++){
                long cityBId = cityIds[j];
                if(frames.get(cityAId).get(cityBId) == null) missing.add(new long[]{cityAId, cityBId});
            }
        }
        System.out.print("Missing frames " + missing.size() + " => ");

		int prev = missing.size();
		while(!missing.isEmpty()){
		    for(int i = 0; i < missing.size(); i++){
		        long[] pair = missing.get(i);
		        for(long otherCity : cityIds){
		            if(frames.get(pair[0]).get(otherCity) == null || frames.get(otherCity).get(pair[1]) == null) continue;
		            FrameDTO newFrame = new FrameDTO();		
		            newFrame.setIdStopDeparture(frames.get(pair[0]).get(otherCity).getIdStopDeparture());
		            newFrame.setIdStopArrival(frames.get(otherCity).get(pair[1]).getIdStopArrival());
		            newFrame.setPrice(frames.get(pair[0]).get(otherCity).getPrice() + frames.get(otherCity).get(pair[1]).getPrice());
		            newFrame.setDeltaTime(frames.get(pair[0]).get(otherCity).getDeltaTime() + frames.get(otherCity).get(pair[1]).getDeltaTime());

		            frames.get(pair[0]).put(pair[1], newFrame);
		            frames.get(pair[1]).put(pair[0], newFrame);		
		            missing.remove(i);
		            break;
		        }
		    }		
		    if(prev == missing.size()) break;
		    prev = missing.size();
		}

        System.out.println(missing.size());
	}

    private Solution solve(String type){
        // https://github.com/MOEAFramework/MOEAFramework/blob/master/docs/listOfAlgorithms.md#nsga-iii
        MOEAProblem problem = new MOEAProblem(1, 3, 0, frames, requirements.get(type), trunks.get(type));

        Executor executor = new Executor()
                .withProblem(problem)
                .withAlgorithm("NSGAIII")
                .withProperty("populationSize", 100)
                // .distributeOn(4)
                .withMaxTime(10000);

        NondominatedPopulation result = executor.run();

        return result.get(0);
    }

    public String run() throws InterruptedException {
		JSONObject allData = new JSONObject();

        Arrays.stream(types)
            .parallel()
            .forEach(type -> {
                float startTime = System.nanoTime();
                Solution solution = this.solve(type);

                JSONObject solutionJSON = new JSONObject();
                solutionJSON.put("computingTime", (System.nanoTime() - startTime) / 1000000000);
                solutionJSON.put("objectives", new JSONArray(solution.getObjectives()));
                solutionJSON.put("variable0", new JSONArray(solution.getVariable(0).toString()));
                // solutionJSON.put("variable0", solution.getVariable(0).toString());
                JSONArray trunksData = new JSONArray();

                double[] times = (double[]) solution.getAttribute("times");
                int[] capacities = (int[]) solution.getAttribute("capacities");
                List<Integer>[] requirementsPerTrunk = (List<Integer>[]) solution.getAttribute("requirementsPerTrunk");

                for(int i = 0; i < trunks.get(type).size(); i++){
                    JSONObject trunkData = new JSONObject();
                    trunkData.put("id", trunks.get(type).get(i).getId());
                    trunkData.put("capacity", trunks.get(type).get(i).getCapacity());
                    trunkData.put("requirements", new JSONArray(requirementsPerTrunk[i]));
                    trunkData.put("time", times[i]);
                    trunkData.put("capacity", capacities[i]);

                    long currentStop = trunks.get(type).get(i).getId_stop_parking();
                    String path = "Empieza en la parada: " + getStopName(currentStop) + "\n";

                    for(int requirementIndex : requirementsPerTrunk[i]){
                        RequirementDTO requirement = requirements.get(type).get(requirementIndex);
                        path += "Requisito: " + requirement.getId() + " => " + getStopName(requirement.getId_stop_departure()) + " => " + getStopName(requirement.getId_stop_arrival()) + "\n";
                    }

                    trunkData.put("path", path);


                    trunksData.put(trunkData);
                }

                solutionJSON.put("trunksData", trunksData);

                allData.put(type, solutionJSON);
            });


		return allData.toString();
    }
}