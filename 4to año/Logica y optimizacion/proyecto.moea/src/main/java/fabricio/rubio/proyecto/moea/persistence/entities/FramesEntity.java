package fabricio.rubio.proyecto.moea.persistence.entities;

import java.time.LocalDate;
import java.time.LocalTime;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "frames")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class FramesEntity {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	private Long id_stop_departure;
	private Long id_stop_arrival;
	private Double price;
	private LocalTime departure_datetime;
	private LocalTime arrival_datetime;
}

// id_stop_departure,id_stop_arrival,price,departure_datetime,arrival_datetime

