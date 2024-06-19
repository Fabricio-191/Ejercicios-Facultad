package fabricio.rubio.proyecto.moea.model.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class FrameDTO {
    // private Long id;
    private Long idStopDeparture;
    private Long idStopArrival;
    private Double price;
    // private LocalTime departureDatetime;
    // private LocalTime arrivalDatetime;
	private Long deltaTime;

    @Override
    public String toString() {
        return "FrameDTO {" + idStopDeparture + ", " + idStopArrival + ", " + price + '}';
    }
}