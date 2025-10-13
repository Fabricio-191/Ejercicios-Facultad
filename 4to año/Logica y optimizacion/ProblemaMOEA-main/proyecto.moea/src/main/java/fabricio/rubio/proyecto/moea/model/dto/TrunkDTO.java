package fabricio.rubio.proyecto.moea.model.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class TrunkDTO {
    private Long id;
    private Long id_stop_parking;
    private Integer capacity;
	private String category;
}