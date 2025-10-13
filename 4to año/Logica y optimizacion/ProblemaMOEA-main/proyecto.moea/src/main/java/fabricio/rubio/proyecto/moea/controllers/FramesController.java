package fabricio.rubio.proyecto.moea.controllers;

import org.springframework.data.domain.Page;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import fabricio.rubio.proyecto.moea.model.dto.FrameDTO;
import fabricio.rubio.proyecto.moea.services.FramesService;

@RestController
public class FramesController {
    private final FramesService service;

    public FramesController(FramesService service) {
        this.service = service;
    }

    @GetMapping(value = "frames")
    public Page<FrameDTO> getFrames(
            @RequestParam(value = "orderField", defaultValue="id") String orderField,
            @RequestParam(value = "orderCriterial", defaultValue="DESC") String orderCriterial,
            @RequestParam(value = "page", defaultValue="0") Integer page,
            @RequestParam(value = "pageSize", defaultValue="30") Integer pageSize
    ) {
        return service.get(orderField, orderCriterial, page, pageSize);
    }

}