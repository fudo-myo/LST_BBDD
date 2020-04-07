from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.runs_dto import RunsDto, create_runs
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_runs import LstRuns
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstRunsService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_runs = None
        self.__runs_by_id = None

    def insert_runs(self, runs_insert: RunsDto):
        try:
            runs_aux = LstRuns(
                run_number=runs_insert.run_number,
                id_run_type=runs_insert.id_run_type,
                date=runs_insert.date,
                id_config=runs_insert.id_config,
                id_production=runs_insert.id_production,
                path_file=runs_insert.path_file,
                init_ra=runs_insert.init_ra,
                end_ra=runs_insert.end_ra,
                init_dec=runs_insert.init_dec,
                end_dec=runs_insert.end_dec,
                init_altitude=runs_insert.init_altitude,
                end_altitude=runs_insert.end_altitude,
                init_azimuth=runs_insert.init_azimuth,
                end_azimuth=runs_insert.end_azimuth,
                init_time_collect_data=runs_insert.init_time_collect_data,
                end_time_collect_data=runs_insert.end_time_collect_data
            )
            self.__session.add(runs_aux)
            self.__session.commit()
            if runs_aux.id_run is not None:
                print("RECORD INSERTED IN TABLE '{}' WITH ID '{}'".format(LstRuns.__tablename__.name,
                                                                          runs_aux.id_run))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstRuns.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_runs(self, id_run, run_number=None, id_run_type=None, date=None, id_config=None, id_production=None,
                    path_file=None, init_ra=None, end_ra=None,
                    init_dec=None, end_dec=None, init_altitude=None, end_altitude=None, init_azimuth=None,
                    end_azimuth=None, init_time_collect_data=None,
                    end_time_collect_data=None):
        try:
            runs_before: RunsDto = self.get_runs_by_id(id_run)
            if Checkers.validate_int(id_run, LstRuns.id_run.name) and runs_before.id_run is not None:
                self.__session.query(LstRuns).filter(LstRuns.id_run.like(id_run)) \
                    .update({
                    LstRuns.run_number: Checkers.check_field_not_null(LstRuns.run_number, run_number),
                    LstRuns.id_run_type: Checkers.check_field_not_null(LstRuns.id_run_type, id_run_type),
                    LstRuns.date: Checkers.check_field_not_null(LstRuns.date, date),
                    LstRuns.id_config: Checkers.check_field_not_null(LstRuns.id_config, id_config),
                    LstRuns.id_production: Checkers.check_field_not_null(LstRuns.id_production, id_production),
                    LstRuns.path_file: Checkers.check_field_not_null(LstRuns.path_file, path_file),
                    LstRuns.init_ra: Checkers.check_field_not_null(LstRuns.init_ra, init_ra),
                    LstRuns.end_ra: Checkers.check_field_not_null(LstRuns.end_ra, end_ra),
                    LstRuns.init_dec: Checkers.check_field_not_null(LstRuns.init_dec, init_dec),
                    LstRuns.end_dec: Checkers.check_field_not_null(LstRuns.end_dec, end_dec),
                    LstRuns.init_altitude: Checkers.check_field_not_null(LstRuns.init_altitude, init_altitude),
                    LstRuns.end_altitude: Checkers.check_field_not_null(LstRuns.end_altitude, end_altitude),
                    LstRuns.init_azimuth: Checkers.check_field_not_null(LstRuns.init_azimuth, init_azimuth),
                    LstRuns.end_azimuth: Checkers.check_field_not_null(LstRuns.end_azimuth, end_azimuth),
                    LstRuns.init_time_collect_data: Checkers.check_field_not_null(LstRuns.init_time_collect_data,
                                                                                  init_time_collect_data),
                    LstRuns.end_time_collect_data: Checkers.check_field_not_null(LstRuns.end_time_collect_data,
                                                                                 end_time_collect_data)
                },
                    synchronize_session=False
                )
                self.__session.commit()
                runs_after: RunsDto = self.get_runs_by_id(id_run)
                if runs_before.__dict__ != runs_after.__dict__:
                    print("RECORD UPDATE IN TABLE '{}' WITH ID '{}'".format(LstRuns.__tablename__.name,
                                                                            id_run))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstRuns.__tablename__.name))

            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstRuns.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_runs(self, id_run):
        try:
            runs_before: RunsDto = self.get_runs_by_id(id_run)
            if Checkers.validate_int(id_run, LstRuns.id_run.name) and runs_before.id_run is not None:
                self.__session.query(LstRuns).filter(LstRuns.id_run.like(id_run)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                runs_after: RunsDto = self.get_runs_by_id(id_run)
                if runs_before.id_run is not None and runs_after.id_run is None:
                    print("RECORD DELETE IN TABLE '{}' WITH ID '{}'".format(LstRuns.__tablename__.name,
                                                                            id_run))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstRuns.__tablename__.name,
                        id_run))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstRuns.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_runs(self):
        runs__dto_list = []
        try:
            self.__all_runs: List[RunsDto] = self.__session.query(LstRuns).all()
            if len(self.__all_runs) != 0:
                for row in self.__all_runs:
                    run_aux = create_runs(
                        row.id_run,
                        row.run_number,
                        row.id_run_type,
                        row.date,
                        row.id_config,
                        row.id_production,
                        row.path_file,
                        row.init_ra,
                        row.end_ra,
                        row.init_dec,
                        row.end_dec,
                        row.init_altitude,
                        row.end_altitude,
                        row.init_azimuth,
                        row.end_azimuth,
                        row.init_time_collect_data,
                        row.end_time_collect_data
                    )
                    runs__dto_list.append(run_aux)
            else:
                Checkers.empty_list(LstRuns.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return runs__dto_list

    def get_runs_by_id(self, id_run):
        try:
            self.__runs_by_id: RunsDto = self.__session.query(LstRuns).filter(LstRuns.id_run.like(id_run)).first()
            if self.__runs_by_id is not None:
                return create_runs(
                    self.__runs_by_id.id_run,
                    self.__runs_by_id.run_number,
                    self.__runs_by_id.id_run_type,
                    self.__runs_by_id.date,
                    self.__runs_by_id.id_config,
                    self.__runs_by_id.id_production,
                    self.__runs_by_id.path_file,
                    self.__runs_by_id.init_ra,
                    self.__runs_by_id.end_ra,
                    self.__runs_by_id.init_dec,
                    self.__runs_by_id.end_dec,
                    self.__runs_by_id.init_altitude,
                    self.__runs_by_id.end_altitude,
                    self.__runs_by_id.init_azimuth,
                    self.__runs_by_id.end_azimuth,
                    self.__runs_by_id.init_time_collect_data,
                    self.__runs_by_id.end_time_collect_data
                )
            else:
                Checkers.print_object_filter_null(LstRuns.id_run.name, str(id_run))
                return create_runs(None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                                   None,
                                   None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_runs(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                           None, None)
