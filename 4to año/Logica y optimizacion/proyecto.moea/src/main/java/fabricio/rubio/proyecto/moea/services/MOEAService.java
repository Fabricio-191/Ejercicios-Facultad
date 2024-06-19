package fabricio.rubio.proyecto.moea.services;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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

    private final HashMap<Integer, Long> cities = new HashMap<>();
    private final HashMap<Long, Integer> inverseCities = new HashMap<>();
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

    public void loadRequirements(){
        requirements = requirementsService
            .get("id", "DESC", 0, 1000000000)
            .stream()
            .collect(Collectors.groupingBy(RequirementDTO::getCategory));
    }

    public void loadTrunks(){
        trunks = trunkService
            .get("id", "DESC", 0, 1000000000)
            .stream()
            .collect(Collectors.groupingBy(TrunkDTO::getCategory));
    }

    public void loadCities(){
        // 8766
        Page<StopDTO> stops = stopService.get("id", "DESC", 0, 1000000000);

        int i = 0;
        for (StopDTO stop : stops.getContent()) {
            cities.put(i, stop.getId());
            inverseCities.put(stop.getId(), i);
            i++;
        }

        Page<RequirementDTO> requirements = requirementsService.get("id", "DESC", 0, 1000000000);

        for (RequirementDTO requirement : requirements.getContent()) {
            if(!cities.containsValue(requirement.getId_stop_departure())){
                cities.put(i, requirement.getId_stop_departure());
                inverseCities.put(requirement.getId_stop_departure(), i);
                i++;
            }
            if(!cities.containsValue(requirement.getId_stop_arrival())){
                cities.put(i, requirement.getId_stop_arrival());
                inverseCities.put(requirement.getId_stop_arrival(), i);
                i++;
            }
        }

        Page<FrameDTO> frames = framesService.get("id", "DESC", 0, 1000000000);

        for (FrameDTO frame : frames.getContent()) {
            if(!cities.containsValue(frame.getIdStopDeparture())){
                cities.put(i, frame.getIdStopDeparture());
                inverseCities.put(frame.getIdStopDeparture(), i);
                i++;
            }
            if(!cities.containsValue(frame.getIdStopArrival())){
                cities.put(i, frame.getIdStopArrival());
                inverseCities.put(frame.getIdStopArrival(), i);
                i++;
            }
        }
    }

	public void loadFrames(){
	    List<FrameDTO> framess = framesService.get("id", "DESC", 0, 1000000000).getContent();

		for (FrameDTO frame : framess) {
            if(!this.frames.containsKey(frame.getIdStopDeparture())){
                this.frames.put(frame.getIdStopDeparture(), new HashMap<>());
            }

            this.frames.get(frame.getIdStopDeparture()).put(frame.getIdStopArrival(), frame);
		}

//         for(int i = 0; i < cities.size(); i++){
//             if(frames[i][i] != null) continue;
//             FrameDTO newFrame = new FrameDTO();
//
//             newFrame.setIdStopDeparture(cities.get(i));
//             newFrame.setIdStopArrival(cities.get(i));
//             newFrame.setPrice(0.0);
//             newFrame.setDeltaTime(0L);
//
//             frames[i][i] = newFrame;
//         }
//
//         ArrayList<int[]> missing = new ArrayList<>();
//
//         for(int i = 0; i < cities.size(); i++){
//             for(int j = 0; j < cities.size(); j++){
//                 if(frames[i][j] == null) missing.add(new int[]{i, j});
//             }
//         }
//
//         int prev = missing.size();
//         while(!missing.isEmpty()){
//             for(int i = 0; i < missing.size(); i++){
//                 int[] pair = missing.get(i);
//                 for(int j = 0; j < cities.size(); j++){
//                     if(frames[pair[0]][j] == null || frames[j][pair[1]] == null) continue;
//                     FrameDTO newFrame = new FrameDTO();
//
//                     newFrame.setIdStopDeparture(frames[pair[0]][j].getIdStopDeparture());
//                     newFrame.setIdStopArrival(frames[j][pair[1]].getIdStopArrival());
//                     newFrame.setPrice(frames[pair[0]][j].getPrice() + frames[j][pair[1]].getPrice());
//                     newFrame.setDeltaTime(frames[pair[0]][j].getDeltaTime() + frames[j][pair[1]].getDeltaTime());
//
//                     frames[pair[0]][pair[1]] = newFrame;
//                     frames[pair[1]][pair[0]] = newFrame;
//                     missing.remove(i);
//                     break;
//                 }
//             }
//
//             if(prev == missing.size()) break;
//             prev = missing.size();
//         }
//
//         System.out.println("Missing: " + missing.size());
	}

    private NondominatedPopulation solve(String type){
        // https://github.com/MOEAFramework/MOEAFramework/blob/master/docs/listOfAlgorithms.md#nsga-iii
        MOEAProblem problem = new MOEAProblem(1, 3, 0, frames, cities, requirements.get(type), trunks.get(type));

        Executor executor = new Executor()
                .withProblem(problem)
                .withAlgorithm("NSGAIII")
                .withProperty("populationSize", 1000)
                // .distributeOn(4)
                .withMaxEvaluations(100000);

        NondominatedPopulation result = executor.run();

        return result;
    }

    public String run() throws InterruptedException {
		JSONObject allData = new JSONObject();

        float startTimeG = System.nanoTime();

        Arrays.stream(types)
            .parallel()
            .forEach(type -> {
                float startTime = System.nanoTime();
                NondominatedPopulation result = this.solve(type);

                Solution solution = result.get(0);

                JSONObject solutionJSON = new JSONObject();
                solutionJSON.put("computingTime", (System.nanoTime() - startTime) / 1000000000);
                solutionJSON.put("objectives", new JSONArray(solution.getObjectives()));
                // solutionJSON.put("variable0", new JSONArray(solution.getVariable(0).toString()));
                solutionJSON.put("variable0", solution.getVariable(0).toString());

                allData.put(type, solutionJSON);
            });


        allData.put("_fullTime", (System.nanoTime() - startTimeG) / 1000000000);

		return allData.toString();
    }
}