package fabricio.rubio.proyecto.moea.services;

import java.time.Duration;
import java.util.HashMap;

import org.springframework.data.domain.Page;
import org.springframework.stereotype.Service;

import fabricio.rubio.proyecto.moea.model.dto.FrameDTO;

@Service
public class MOEAService {
    private final FramesService framesService;
    private final HashMap<Long, HashMap<Long, Duration>> times = new HashMap<>();

    public MOEAService(FramesService framesService) {
        this.framesService = framesService;
        Page<FrameDTO> frames = framesService.get("id", "DESC", 0, 1000000000);

        for (FrameDTO frame : frames.getContent()) {
            times.put(frame.getIdStopDeparture(), new HashMap<>());
        }

        for(FrameDTO frame : frames.getContent()) {
            Duration time = Duration.between(frame.getArrivalDatetime(), frame.getDepartureDatetime());
            times.get(frame.getIdStopDeparture()).put(frame.getIdStopArrival(), time);
        }
    }


    public String run(){
        String str = "";

        for(Long id1 : times.keySet()) {
            for(Long id2 : times.get(id1).keySet()) {
                str += id1 + " " + id2 + " " + times.get(id1).get(id2) + "<br>";
            }
        }

        return str;
    }
}
