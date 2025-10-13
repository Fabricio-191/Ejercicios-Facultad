package fabricio.rubio.proyecto.moea.model.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalTime;

@Getter
@Setter
@NoArgsConstructor
public class RequirementDTO {
	private Long id;
	private Long id_stop_departure;
	private Long id_stop_arrival;
	private String category;
	private LocalTime pickup_time;
	private Float loading;
}