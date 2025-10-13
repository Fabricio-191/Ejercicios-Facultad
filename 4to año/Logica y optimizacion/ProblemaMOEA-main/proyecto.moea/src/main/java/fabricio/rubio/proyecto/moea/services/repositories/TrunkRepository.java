package fabricio.rubio.proyecto.moea.services.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;

import fabricio.rubio.proyecto.moea.persistence.entities.TrunkEntity;

@Repository
public interface TrunkRepository extends PagingAndSortingRepository<TrunkEntity, Long>, CrudRepository<TrunkEntity, Long> {

}
