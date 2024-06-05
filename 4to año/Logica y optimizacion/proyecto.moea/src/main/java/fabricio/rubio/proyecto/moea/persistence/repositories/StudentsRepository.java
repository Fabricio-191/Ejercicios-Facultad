package fabricio.rubio.proyecto.moea.persistence.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;

import fabricio.rubio.proyecto.moea.persistence.entities.StudentEntity;

@Repository
public interface StudentsRepository extends PagingAndSortingRepository<StudentEntity, Long>, CrudRepository<StudentEntity, Long> {

}
