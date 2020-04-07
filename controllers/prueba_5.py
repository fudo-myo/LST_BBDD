from DTO.configuration_dto import ConfigurationDto
from entities.lst_pixel_group import LstPixelGroup
from services.lst_configuraction_service import LstConfigurationService
from services.lst_pixel_group_service import LstPixelGroupService

configService = LstConfigurationService()
pxel_group = LstPixelGroupService()

# gro = pxel_group.get_all_pixel_group()
# for row in gro:
#     print("prueba filtrada -> id_config:", row.id_config, )
#     print("prueba filtrada -> pixel_group_number:", row.pixel_group_number, )
#     print("prueba filtrada -> id_pixel_group:", row.id_pixel_group, )
#     print("prueba filtrada -> other_data:", row.other_data, "\n")

# config_insert_dto = ConfigurationDto()
# config_insert_dto.id_config = "dd"
# config_insert_dto.config_description = 'prueba insert'
# config_insert_dto.param_1 = 'insert p'
# config_insert_dto.param_2 = 'insert p'
# config_insert_dto.param_3 = 'insert p'
# configService.insert_config(config_insert_dto)
#
# configurationList = configService.get_all_config()
#
# for row in configurationList:
#     print("id:", row.id_config)
#     print("desc:", row.config_description, )
#     print("param1:", row.param_1, )
#     print("param2:", row.param_2, )
#     print("param3:", row.param_3, "\n")
#configService.delete_by_id(6)
#
#
# configuration = configService.get_config_by_id(2)
# print("prueba filtrada -> id:", configuration.id_config, )
# print("prueba filtrada -> desc:", configuration.config_description, )
# print("prueba filtrada -> param1:", configuration.param_1, )
# print("prueba filtrada -> param2:", configuration.param_2, )
# print("prueba filtrada -> param3:", configuration.param_3, "\n")

configService.update_config(7, None, 55, None, "sad param 3")
#print("Prueba id: '{}'".format(config_insert_dto.id_config))