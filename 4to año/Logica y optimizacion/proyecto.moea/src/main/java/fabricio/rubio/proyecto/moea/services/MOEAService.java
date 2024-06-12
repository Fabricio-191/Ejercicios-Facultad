package fabricio.rubio.proyecto.moea.services;

import java.time.Duration;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import fabricio.rubio.proyecto.moea.model.dto.RequirementDTO;
import fabricio.rubio.proyecto.moea.model.dto.StopDTO;
import fabricio.rubio.proyecto.moea.model.dto.TrunkDTO;
import org.moeaframework.algorithm.NSGAIII;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Service;

import fabricio.rubio.proyecto.moea.commons.MOEAProblem;
import fabricio.rubio.proyecto.moea.model.dto.FrameDTO;
import jakarta.annotation.PostConstruct;

@Service
public class MOEAService {
    private final FramesService framesService;
    private final StopService stopService;
    private final RequirementsService requirementsService;
    private final TrunkService trunkService;

    private final HashMap<Long, HashMap<Long, Long>> times = new HashMap<>();
    private final HashMap<Long, Long> cities = new HashMap<>();
    private Map<String, List<RequirementDTO>> requirements;
    private Map<String, List<TrunkDTO>> trunks;

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

	@PostConstruct
	public void loadTimes(){
        Page<FrameDTO> frames = framesService.get("id", "DESC", 0, 1000000000);

        for (FrameDTO frame : frames.getContent()) {
            times.put(frame.getIdStopDeparture(), new HashMap<>());
        }

        for (FrameDTO frame : frames.getContent()) {
            Duration time = Duration.between(frame.getArrivalDatetime(), frame.getDepartureDatetime());

			if(time.isNegative()) time.plusDays(1);

            times.get(frame.getIdStopDeparture()).put(frame.getIdStopArrival(), time.toMinutes());
        }
	}

    @PostConstruct
    public void loadCities(){
        Page<StopDTO> stops = stopService.get("id", "DESC", 0, 1000000000);

        long i = 1;
        for (StopDTO stop : stops.getContent()) {
            cities.put(i, stop.getId());
            i++;
        }
    }

    @PostConstruct
    public void loadRequirements(){
        requirements = requirementsService
                .get("id", "DESC", 0, 1000000000)
                .stream()
                .collect(Collectors.groupingBy(RequirementDTO::getCategory));
    }

    @PostConstruct
    public void loadTrunks(){
        trunks = trunkService
                .get("id", "DESC", 0, 1000000000)
                .stream()
                .collect(Collectors.groupingBy(TrunkDTO::getCategory));
    }

    public String run(){
		MOEAProblem problem = new MOEAProblem(3, 1, 0, times, cities, requirements, trunks);
		NSGAIII algorithm = new NSGAIII(problem);
		algorithm.run(10000);
		algorithm.getResult().display();

        return algorithm.getResult().toString();
    }
}
