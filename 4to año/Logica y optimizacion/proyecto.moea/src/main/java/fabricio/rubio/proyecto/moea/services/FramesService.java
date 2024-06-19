package fabricio.rubio.proyecto.moea.services;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import fabricio.rubio.proyecto.moea.model.dto.FrameDTO;
import fabricio.rubio.proyecto.moea.model.mapper.FramesMapper;
import fabricio.rubio.proyecto.moea.services.repositories.FramesRepository;


@Service
public class FramesService {
	protected final FramesRepository repository;
	protected final FramesMapper mapper;

	public FramesService(FramesRepository repository, FramesMapper mapper) {
		this.repository = repository;
		this.mapper = mapper;
	}

	public Page<FrameDTO> get(String orderField, String orderCriterial, Integer pageNumber, Integer pageSize) {
		Pageable page;

		if (orderCriterial.equalsIgnoreCase("desc")) {
			page = PageRequest.of(pageNumber, pageSize, Sort.by(orderField).descending());
		}else{
			page = PageRequest.of(pageNumber, pageSize, Sort.by(orderField).ascending());
		}

		return repository.findAll(page).map(this.mapper::toDTO);
	}
}