import logging
from scipy import spatial
import sys
from mashop.microtoolkit.toolkit import APIError, status_codes
from mashop.utilities import build_uv_svr_error_response
from mashop.api.utils import (validate_params, convert_param_list_values, RGB, HEX_NAME_DICT)

logger = logging.getLogger(__name__)


def http_get(request, response, params):
    # -------- Validations -----------
    logger.debug(f'Validating the RGB color name query parameter')
    query_param = request.params.get('color')
    if not query_param:
        raise APIError(code='Invalid Input: color',
                       cause='Invalid Query Input: color',
                       message='Invalid Query parameter, Please enter query parameter =color',
                       status=status_codes.HTTP_NOT_FOUND,
                       extended_info=build_uv_svr_error_response(
                           server_message='Invalid Input: color',
                           server_control_name='errInvalidColor')
                       )
    required_params = {'color': [str]}
    validate_params(request.params, required_params=required_params)
    logger.debug(f'Check the query param contains 3 values for RGB color')
    if len(query_param) !=3:
        raise APIError(code='Insufficient number of Input: color',
                       cause='Invalid Query Input: color',
                       message='Inappropriate number of color code, Please Try to enter 3 values',
                       status=status_codes.HTTP_NOT_FOUND,
                       extended_info=build_uv_svr_error_response(
                           server_message='Invalid Input: color codes',
                           server_control_name='errInvalidNumberOfColorCodes'))

    query_param_list = convert_param_list_values(query_param)
    logger.debug(f'Mapping the RGB color code {query_param_list} in to its approximate color name')

    rgb_color_name = (RGB[spatial.KDTree(RGB).query(query_param_list)[1]])

    color_code_name = '#' \
        + format(rgb_color_name[0], 'x').zfill(2) \
        + format(rgb_color_name[1], 'x').zfill(2) \
        + format(rgb_color_name[2], 'x').zfill(2)
    color_hex = color_code_name.upper()
    color_difference = '(' + '{0:+d}'.format(rgb_color_name[0] - query_param_list[0]) \
        + ',' + '{0:+d}'.format(rgb_color_name[1] - query_param_list[1]) \
        + ',' + '{0:+d}'.format(rgb_color_name[2] - query_param_list[2]) \
        + ')'
    try:
        color_name = HEX_NAME_DICT[color_hex]
    except Exception as e:
        e = sys.exc_info()[0]
        raise APIError(code='Color Name not found',
                       cause='Invalid Input: RGB color code',
                       message=f'{e}',
                       status=status_codes.HTTP_NOT_FOUND,
                       extended_info=build_uv_svr_error_response(
                           server_message='Unable to find approximate color name',
                           server_control_name=f'{e}'))
    response.body = {'color_name': color_name,
                     'color_rgb': query_param_list,
                     'color_hex': color_hex,
                     'color_diff': color_difference}
    return response

