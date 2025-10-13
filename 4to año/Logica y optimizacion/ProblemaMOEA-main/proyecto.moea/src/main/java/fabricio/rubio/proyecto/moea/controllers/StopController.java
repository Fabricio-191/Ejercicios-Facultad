package fabricio.rubio.proyecto.moea.controllers;

import org.springframework.data.domain.Page;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import fabricio.rubio.proyecto.moea.model.dto.StopDTO;
import fabricio.rubio.proyecto.moea.services.StopService;

@RestController
public class StopController {
    private final StopService service;

    public StopController(StopService service) {
        this.service = service;
    }

    @GetMapping(value = "stops")
    public Page<StopDTO> getStops(
        @RequestParam(value = "orderField", defaultValue="id") String orderField,
        @RequestParam(value = "orderCriterial", defaultValue="DESC") String orderCriterial,
        @RequestParam(value = "page", defaultValue="0") Integer page,
        @RequestParam(value = "pageSize", defaultValue="30") Integer pageSize
    ) {
        return service.get(orderField, orderCriterial, page, pageSize);
    }

}