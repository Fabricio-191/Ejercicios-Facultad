package fabricio.rubio.proyecto.moea.services;

import java.util.NoSuchElementException;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import fabricio.rubio.proyecto.moea.persistence.entities.StudentEntity;
import fabricio.rubio.proyecto.moea.persistence.repositories.StudentsRepository;

@Service
public class StudentsService {
	private final StudentsRepository studentRepository;

	public StudentsService(StudentsRepository studentRepository) {
		this.studentRepository = studentRepository;
	}

	public Page<StudentEntity> getStudents(String orderField, String orderCriterial, Integer pageNumber, Integer pageSize) {
		Pageable page;

		if (orderCriterial.toLowerCase().equals("desc")) {
			page = PageRequest.of(pageNumber, pageSize, Sort.by(orderField).descending());
		}else{
			page = PageRequest.of(pageNumber, pageSize, Sort.by(orderField).ascending());
		}

		return studentRepository.findAll(page);
	}

	public StudentEntity getStudentById(Long id) {
		return studentRepository.findById(id)
				.orElseThrow(() -> new NoSuchElementException("Student not found with id: " + id));
	}

	public StudentEntity createStudent(StudentEntity student) {
		return studentRepository.save(student);
	}

	public StudentEntity updateStudent(Long id, StudentEntity updatedStudent) {
		StudentEntity existingStudent = studentRepository.findById(id)
				.orElseThrow(() -> new NoSuchElementException("Student not found with id: " + id));

		existingStudent.setName(updatedStudent.getName());
		existingStudent.setBirthdate(updatedStudent.getBirthdate());
		existingStudent.setNationality(updatedStudent.getNationality());
		existingStudent.setResidence(updatedStudent.getResidence());

		return studentRepository.save(existingStudent);
	}

	public void deleteStudent(Long id) {
		studentRepository.deleteById(id);
	}
}
