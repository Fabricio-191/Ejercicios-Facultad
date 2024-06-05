package fabricio.rubio.proyecto.moea.controllers;

import org.springframework.data.domain.Page;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import fabricio.rubio.proyecto.moea.persistence.entities.StudentEntity;
import fabricio.rubio.proyecto.moea.services.StudentsService;

@RestController
public class StudentsController {
	private final StudentsService studentsService;

	public StudentsController(StudentsService studentsService) {
		this.studentsService = studentsService;
	}
	
	@GetMapping(value = "students")
	public Page<StudentEntity> getStudents(
		@RequestParam(value = "orderField", defaultValue="name") String orderField,
		@RequestParam(value = "orderCriterial", defaultValue="DESC") String orderCriterial,
		@RequestParam(value = "page", defaultValue="0") Integer page,
		@RequestParam(value = "pageSize", defaultValue="30") Integer pageSize
	) {
		return studentsService.getStudents(orderField, orderCriterial, page, pageSize);
	}

	@PostMapping(value = "students")
	public StudentEntity createStudent(@RequestBody StudentEntity student) {
		return studentsService.createStudent(student);
	}

	@GetMapping(value = "students/{id}")
	public StudentEntity getStudentById(@PathVariable("id") Long id) {
		return studentsService.getStudentById(id);
	}

	@PutMapping(value = "students/{id}")
	public StudentEntity updateStudent(@PathVariable("id") Long id, @RequestBody StudentEntity student) {
		return studentsService.updateStudent(id, student);
	}

	@DeleteMapping(value = "students/{id}")
	public void deleteStudent(@PathVariable("id") Long id) {
		studentsService.deleteStudent(id);
	}
}
