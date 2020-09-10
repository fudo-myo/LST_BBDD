import json
import os

from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy import units as u
from astropy.time import Time

from DTO.sources_dto import SourcesDto
from services.lst_sources_service import LstSourcesService
from utils.checkers import Checkers

dir_sources = "C:\\Users\\fjromero\\Documents\\cta\\BBDD_ISIDRO\\sources\\"
json_files = [f for f in os.listdir(dir_sources) if f.endswith('.json')]
source_service = LstSourcesService()
for element in json_files:
    file_json = open(dir_sources + f"\\{element}", "r")
    data_json = json.load(file_json)
    for key,value in data_json.items():
        source_dto = SourcesDto()
        source_dto.source_des = key
        source_dto.right_asc = value['RA']
        source_dto.declination = value['Dec']
        source_dto.right_asc_off_set = Checkers.check_if_key_exist(value,'RAOffset')
        source_dto.declination_off_set = Checkers.check_if_key_exist(value,'DecOffset')
        source_dto.altitude_off_set = Checkers.check_if_key_exist(value,'AltOffset')
        source_dto.azimuth_off_set = Checkers.check_if_key_exist(value,'AZOffset')
        source_equatorials = SkyCoord(ra=value['RA'], dec=value['Dec'], unit='deg', frame='icrs')
        location_obs = EarthLocation.of_site('Roque de los Muchachos')
        altaz_frame = AltAz(obstime=Time("J2000"), location=location_obs)
        altaz_source = source_equatorials.transform_to(altaz_frame)
        source_dto.altitude = altaz_source.alt.deg
        source_dto.azimuth = altaz_source.az.deg
        source_service.insert_sources(source_dto)


    print("pp")

print("prueba")
