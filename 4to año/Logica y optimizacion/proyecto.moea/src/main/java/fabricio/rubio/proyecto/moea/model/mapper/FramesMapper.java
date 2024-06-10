package fabricio.rubio.proyecto.moea.model.mapper;

import fabricio.rubio.proyecto.moea.persistence.entities.FramesEntity;
import org.springframework.stereotype.Component;
import fabricio.rubio.proyecto.moea.model.dto.FrameDTO;

@Component
public class FramesMapper {
    public FrameDTO toDTO(FramesEntity frame) {
        FrameDTO dto = new FrameDTO();
        dto.setId(frame.getId());
        dto.setIdStopDeparture(frame.getId_stop_departure());
        dto.setIdStopArrival(frame.getId_stop_arrival());
        dto.setPrice(frame.getPrice());
        dto.setDepartureDatetime(frame.getDeparture_datetime());
        dto.setArrivalDatetime(frame.getArrival_datetime());
        return dto;
    }

    public FramesEntity toEntity(FrameDTO dto) {
        FramesEntity frame = new FramesEntity();
        frame.setId(dto.getId());
        frame.setId_stop_departure(dto.getIdStopDeparture());
        frame.setId_stop_arrival(dto.getIdStopArrival());
        frame.setPrice(dto.getPrice());
        frame.setDeparture_datetime(dto.getDepartureDatetime());
        frame.setArrival_datetime(dto.getArrivalDatetime());
        return frame;
    }
}