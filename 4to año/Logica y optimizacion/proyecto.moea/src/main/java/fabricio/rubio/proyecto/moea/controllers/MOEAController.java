package fabricio.rubio.proyecto.moea.controllers;

import fabricio.rubio.proyecto.moea.services.MOEAService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;

@RestController
public class MOEAController {
    private final MOEAService service;

    public MOEAController(MOEAService service) {
        this.service = service;
    }

    @GetMapping("moea/init")
    public void init() {
        service.loadTimes();
    }

    @PostMapping("moea/run")
    public String run() {
        return service.run();
    }

    @GetMapping(value = "moea/frames")
    public HashMap<Long, HashMap<Long, Long>> getFrames() {
        return service.loadTimes();
    }
}