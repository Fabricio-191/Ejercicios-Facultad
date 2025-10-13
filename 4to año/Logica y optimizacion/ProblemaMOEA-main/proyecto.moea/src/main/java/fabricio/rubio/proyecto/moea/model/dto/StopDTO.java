package fabricio.rubio.proyecto.moea.model.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class StopDTO {
    private Long id;
    private String name;
    private String city;
    private String province;
    private String latitud;
    private String longitud;
}