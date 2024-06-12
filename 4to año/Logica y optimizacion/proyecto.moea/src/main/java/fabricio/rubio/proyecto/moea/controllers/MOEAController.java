package fabricio.rubio.proyecto.moea.controllers;

import fabricio.rubio.proyecto.moea.services.MOEAService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MOEAController {
    private final MOEAService service;

    public MOEAController(MOEAService service) {
        this.service = service;
    }

    @GetMapping("moea/init")
    public void init() {
        service.loadTimes();
        service.loadCities();
    }

    @GetMapping("moea/run")
    @PostMapping("moea/run")
    public String run() {
        service.loadTimes();
        service.loadCities();
        return service.run();
    }
}