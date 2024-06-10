package fabricio.rubio.proyecto.moea.persistence.entities;

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
@Table(name = "stops")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class StopEntity {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
    private String name;
    private String city;
    private String province;
    private String latitud;
    private String longitud;
}

// id,name,city,province,latitud,longitud
