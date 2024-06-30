package fabricio.rubio.proyecto.moea.controllers;


import jakarta.annotation.PostConstruct;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import fabricio.rubio.proyecto.moea.services.MOEAService;

@RestController
public class MOEAController {
    private final MOEAService service;

    public MOEAController(MOEAService service) {
        this.service = service;
    }

    @GetMapping(path = "moea/test", produces = "application/json")
	public String test(){
        this.init();
        return this.run();
	}

    @GetMapping("moea/init")
    public void init() {
        System.out.println("Loading cities");
        service.loadCities();
        System.out.println("Loading requirements");
        service.loadRequirements();
        System.out.println("Loading trunks");
        service.loadTrunks();
        System.out.println("Loading frames");
        service.loadFrames();
    }

    @GetMapping(path = "moea/run", produces = "application/json")
    public String run() {
        System.out.println("Running MOEA");
        try{
            return service.run();
        }catch (InterruptedException e){
            e.printStackTrace();
            return "{\"error\": \"" + e.getMessage() + "\" }";
        }
    }
}