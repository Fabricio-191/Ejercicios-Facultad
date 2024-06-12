package fabricio.rubio.proyecto.moea.services;

import java.time.Duration;
import java.util.HashMap;

import org.moeaframework.algorithm.NSGAIII;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Service;

import fabricio.rubio.proyecto.moea.commons.MOEAProblem;
import fabricio.rubio.proyecto.moea.model.dto.FrameDTO;
import jakarta.annotation.PostConstruct;

@Service
public class MOEAService {
    private final FramesService framesService;
    private final HashMap<Long, HashMap<Long, Long>> times = new HashMap<>();

    public MOEAService(FramesService framesService) {
        this.framesService = framesService;
    }

	@PostConstruct
	public HashMap<Long, HashMap<Long, Long>> loadTimes(){
        Page<FrameDTO> frames = framesService.get("id", "DESC", 0, 1000000000);

        for (FrameDTO frame : frames.getContent()) {
            times.put(frame.getIdStopDeparture(), new HashMap<>());
        }

        for (FrameDTO frame : frames.getContent()) {
            Duration time = Duration.between(frame.getArrivalDatetime(), frame.getDepartureDatetime());

			if(time.isNegative()){
				
			}

            times.get(frame.getIdStopDeparture()).put(frame.getIdStopArrival(), time.toSeconds());
        }

        return times;
	}

    public String run(){
		MOEAProblem problem = new MOEAProblem(1, 1, 0);
		NSGAIII algorithm = new NSGAIII(problem);
		algorithm.run(10000);
		algorithm.getResult().display();

        return algorithm.getResult().toString();
    }
}
