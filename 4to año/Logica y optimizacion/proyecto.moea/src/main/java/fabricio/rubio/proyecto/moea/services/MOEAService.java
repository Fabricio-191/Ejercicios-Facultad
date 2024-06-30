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

    private final HashMap<Long, Long> cities = new HashMap<>();
    private final HashMap<Long, Long> inverseCities = new HashMap<>();
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

        long i = 0;
        for (StopDTO stop : stops.getContent()) {
            cities.put(i, stop.getId());
            inverseCities.put(stop.getId(), i);
            i++;
        }

        System.out.println("Cities: " + cities.size());
    }

    public void loadRequirements(){
        requirements = requirementsService
            .get("id", "DESC", 0, 1000000000)
            .stream()
            .filter(requirement ->
                    cities.containsValue(requirement.getId_stop_arrival()) &&
                    cities.containsValue(requirement.getId_stop_departure())
            )
            .collect(Collectors.groupingBy(RequirementDTO::getCategory));
    }

    public void loadTrunks(){
        trunks = trunkService
            .get("id", "DESC", 0, 1000000000)
            .stream()
            .collect(Collectors.groupingBy(TrunkDTO::getCategory));
    }

	public void loadFrames(){
		for(long cityId : cities.values()){
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
            if (!cities.containsValue(frame.getIdStopDeparture())) continue;
            if (!cities.containsValue(frame.getIdStopArrival())) continue;

		    this.frames.get(frame.getIdStopDeparture()).put(frame.getIdStopArrival(), frame);
		    this.frames.get(frame.getIdStopArrival()).put(frame.getIdStopDeparture(), frame);
		}

		ArrayList<long[]> missing = new ArrayList<>();		
		for(long i = 0; i < cities.size() - 1; i++){
		    long cityAId = cities.get(i);
		    for(long j = i + 1; j < cities.size(); j++){
		        if(frames.get(cityAId).get(cities.get(j)) == null) missing.add(new long[]{cityAId, cities.get(j)});
		    }
		}

		int prev = missing.size();
		while(!missing.isEmpty()){
		    System.out.println("Missing: " + missing.size());
		    for(int i = 0; i < missing.size(); i++){
		        long[] pair = missing.get(i);
		        for(long otherCity : cities.values()){
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

        System.out.println("Missing: " + missing.size());
	}

    private Solution solve(String type){
        // https://github.com/MOEAFramework/MOEAFramework/blob/master/docs/listOfAlgorithms.md#nsga-iii
        MOEAProblem problem = new MOEAProblem(1, 3, 0, frames, requirements.get(type), trunks.get(type));

        Executor executor = new Executor()
                .withProblem(problem)
                .withAlgorithm("NSGAIII")
                .withProperty("populationSize", 100)
                // .distributeOn(4)
                .withMaxTime(60);

        NondominatedPopulation result = executor.run();

        return result.get(0);
    }

    public String run() throws InterruptedException {
		JSONObject allData = new JSONObject();

        float startTimeG = System.nanoTime();
        Arrays.stream(types)
            .parallel()
            .forEach(type -> {
                float startTime = System.nanoTime();
                Solution solution = this.solve(type);

                JSONObject solutionJSON = new JSONObject();
                solutionJSON.put("computingTime", (System.nanoTime() - startTime) / 1000000000);
                solutionJSON.put("objectives", new JSONArray(solution.getObjectives()));
                // solutionJSON.put("variable0", new JSONArray(solution.getVariable(0).toString()));
                solutionJSON.put("variable0", solution.getVariable(0).toString());
                solutionJSON.put("camionesSinUsar", solution.getAttribute("camionesSinUsar"));
                solutionJSON.put("framesDesconocidos", solution.getAttribute("framesDesconocidos"));

                allData.put(type, solutionJSON);
            });


        allData.put("_fullTime", (System.nanoTime() - startTimeG) / 1000000000);

		return allData.toString();
    }
}