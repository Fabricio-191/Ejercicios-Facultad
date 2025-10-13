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
@Table(name = "truncks")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class TrunkEntity {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
    private Long id_stop_parking;
    private Integer capacity;
	private String category;
}

// id_stop_departure,id_stop_arrival,category,pickup_time,id_stop_parking,capacity,Id
