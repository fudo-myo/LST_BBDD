from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.sources_dto import SourcesDto, create_source
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_sources import LstSources
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstSourcesService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_sources = None
        self.__sources_by_id = None

    def insert_sources(self, sources_insert: SourcesDto):
        try:
            sources_aux = LstSources(
                source_des=sources_insert.source_des,
                right_asc=sources_insert.right_asc,
                declination=sources_insert.declination,
                altitude=sources_insert.altitude,
                azimuth=sources_insert.azimuth,
                right_asc_off_set=sources_insert.right_asc_off_set,
                declination_off_set=sources_insert.declination_off_set,
                altitude_off_set=sources_insert.altitude_off_set,
                azimuth_off_set=sources_insert.azimuth_off_set
            )

            self.__session.add(sources_aux)
            self.__session.commit()
            if sources_aux.id_source is not None:
                sources_insert.id_source = sources_aux.id_source
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstSources.__tablename__.name,
                                                                          sources_aux.id_source))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstSources.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_sources(self, source_des_search, id_source=None, source_des_update=None, right_asc=None,
                       declination=None, altitude=None,
                       azimuth=None, right_asc_off_set=None, declination_off_set=None, altitude_off_set=None,
                       azimuth_off_set=None):
        try:
            source_before: SourcesDto = self.get_source_by_id_and_desc(id_source, source_des_search)
            if Checkers.validate_int(id_source, LstSources.id_source.name) and \
                    Checkers.validate_string(source_des_search, LstSources.source_des.name) and \
                    source_before.id_source is not None and \
                    source_before.source_des is not None:
                self.__session.query(LstSources).filter(LstSources.id_source.like(source_before.id_source)) \
                    .filter(LstSources.source_des.like(source_before.source_des)) \
                    .update({
                    LstSources.source_des: Checkers.check_field_not_null(LstSources.source_des, source_des_update),
                    LstSources.right_asc: Checkers.check_field_not_null(LstSources.right_asc, right_asc),
                    LstSources.declination: Checkers.check_field_not_null(LstSources.declination, declination),
                    LstSources.altitude: Checkers.check_field_not_null(LstSources.altitude, altitude),
                    LstSources.azimuth: Checkers.check_field_not_null(LstSources.azimuth, azimuth),
                    LstSources.right_asc_off_set: Checkers.check_field_not_null(LstSources.right_asc_off_set,
                                                                                right_asc_off_set),
                    LstSources.declination_off_set: Checkers.check_field_not_null(LstSources.declination_off_set,
                                                                                  declination_off_set),
                    LstSources.altitude_off_set: Checkers.check_field_not_null(LstSources.altitude_off_set,
                                                                               altitude_off_set),
                    LstSources.azimuth_off_set: Checkers.check_field_not_null(LstSources.azimuth_off_set,
                                                                              azimuth_off_set)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                source_after: SourcesDto = self.get_source_by_id_and_desc(source_before.id_source,
                                                                          Checkers.check_field_not_null(
                                                                              source_before.source_des,
                                                                              source_des_update
                                                                          ))

                if source_before.__dict__ != source_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstSources.__tablename__.name,
                                                                            source_before.id_source))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstSources.__tablename__.name))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstSources.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_source(self, id_source, source_des=None):
        try:
            source_before: SourcesDto = self.get_source_by_id_and_desc(id_source, source_des)
            if Checkers.validate_int(id_source, LstSources.id_source.name) and \
                    source_before.id_source is not None:
                self.__session.query(LstSources).filter(LstSources.id_source.like(id_source)) \
                    .delete(synchronize_session=False)
                self.__session.commit()

                source_after: SourcesDto = self.get_source_by_id_and_desc(id_source, source_des)
                if source_before.id_source is not None and \
                        source_after.id_source is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstSources.__tablename__.name,
                                                                            id_source))

                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstSources.__tablename__.name,
                        id_source))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstSources.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_sources(self):
        sources_dto_list = []
        try:
            self.__all_sources: List[SourcesDto] = self.__session.query(LstSources).all()
            if len(self.__all_sources) != 0:
                for row in self.__all_sources:
                    source_aux = create_source(
                        row.id_source,
                        row.source_des,
                        row.right_asc,
                        row.declination,
                        row.altitude,
                        row.azimuth,
                        row.right_asc_off_set,
                        row.declination_off_set,
                        row.altitude_off_set,
                        row.azimuth_off_set
                    )
                    sources_dto_list.append(source_aux)
            else:
                Checkers.empty_list(LstSources.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return sources_dto_list

    def get_source_by_id_and_desc(self, id_source=None, source_des=None):
        try:
            if id_source is not None and source_des is not None:
                self.__sources_by_id: SourcesDto = self.__session.query(LstSources).filter(
                    LstSources.id_source.like(id_source),
                    LstSources.source_des.like(source_des)).first()
            elif id_source is None and source_des is not None:
                self.__sources_by_id: SourcesDto = self.__session.query(LstSources).filter(
                    LstSources.source_des.like(source_des)).first()

            elif source_des is None and id_source is not None:
                self.__sources_by_id: SourcesDto = self.__session.query(LstSources).filter(
                    LstSources.id_source.like(id_source)).first()

            if self.__sources_by_id is not None:
                return create_source(
                    self.__sources_by_id.id_source,
                    self.__sources_by_id.source_des,
                    self.__sources_by_id.right_asc,
                    self.__sources_by_id.declination,
                    self.__sources_by_id.altitude,
                    self.__sources_by_id.azimuth,
                    self.__sources_by_id.right_asc_off_set,
                    self.__sources_by_id.declination_off_set,
                    self.__sources_by_id.altitude_off_set,
                    self.__sources_by_id.azimuth_off_set
                )

            else:
                Checkers.print_object_filter_null(LstSources.id_source.name, str(id_source))
                return create_source(None, None, None, None, None, None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_source(None, None, None, None, None, None, None, None, None, None)
