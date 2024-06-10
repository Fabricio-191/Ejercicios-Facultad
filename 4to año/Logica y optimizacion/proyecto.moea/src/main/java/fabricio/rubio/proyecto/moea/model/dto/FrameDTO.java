package fabricio.rubio.proyecto.moea.model.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalTime;

@Getter
@Setter
@NoArgsConstructor
public class FrameDTO {
    private Long id;
    private Long idStopDeparture;
    private Long idStopArrival;
    private Double price;
    private LocalTime departureDatetime;
    private LocalTime arrivalDatetime;
}