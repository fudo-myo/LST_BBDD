from typing import List

from sqlalchemy.exc import InvalidRequestError, OperationalError
from sqlalchemy.orm import Session

from DTO.configuration_dto import create_configuration, ConfigurationDto
from config.base import getSession
from utils.checkers import Checkers

try:
    from entities.lst_configuration import LstConfiguration
except ImportError as error:
    Checkers.print_exception_one_param(error)


class LstConfigurationService:

    def __init__(self):
        self.__session: Session = getSession()
        self.__all_config = None
        self.__config_by_id = None

    def insert_config(self, config_insert: ConfigurationDto):
        try:
            config_aux = LstConfiguration(
                config_description=config_insert.config_description,
                param_1=config_insert.param_1,
                param_2=config_insert.param_2,
                param_3=config_insert.param_3)
            self.__session.add(config_aux)
            self.__session.commit()
            if config_aux.id_config is not None:
                config_insert.id_config = config_aux.id_config
                print(" RECORD INSERTED IN TABLE '{}' WITH ID '{}' ".format(LstConfiguration.__tablename__.name,
                                                                            config_aux.id_config))
            else:
                print(" THE RECORD OF TABLE '{}' HAS NOT BEEN INSERTED".format(LstConfiguration.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def update_config(self, id_to_update, config_description=None, param_1=None, param_2=None, param_3=None):
        try:
            config_to_update_before: ConfigurationDto = self.get_config_by_id(id_to_update)
            if Checkers.validate_int(id_to_update,
                                     LstConfiguration.id_config.name) and config_to_update_before.id_config is not None:
                self.__session.query(LstConfiguration).filter(LstConfiguration.id_config.like(id_to_update)) \
                    .update({
                    LstConfiguration.config_description: Checkers.check_field_not_null(
                        LstConfiguration.config_description,
                        config_description),
                    LstConfiguration.param_1: Checkers.check_field_not_null(LstConfiguration.param_1, param_1),
                    LstConfiguration.param_2: Checkers.check_field_not_null(LstConfiguration.param_2, param_2),
                    LstConfiguration.param_3: Checkers.check_field_not_null(LstConfiguration.param_3, param_3)},
                    synchronize_session=False
                )
                self.__session.commit()
                config_to_update_after: ConfigurationDto = self.get_config_by_id(id_to_update)
                if config_to_update_before.__dict__ != config_to_update_after.__dict__:
                    print(" RECORD UPDATED IN TABLE '{}' WITH ID '{}' ".format(LstConfiguration.__tablename__.name,
                                                                               id_to_update))
                else:
                    print(" THE RECORD OF TABLE '{}' HAS NOT BEEN UPDATED".format(LstConfiguration.__tablename__.name))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE UPDATED ".format(LstConfiguration.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def delete_by_id(self, id_to_delete):
        try:
            config_to_delete_before: ConfigurationDto = self.get_config_by_id(id_to_delete)
            if Checkers.validate_int(id_to_delete,
                                     LstConfiguration.id_config.name) and config_to_delete_before.id_config is not None:
                self.__session.query(LstConfiguration).filter(LstConfiguration.id_config.like(id_to_delete)) \
                    .delete(synchronize_session=False)
                self.__session.commit()
                config_to_delete_after: ConfigurationDto = self.get_config_by_id(id_to_delete)
                if config_to_delete_before.id_config is not None and config_to_delete_after.id_config is None:
                    print(" RECORD DELETED IN TABLE '{}' WITH ID '{}' ".format(LstConfiguration.__tablename__.name,
                                                                               id_to_delete))
                else:
                    print(" THE RECORD OF TABLE '{}' WITH ID '{}' HAS NOT BEEN DELETED BECAUSE IT DID NOT EXIST".format(
                        LstConfiguration.__tablename__.name,
                        id_to_delete))
            else:
                print(" THE RECORD OF TABLE '{}' COULD NOT BE DELETED".format(LstConfiguration.__tablename__.name))

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

    def get_all_config(self):
        configuration_dto_list = []
        try:
            self.__all_config: List[ConfigurationDto] = self.__session.query(LstConfiguration).all()
            if len(self.__all_config) != 0:
                for row in self.__all_config:
                    config_aux = create_configuration(row.id_config,
                                                      row.config_description,
                                                      row.param_1,
                                                      row.param_2,
                                                      row.param_3)
                    configuration_dto_list.append(config_aux)
            else:
                Checkers.empty_list(LstConfiguration.__tablename__.name)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return configuration_dto_list

    def get_config_by_id(self, id_config):
        try:
            self.__config_by_id: ConfigurationDto = self.__session.query(LstConfiguration).filter(
                LstConfiguration.id_config.like(id_config)).first()
            if self.__config_by_id is not None:
                return create_configuration(self.__config_by_id.id_config,
                                            self.__config_by_id.config_description,
                                            self.__config_by_id.param_1,
                                            self.__config_by_id.param_2,
                                            self.__config_by_id.param_3)
            else:
                Checkers.print_object_filter_null(LstConfiguration.id_config.name, str(id_config))
                return create_configuration(None, None, None, None, None)

        except (InvalidRequestError, NameError) as error_request:
            Checkers.print_exception_one_param(error_request)
        except OperationalError as error_request2:
            Checkers.print_exception_two_params(error_request2.orig.args[1], error_request2.orig.args[0])

        return create_configuration(None, None, None, None, None)
