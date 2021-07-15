from rest_framework import status, response


def exception_response(e):
    """
    :param e: exception message
    :return: exception occurred
    """
    return response.Response(
        {
            'status': 403,
            'error': e.__str__()
        },
        status=status.HTTP_403_FORBIDDEN
    )


def register_successfully():
    """
    :return: User registration successful and new user created
    """
    return response.Response(
        {
            'success': 'True',
            'message': 'User registered  successfully',
        },
        status=status.HTTP_201_CREATED,

    )


def login_successfully(serializer):
    """
    :param serializer:
    :return: Login Successfully
    """
    return response.Response(
        {
            'success': 'True',
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        },
        status=status.HTTP_200_OK,

    )


def not_found():
    return response.Response(
        {
            'status': 404,
            'message': 'User not found',
            'error': 'Invalid user'
        },
        status=status.HTTP_404_NOT_FOUND
    )


def get_otp(time_otp):
    return response.Response(
        {
            'status': 200,
            'message': f'User OTP: {time_otp} sent successfully',
        },
        status=status.HTTP_200_OK
    )


def change_password_successfully():
    return response.Response(
        {
            'status': 200,
            'message': 'change your password successfully',

        },
        status=status.HTTP_200_OK
    )


def verification_failed():
    return response.Response(
        {
            'status': 400,
            'message': 'Verification failed',
        },
        status=status.HTTP_400_BAD_REQUEST
    )


def password_not_match():
    return response.Response(
        {
            'status': 406,
            'message': 'The passwords are not matching'
        },
        status=status.HTTP_406_NOT_ACCEPTABLE
    )


def please_verify():
    return response.Response(
        {
            'status': 406,
            'message': 'Please verify your mail id before login'
        },
        status=status.HTTP_406_NOT_ACCEPTABLE
    )


def verified_successfully():
    return response.Response(
        {
            'status': 202,
            'message': 'email id verified successfully'
        },
        status=status.HTTP_202_ACCEPTED
    )


def profile_updated():
    return response.Response(
        {
            'status': 200,
            'message': 'profile updated successfully'
        },
        status=status.HTTP_200_OK
    )


def update_failed():
    return response.Response(
        {
            'status': 400,
            'message': 'update failed'
        },
        status=status.HTTP_400_BAD_REQUEST
    )


def profile_details(profile_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'details fetched successfully',
            'data': profile_ser.data
        },
        status=status.HTTP_200_OK
    )


def resource_added_successfully():
    return response.Response(
        {
            'status': 201,
            'message': 'resources added successfully'
        },
        status=status.HTTP_201_CREATED
    )


def resource_fetched_successfully(resource_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'all enabled resources fetched successfully',
            'data': resource_ser.data
        },
        status=status.HTTP_200_OK
    )


def resource_update_successfully(updated_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'Resource you requested get updated successfully',
            'data': updated_ser.data
        },
        status=status.HTTP_200_OK
    )


def resource_deleted():
    return response.Response(
        {
            'status': 200,
            'message': 'resource deleted successfully'
        },
        status=status.HTTP_200_OK
    )


def get_resource(resource_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'get the resource successfully',
            'data': resource_ser.data
        },
        status=status.HTTP_200_OK
    )


def disable_resource():
    return response.Response(
        {
            'status': 200,
            'message': 'disable the resource successfully'
        },
        status=status.HTTP_200_OK
    )


def enable_resource():
    return response.Response(
        {
            'status': 200,
            'message': 'enable the resource successfully'
        },
        status=status.HTTP_200_OK
    )


def new_meeting_scheduled():
    return response.Response(
        {
            'status': 201,
            'message': 'New meeting scheduled successfully'
        },
        status=status.HTTP_201_CREATED
    )


def get_booking_details(booking_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'Booking details fetched successfully',
            'data': booking_ser.data
        },
        status=status.HTTP_200_OK
    )


def no_data_found():
    return response.Response(
        {
            'status': 400,
            'message': 'no scheduled meetings found for user'
        },
        status=status.HTTP_400_BAD_REQUEST
    )


def booking_updated():
    return response.Response(
        {
            'status': 200,
            'message': 'booking updated successfully'
        },
        status=status.HTTP_200_OK
    )


def booking_deleted():
    return response.Response(
        {
            'status': 200,
            'message': 'delete the booking successfully'
        },
        status=status.HTTP_200_OK
    )


def get_search_result(serializer, result_count):
    return response.Response(
        {
            'status': 200,
            'message': 'search results fetched successfully',
            'count': result_count,
            'result': serializer.data

        },
        status=status.HTTP_200_OK
    )


def new_equipment_added():
    return response.Response(
        {
            'status': 201,
            'message': 'New equipment added successfully'
        },
        status=status.HTTP_201_CREATED
    )


def get_all_equipment(equipment_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'Equipments are fetched successfully',
            'data': equipment_ser.data
        },
        status=status.HTTP_200_OK
    )


def get_equipment_by_resource(equipment_resource_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'equipments fetched by resource successfully',
            'data': equipment_resource_ser.data
        },
        status=status.HTTP_200_OK
    )


def update_equipment():
    return response.Response(
        {
            'status': 200,
            'message': 'equipment details updated successfully',
        },
        status=status.HTTP_200_OK
    )


def equipment_deleted():
    return response.Response(
        {
            'status': 200,
            'message': 'equipment deleted successfully'
        }
    )


def get_equipment(equipment_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'Equipment details fetched successfully',
            'data': equipment_ser.data
        },
        status=status.HTTP_200_OK
    )


def resource_type_added():
    return response.Response(
        {
            'status': 201,
            'message': 'resource type added successfully'
        },
        status=status.HTTP_201_CREATED
    )


def update_resource_type():
    return response.Response(
        {
            'status': 200,
            'message': 'resource type updated successfully'
        },
        status=status.HTTP_200_OK
    )


def delete_type_deleted():
    return response.Response(
        {
            'status': 200,
            'message': 'resource type deleted successfully'
        },
        status=status.HTTP_200_OK
    )


def get_resource_type(resource_type_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'get the resource type successfully',
            'data': resource_type_ser.data
        },
        status=status.HTTP_200_OK

    )


def additional_service_added():
    return response.Response(
        {
            'status': 201,
            'message': 'additional service added successfully'
        },
        status=status.HTTP_201_CREATED
    )


def enter_the_id():
    return response.Response(
        {
            'status': 400,
            'message': 'please enter the id',
        },
        status=status.HTTP_400_BAD_REQUEST
    )


def get_additional_service(service_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'Additional service data fetched successfully',
            'data': service_ser.data
        }
    )


def additional_service_updated():
    return response.Response(
        {
            'status': 200,
            'message': 'additional service data updated successfully'
        },
        status=status.HTTP_200_OK
    )


def disable_service():
    return response.Response(
        {
            'status': 200,
            'message': 'Disable the service successfully'
        },
        status=status.HTTP_200_OK
    )


def enable_service():
    return response.Response(
        {
            'status': 200,
            'message': 'Enable the service successfully'
        },
        status=status.HTTP_200_OK
    )


def deleted_service():
    return response.Response(
        {
            'status': 200,
            'message': 'Delete the service successfully'
        },
        status=status.HTTP_200_OK
    )


def amenity_added():
    return response.Response(
        {
            'status': 201,
            'message': 'Amenity added successfully'
        },
        status=status.HTTP_201_CREATED
    )


def get_amenity_by_resource(amenity_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'get the amenities according to the resource',
            'data': amenity_ser.data
        },
        status=status.HTTP_200_OK
    )


def update_amenity():
    return response.Response(
        {
            'status': 200,
            'message': 'update the amenity successfully'
        },
        status=status.HTTP_200_OK
    )


def delete_amenity():
    return response.Response(
        {
            'status': 200,
            'message': 'amenity deleted successfully'
        },
        status=status.HTTP_200_OK
    )


def filtered_data(resource_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'resource data filtered successfully',
            'data': resource_ser.data
        },
        status=status.HTTP_200_OK
    )


def filtered_booking(booking_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'booking data filtered successfully',
            'data': booking_ser.data
        },
        status=status.HTTP_200_OK
    )


def add_new_stock():
    return response.Response(
        {
            'status': 201,
            'message': 'New stock of equipment added to the resource'
        },
        status=status.HTTP_201_CREATED
    )


def equipment_stock_updated():
    return response.Response(
        {
            'status': 200,
            'message': 'The equipment stock updated successfully'
        },
        status=status.HTTP_200_OK
    )


def get_equipment_stock(stock_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'The equipment stock fetched successfully',
            'data': stock_ser.data
        },
        status=status.HTTP_200_OK
    )


def add_additional_service_stock():
    return response.Response(
        {
            'status': 201,
            'message': 'The Additional service stock added successfully',
        },
        status=status.HTTP_201_CREATED
    )


def get_service_stock(service_stock_ser):
    return response.Response(
        {
            'status': 200,
            'message': 'The additional service stocks fetched successfully by resource',
            'data': service_stock_ser.data
        },
        status=status.HTTP_200_OK
    )


def update_service_stock():
    return response.Response(
        {
            'status': 200,
            'message': 'The Additional service stock get updated'
        },
        status=status.HTTP_200_OK
    )


def stock_error():
    return response.Response(
        {
            'status': 406,
            'message': 'quantity is larger than the stock left'
        },
        status=status.HTTP_406_NOT_ACCEPTABLE
    )


def fetch_data_response(model_info, data):
    return response.Response(

        {
            'status': 200,
            'message': f'{model_info} details fetched successfully',
            'data': data
        },
        status=status.HTTP_200_OK

    )


def not_available():
    return response.Response(
        {
            'status': 409,
            'message': 'Resource not available for this time slot'
        },
        status=status.HTTP_409_CONFLICT
    )


def select_option():
    return response.Response(
        {
            'status': 400,
            'message': 'Please select the option'

        },
        status=status.HTTP_400_BAD_REQUEST
    )
