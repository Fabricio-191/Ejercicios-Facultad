package fabricio.rubio.proyecto.moea.services;

import fabricio.rubio.proyecto.moea.model.dto.RequirementDTO;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import fabricio.rubio.proyecto.moea.model.mapper.RequirementMapper;
import fabricio.rubio.proyecto.moea.services.repositories.RequirementRepository;
import org.springframework.stereotype.Service;


@Service
public class RequirementsService {
	protected final RequirementRepository repository;
	protected final RequirementMapper mapper;

	public RequirementsService(RequirementRepository repository, RequirementMapper mapper) {
		this.repository = repository;
		this.mapper = mapper;
	}

	public Page<RequirementDTO> get(String orderField, String orderCriterial, Integer pageNumber, Integer pageSize) {
		Pageable page;

		if (orderCriterial.equalsIgnoreCase("desc")) {
			page = PageRequest.of(pageNumber, pageSize, Sort.by(orderField).descending());
		}else{
			page = PageRequest.of(pageNumber, pageSize, Sort.by(orderField).ascending());
		}

		return repository.findAll(page).map(this.mapper::toDTO);
	}
}